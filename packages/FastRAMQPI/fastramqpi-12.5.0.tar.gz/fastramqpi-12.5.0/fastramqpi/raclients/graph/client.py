# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from typing import Any
from typing import Coroutine
from typing import Dict
from typing import Optional
from typing import Type
from typing import Union
from typing import no_type_check

import httpx
from gql import Client as GQLClient
from gql.client import AsyncClientSession
from gql.client import SyncClientSession
from gql.transport import AsyncTransport
from graphql import DocumentNode
from pydantic import AnyHttpUrl

from ..auth import AuthenticatedAsyncHTTPXClient
from ..auth import AuthenticatedHTTPXClient
from ..auth import keycloak_token_endpoint
from ..graph.transport import AsyncHTTPXTransport
from ..graph.transport import HTTPXTransport


class GraphQLClient(GQLClient):
    transport: Union[HTTPXTransport, AsyncHTTPXTransport]

    def __init__(
        self,
        url: str,
        client_id: str,
        client_secret: str,
        auth_realm: str,
        auth_server: AnyHttpUrl,
        *args: Any,
        sync: bool = False,
        httpx_client_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ):
        """
        GQL Client wrapper providing defaults and automatic authentication for OS2mo.
        If you need a client with a persistent session, for example from a FastAPI
        application, consider the ``PersistentGraphQLClient`` subclass.

        Args:
            url: URL of the GraphQL server endpoint.
            client_id: Keycloak client id used for authentication.
            client_secret: Keycloak client secret used for authentication.
            auth_realm: Keycloak auth realm used for authentication.
            auth_server: URL of the Keycloak server used for authentication.
            *args: Extra arguments passed to the superclass init method.
            sync: If true, this client is initialised with a synchronous transport.
            httpx_client_kwargs: Extra keyword arguments passed to the HTTPX client.
            **kwargs: Extra keyword arguments passed to the superclass init method.

        Example:
            Asynchronously::

                client = GraphQLClient(
                    url="http://os2mo.example.org/graphql",
                    client_id="AzureDiamond",
                    client_secret="hunter2",
                    auth_realm="mordor",
                    auth_server="https://keycloak.example.org:8081/auth",
                )
                async with client as session:
                    query = gql(
                        ""'
                        query MOQuery {
                          ...
                        }
                        ""'
                    )
                    result = await session.execute(query)
                    print(result)

            Or synchronously::

                with GraphQLClient(sync=True) as session:
                    result = session.execute(query)
        """
        transport_cls: Type[Union[HTTPXTransport, AsyncHTTPXTransport]]
        client_cls: Type[Union[httpx.Client, httpx.AsyncClient]]

        if sync:
            transport_cls = HTTPXTransport
            client_cls = AuthenticatedHTTPXClient
        else:
            transport_cls = AsyncHTTPXTransport
            client_cls = AuthenticatedAsyncHTTPXClient

        transport = transport_cls(
            url=url,
            client_cls=client_cls,
            client_args=dict(
                client_id=client_id,
                client_secret=client_secret,
                token_endpoint=keycloak_token_endpoint(
                    auth_server=auth_server,
                    auth_realm=auth_realm,
                ),
                **(httpx_client_kwargs or {}),
            ),
        )

        super().__init__(*args, transport=transport, **kwargs)  # type: ignore[misc]


class PersistentGraphQLClient(GraphQLClient):
    """
    GraphQLClient with persistent transport session. Since the session is shared, it is
    the responsibility of the caller to call/await ``close()``/``aclose()`` when done.

    Example:
        Example usage in a FastAPI application. The global client is created in a module
        called ``clients.py``::

            graphql_client = PersistentGraphQLClient(
                url=f"{settings.mo_url}/graphql",
                client_id=settings.client_id,
                client_secret=settings.client_secret,
                auth_realm=settings.auth_realm,
                auth_server=settings.auth_server,
            )


        Using the client from anywhere::

            @app.get("/test")
            async def test():
                return await graphql_client.execute(...)

        We must make sure to close the client on shutdown. FastAPI makes this very easy
        using a ``shutdown`` signal in ``app.py``::

            def create_app():
                app = FastAPI()

                @app.on_event("shutdown")
                async def close_clients():
                    await graphql_client.aclose()

                return app
    """

    @no_type_check
    def execute(
        self, document: DocumentNode, *args: Any, **kwargs: Any
    ) -> Union[Dict, Coroutine[None, None, Dict]]:
        """
        Execute the provided document AST against the remote server using the transport
        provided during init.

        Either the transport is sync, and we execute the query synchronously directly
        OR the transport is async, and we return an awaitable coroutine which executes
        the query. In any case, the caller can ``execute(...)`` or ``await execute()``
        as expected from the call context.

        Args:
            document: The GraphQL request query.
            *args: Extra arguments passed to the transport execute method.
            **kwargs: Extra keyword arguments passed to the transport execute method.

        Returns: Dictionary (or coroutine) containing the result of the query.
        """
        if isinstance(self.transport, AsyncTransport):
            return self.execute_async(document, *args, **kwargs)
        return self.execute_sync(document, *args, **kwargs)

    def __enter__(self) -> SyncClientSession:
        """Persist the GraphQL client session by only opening it once."""
        if not hasattr(self, "session"):
            super().__enter__()
        return self.session  # type: ignore

    async def __aenter__(self) -> AsyncClientSession:
        """Persist the GraphQL client session by only opening it once."""
        if not hasattr(self, "session"):
            await super().__aenter__()
        return self.session  # type: ignore

    def __exit__(self, *args: Any) -> None:
        """We're a persistent client: Don't close the transport when exiting."""
        pass

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        """We're a persistent client: Don't close the transport when exiting."""
        pass

    def close(self) -> None:
        """
        Close the transport session.
        """
        super().__exit__()

    async def aclose(self) -> None:
        """
        Close the async transport session.
        """
        await super().__aexit__(None, None, None)
