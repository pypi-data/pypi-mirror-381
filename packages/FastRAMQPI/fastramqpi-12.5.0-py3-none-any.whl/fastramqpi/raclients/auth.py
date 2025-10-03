# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from typing import Any
from typing import Optional
from typing import cast

from authlib.integrations.httpx_client import (
    AsyncOAuth2Client as AsyncHTTPXOAuth2Client,
)
from authlib.integrations.httpx_client import OAuth2Client as HTTPXOAuth2Client
from authlib.oauth2 import OAuth2Client
from httpx import USE_CLIENT_DEFAULT
from httpx._types import AuthTypes
from pydantic import AnyHttpUrl
from pydantic import parse_obj_as


class BaseAuthenticatedClient(OAuth2Client):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        token_endpoint: AnyHttpUrl,
        *args: Any,
        grant_type: str = "client_credentials",
        token_endpoint_auth_method: str = "client_secret_post",
        **kwargs: Any,
    ):
        """
        Base used to implement authenticated HTTPX clients. Does not work on its own.

        Args:
            client_id: Client identifier used to obtain tokens.
            client_secret: Client secret used to obtain tokens.
            token_endpoint: OIDC token endpoint URL.
            *args: Other arguments, passed to Authlib's OAuth2Client.
            grant_type: OAuth2 grant type.
            token_endpoint_auth_method: RFC7591 client authentication method. Authlib
             supports 'client_secret_basic' (default), 'client_secret_post', and None.
            **kwargs: Other keyword arguments, passed to Authlib's OAuth2Client.
        """
        self.token_endpoint = token_endpoint

        super().__init__(
            *args,
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            token_endpoint=token_endpoint,
            token_endpoint_auth_method=token_endpoint_auth_method,
            **kwargs,
        )

    def should_fetch_token(
        self,
        url: str,
        withhold_token: bool = False,
        auth: Optional[AuthTypes] = USE_CLIENT_DEFAULT,  # type: ignore[assignment]
    ) -> bool:
        """
        Determine if we should fetch a token. Authlib automatically _refreshes_ tokens,
        but it does not fetch the initial one. Therefore, we should fetch a token the
        first time a request is sent; i.e. when self.token is None.

        Args:
            url: The URL of the request we are in the context of. Used to avoid
                 recursion, since fetching a token also uses our caller self.request().
            withhold_token: Forwarded from `self.request(..., withhold_token=False)`. If
             this is set, Authlib does not pass a token in the request, in which case
             there is no need to fetch one either.
            auth: Forwarded from `self.request(..., auth=USE_CLIENT_DEFAULT)`. If this
             is set, Authlib does not pass a token in the request, in which case there
             is no need to fetch one either.

        Returns: True if a token should be fetched. False otherwise.
        """
        return (
            not withhold_token
            and auth is USE_CLIENT_DEFAULT
            and self.token is None
            and url != self.token_endpoint
        )


def keycloak_token_endpoint(auth_server: AnyHttpUrl, auth_realm: str) -> AnyHttpUrl:
    """Construct keycloak token endpoint based on the given auth server and realm.

    Args:
        auth_server: HTTP URL of the authentication server.
        auth_realm: Keycloak realm used for authentication.

    Returns: Token endpoint URL.
    """
    return cast(  # wtf is even going on. mypy is so dumb
        AnyHttpUrl,
        parse_obj_as(
            AnyHttpUrl,
            f"{auth_server}/realms/{auth_realm}/protocol/openid-connect/token",
        ),
    )


class AuthenticatedHTTPXClient(BaseAuthenticatedClient, HTTPXOAuth2Client):
    """
    Synchronous HTTPX Client that automatically authenticates requests.

    Example usage::

        with AuthenticatedHTTPXClient(
            client_id="AzureDiamond",
            client_secret="hunter2",
            token_endpoint=keycloak_token_endpoint(
                auth_server=parse_obj_as(AnyHttpUrl, "https://keycloak.example.org/auth"),
                auth_realm="mordor",
            ),
        ) as client:
            r = client.get("https://example.org")

    """

    def request(
        self,
        method: str,
        url: str,
        withhold_token: bool = False,
        auth: AuthTypes = USE_CLIENT_DEFAULT,  # type: ignore[assignment]
        **kwargs: Any,
    ) -> Any:
        """
        Decorate Authlib's OAuth2Client.request() to automatically fetch a token the
        first time a request is made.

        Args:
            method: HTTP method. Forwarded to superclass.
            url: Request URL. Needed to determine if we should fetch_token().
            withhold_token: Needed to determine if we should fetch_token().
            auth: Authentication method. Needed to determine if we should fetch_token().
            **kwargs: Not used. Forwarded to superclass.

        Returns: HTTPX Response.
        """
        if self.should_fetch_token(url, withhold_token, auth):
            self.fetch_token()
        return super().request(method, url, withhold_token, auth, **kwargs)


class AuthenticatedAsyncHTTPXClient(BaseAuthenticatedClient, AsyncHTTPXOAuth2Client):
    """
    Asynchronous HTTPX Client that automatically authenticates requests.

    Example usage::

        async with AuthenticatedAsyncHTTPXClient(
            client_id="AzureDiamond",
            client_secret="hunter2",
            token_endpoint=keycloak_token_endpoint(
                auth_server=parse_obj_as(AnyHttpUrl, "https://keycloak.example.org/auth"),
                auth_realm="mordor",
            ),
        ) as client:
            r = await client.get("https://example.org")

    """

    async def request(
        self,
        method: str,
        url: str,
        withhold_token: bool = False,
        auth: AuthTypes = USE_CLIENT_DEFAULT,  # type: ignore[assignment]
        **kwargs: Any,
    ) -> Any:
        """
        Decorate Authlib's AsyncOAuth2Client.request() to automatically fetch a token
        the first time a request is made.

        Args:
            method: HTTP method. Forwarded to superclass.
            url: Request URL. Needed to determine if we should fetch_token().
            withhold_token: Needed to determine if we should fetch_token().
            auth: Authentication method. Needed to determine if we should fetch_token().
            **kwargs: Not used. Forwarded to superclass.

        Returns: HTTPX Response.
        """
        if self.should_fetch_token(url, withhold_token, auth):
            await self.fetch_token()
        return await super().request(method, url, withhold_token, auth, **kwargs)
