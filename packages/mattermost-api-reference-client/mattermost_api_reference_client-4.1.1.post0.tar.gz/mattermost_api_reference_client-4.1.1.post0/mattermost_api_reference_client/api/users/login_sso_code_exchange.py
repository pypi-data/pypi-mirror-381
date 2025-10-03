from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.login_sso_code_exchange_body import LoginSSOCodeExchangeBody
from ...models.login_sso_code_exchange_response_200 import LoginSSOCodeExchangeResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: LoginSSOCodeExchangeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/users/login/sso/code-exchange",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AppError, LoginSSOCodeExchangeResponse200]]:
    if response.status_code == 200:
        response_200 = LoginSSOCodeExchangeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = AppError.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AppError, LoginSSOCodeExchangeResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LoginSSOCodeExchangeBody,
) -> Response[Union[AppError, LoginSSOCodeExchangeResponse200]]:
    """Exchange SSO login code for session tokens

     Exchange a short-lived login_code for session tokens using SAML code exchange (mobile SSO flow).
    This endpoint is part of the mobile SSO code-exchange flow to prevent tokens  from appearing in deep
    links.
    ##### Permissions
    No permission required.

    Args:
        body (LoginSSOCodeExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppError, LoginSSOCodeExchangeResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LoginSSOCodeExchangeBody,
) -> Optional[Union[AppError, LoginSSOCodeExchangeResponse200]]:
    """Exchange SSO login code for session tokens

     Exchange a short-lived login_code for session tokens using SAML code exchange (mobile SSO flow).
    This endpoint is part of the mobile SSO code-exchange flow to prevent tokens  from appearing in deep
    links.
    ##### Permissions
    No permission required.

    Args:
        body (LoginSSOCodeExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppError, LoginSSOCodeExchangeResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LoginSSOCodeExchangeBody,
) -> Response[Union[AppError, LoginSSOCodeExchangeResponse200]]:
    """Exchange SSO login code for session tokens

     Exchange a short-lived login_code for session tokens using SAML code exchange (mobile SSO flow).
    This endpoint is part of the mobile SSO code-exchange flow to prevent tokens  from appearing in deep
    links.
    ##### Permissions
    No permission required.

    Args:
        body (LoginSSOCodeExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppError, LoginSSOCodeExchangeResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LoginSSOCodeExchangeBody,
) -> Optional[Union[AppError, LoginSSOCodeExchangeResponse200]]:
    """Exchange SSO login code for session tokens

     Exchange a short-lived login_code for session tokens using SAML code exchange (mobile SSO flow).
    This endpoint is part of the mobile SSO code-exchange flow to prevent tokens  from appearing in deep
    links.
    ##### Permissions
    No permission required.

    Args:
        body (LoginSSOCodeExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppError, LoginSSOCodeExchangeResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
