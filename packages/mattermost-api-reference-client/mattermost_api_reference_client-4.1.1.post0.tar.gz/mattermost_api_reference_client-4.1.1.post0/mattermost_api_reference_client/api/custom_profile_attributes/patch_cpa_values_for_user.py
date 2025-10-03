from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.patch_cpa_values_for_user_body_item import PatchCPAValuesForUserBodyItem
from ...models.patch_cpa_values_for_user_response_200_item import PatchCPAValuesForUserResponse200Item
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: list["PatchCPAValuesForUserBodyItem"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v4/users/{user_id}/custom_profile_attributes",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AppError, list["PatchCPAValuesForUserResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PatchCPAValuesForUserResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = AppError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AppError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AppError, list["PatchCPAValuesForUserResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["PatchCPAValuesForUserBodyItem"],
) -> Response[Union[AppError, list["PatchCPAValuesForUserResponse200Item"]]]:
    """Update custom profile attribute values for a user

     Update Custom Profile Attribute field values for a specific user.

    _This endpoint is experimental._

    __Minimum server version__: 11

    ##### Permissions
    Must have permission to edit the user. Users can only edit their own CPA values unless they are
    system administrators.

    Args:
        user_id (str):
        body (list['PatchCPAValuesForUserBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppError, list['PatchCPAValuesForUserResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["PatchCPAValuesForUserBodyItem"],
) -> Optional[Union[AppError, list["PatchCPAValuesForUserResponse200Item"]]]:
    """Update custom profile attribute values for a user

     Update Custom Profile Attribute field values for a specific user.

    _This endpoint is experimental._

    __Minimum server version__: 11

    ##### Permissions
    Must have permission to edit the user. Users can only edit their own CPA values unless they are
    system administrators.

    Args:
        user_id (str):
        body (list['PatchCPAValuesForUserBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppError, list['PatchCPAValuesForUserResponse200Item']]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["PatchCPAValuesForUserBodyItem"],
) -> Response[Union[AppError, list["PatchCPAValuesForUserResponse200Item"]]]:
    """Update custom profile attribute values for a user

     Update Custom Profile Attribute field values for a specific user.

    _This endpoint is experimental._

    __Minimum server version__: 11

    ##### Permissions
    Must have permission to edit the user. Users can only edit their own CPA values unless they are
    system administrators.

    Args:
        user_id (str):
        body (list['PatchCPAValuesForUserBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppError, list['PatchCPAValuesForUserResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["PatchCPAValuesForUserBodyItem"],
) -> Optional[Union[AppError, list["PatchCPAValuesForUserResponse200Item"]]]:
    """Update custom profile attribute values for a user

     Update Custom Profile Attribute field values for a specific user.

    _This endpoint is experimental._

    __Minimum server version__: 11

    ##### Permissions
    Must have permission to edit the user. Users can only edit their own CPA values unless they are
    system administrators.

    Args:
        user_id (str):
        body (list['PatchCPAValuesForUserBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppError, list['PatchCPAValuesForUserResponse200Item']]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
