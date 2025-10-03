from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.command import Command
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    team_id: Union[Unset, str] = UNSET,
    custom_only: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["team_id"] = team_id

    params["custom_only"] = custom_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/commands",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AppError, list["Command"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Command.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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

    if response.status_code == 501:
        response_501 = AppError.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AppError, list["Command"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    team_id: Union[Unset, str] = UNSET,
    custom_only: Union[Unset, bool] = False,
) -> Response[Union[AppError, list["Command"]]]:
    """List commands for a team

     List commands for a team.
    ##### Permissions
    `manage_slash_commands` if need list custom commands.

    Args:
        team_id (Union[Unset, str]):
        custom_only (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppError, list['Command']]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        custom_only=custom_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    team_id: Union[Unset, str] = UNSET,
    custom_only: Union[Unset, bool] = False,
) -> Optional[Union[AppError, list["Command"]]]:
    """List commands for a team

     List commands for a team.
    ##### Permissions
    `manage_slash_commands` if need list custom commands.

    Args:
        team_id (Union[Unset, str]):
        custom_only (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppError, list['Command']]
    """

    return sync_detailed(
        client=client,
        team_id=team_id,
        custom_only=custom_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    team_id: Union[Unset, str] = UNSET,
    custom_only: Union[Unset, bool] = False,
) -> Response[Union[AppError, list["Command"]]]:
    """List commands for a team

     List commands for a team.
    ##### Permissions
    `manage_slash_commands` if need list custom commands.

    Args:
        team_id (Union[Unset, str]):
        custom_only (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppError, list['Command']]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        custom_only=custom_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    team_id: Union[Unset, str] = UNSET,
    custom_only: Union[Unset, bool] = False,
) -> Optional[Union[AppError, list["Command"]]]:
    """List commands for a team

     List commands for a team.
    ##### Permissions
    `manage_slash_commands` if need list custom commands.

    Args:
        team_id (Union[Unset, str]):
        custom_only (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppError, list['Command']]
    """

    return (
        await asyncio_detailed(
            client=client,
            team_id=team_id,
            custom_only=custom_only,
        )
    ).parsed
