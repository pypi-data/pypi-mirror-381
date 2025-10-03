from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.validate_expression_against_requester_body import ValidateExpressionAgainstRequesterBody
from ...models.validate_expression_against_requester_response_200 import ValidateExpressionAgainstRequesterResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: ValidateExpressionAgainstRequesterBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/access_control_policies/cel/validate_requester",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AppError, ValidateExpressionAgainstRequesterResponse200]]:
    if response.status_code == 200:
        response_200 = ValidateExpressionAgainstRequesterResponse200.from_dict(response.json())

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
) -> Response[Union[AppError, ValidateExpressionAgainstRequesterResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateExpressionAgainstRequesterBody,
) -> Response[Union[AppError, ValidateExpressionAgainstRequesterResponse200]]:
    """Validate if the current user matches a CEL expression

     Validates whether the current authenticated user matches the given CEL expression.
    This is used to determine if a channel admin can test expressions they match.
    ##### Permissions
    Must have `manage_system` permission OR be a channel admin for the specified channel (channelId
    required for channel admins).

    Args:
        body (ValidateExpressionAgainstRequesterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppError, ValidateExpressionAgainstRequesterResponse200]]
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
    body: ValidateExpressionAgainstRequesterBody,
) -> Optional[Union[AppError, ValidateExpressionAgainstRequesterResponse200]]:
    """Validate if the current user matches a CEL expression

     Validates whether the current authenticated user matches the given CEL expression.
    This is used to determine if a channel admin can test expressions they match.
    ##### Permissions
    Must have `manage_system` permission OR be a channel admin for the specified channel (channelId
    required for channel admins).

    Args:
        body (ValidateExpressionAgainstRequesterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppError, ValidateExpressionAgainstRequesterResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateExpressionAgainstRequesterBody,
) -> Response[Union[AppError, ValidateExpressionAgainstRequesterResponse200]]:
    """Validate if the current user matches a CEL expression

     Validates whether the current authenticated user matches the given CEL expression.
    This is used to determine if a channel admin can test expressions they match.
    ##### Permissions
    Must have `manage_system` permission OR be a channel admin for the specified channel (channelId
    required for channel admins).

    Args:
        body (ValidateExpressionAgainstRequesterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppError, ValidateExpressionAgainstRequesterResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateExpressionAgainstRequesterBody,
) -> Optional[Union[AppError, ValidateExpressionAgainstRequesterResponse200]]:
    """Validate if the current user matches a CEL expression

     Validates whether the current authenticated user matches the given CEL expression.
    This is used to determine if a channel admin can test expressions they match.
    ##### Permissions
    Must have `manage_system` permission OR be a channel admin for the specified channel (channelId
    required for channel admins).

    Args:
        body (ValidateExpressionAgainstRequesterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppError, ValidateExpressionAgainstRequesterResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
