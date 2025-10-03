from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.access_control_policy_test_response import AccessControlPolicyTestResponse
from ...models.app_error import AppError
from ...models.query_expression_params import QueryExpressionParams
from ...types import Response


def _get_kwargs(
    *,
    body: QueryExpressionParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/access_control_policies/cel/test",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccessControlPolicyTestResponse, AppError]]:
    if response.status_code == 200:
        response_200 = AccessControlPolicyTestResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AppError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AppError.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = AppError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AccessControlPolicyTestResponse, AppError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QueryExpressionParams,
) -> Response[Union[AccessControlPolicyTestResponse, AppError]]:
    """Test an access control policy expression

     Tests an access control policy expression against users to see who would be affected.
    ##### Permissions
    Must have the `manage_system` permission.

    Args:
        body (QueryExpressionParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessControlPolicyTestResponse, AppError]]
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
    body: QueryExpressionParams,
) -> Optional[Union[AccessControlPolicyTestResponse, AppError]]:
    """Test an access control policy expression

     Tests an access control policy expression against users to see who would be affected.
    ##### Permissions
    Must have the `manage_system` permission.

    Args:
        body (QueryExpressionParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessControlPolicyTestResponse, AppError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QueryExpressionParams,
) -> Response[Union[AccessControlPolicyTestResponse, AppError]]:
    """Test an access control policy expression

     Tests an access control policy expression against users to see who would be affected.
    ##### Permissions
    Must have the `manage_system` permission.

    Args:
        body (QueryExpressionParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessControlPolicyTestResponse, AppError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QueryExpressionParams,
) -> Optional[Union[AccessControlPolicyTestResponse, AppError]]:
    """Test an access control policy expression

     Tests an access control policy expression against users to see who would be affected.
    ##### Permissions
    Must have the `manage_system` permission.

    Args:
        body (QueryExpressionParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessControlPolicyTestResponse, AppError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
