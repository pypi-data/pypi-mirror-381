from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.relation_request import RelationRequest
from ...models.relation_response import RelationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source: str,
    target: str,
    *,
    body: RelationRequest,
    relation_type: str,
    api_key_header_value: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["relation_type"] = relation_type

    json_api_key_header_value: Union[None, Unset, str]
    if isinstance(api_key_header_value, Unset):
        json_api_key_header_value = UNSET
    else:
        json_api_key_header_value = api_key_header_value
    params["api_key_header_value"] = json_api_key_header_value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/relations/{source}/{target}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, RelationResponse]]:
    if response.status_code == 200:
        response_200 = RelationResponse.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, RelationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source: str,
    target: str,
    *,
    client: AuthenticatedClient,
    body: RelationRequest,
    relation_type: str,
    api_key_header_value: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, RelationResponse]]:
    r"""Edit Relation

     Updates relation (edge) information in the knowledge graph and re-embeds the relation in the vector
    database.

    Args:
        source_entity: Name of the source entity
        target_entity: Name of the target entity
        updated_data: Dictionary containing updated attributes, e.g. {\"description\": \"new
    description\", \"keywords\": \"new keywords\"}

    Returns:
        Dictionary containing updated relation information

    Args:
        source (str):
        target (str):
        relation_type (str):
        api_key_header_value (Union[None, Unset, str]):
        body (RelationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RelationResponse]]
    """

    kwargs = _get_kwargs(
        source=source,
        target=target,
        body=body,
        relation_type=relation_type,
        api_key_header_value=api_key_header_value,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source: str,
    target: str,
    *,
    client: AuthenticatedClient,
    body: RelationRequest,
    relation_type: str,
    api_key_header_value: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, RelationResponse]]:
    r"""Edit Relation

     Updates relation (edge) information in the knowledge graph and re-embeds the relation in the vector
    database.

    Args:
        source_entity: Name of the source entity
        target_entity: Name of the target entity
        updated_data: Dictionary containing updated attributes, e.g. {\"description\": \"new
    description\", \"keywords\": \"new keywords\"}

    Returns:
        Dictionary containing updated relation information

    Args:
        source (str):
        target (str):
        relation_type (str):
        api_key_header_value (Union[None, Unset, str]):
        body (RelationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, RelationResponse]
    """

    return sync_detailed(
        source=source,
        target=target,
        client=client,
        body=body,
        relation_type=relation_type,
        api_key_header_value=api_key_header_value,
    ).parsed


async def asyncio_detailed(
    source: str,
    target: str,
    *,
    client: AuthenticatedClient,
    body: RelationRequest,
    relation_type: str,
    api_key_header_value: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, RelationResponse]]:
    r"""Edit Relation

     Updates relation (edge) information in the knowledge graph and re-embeds the relation in the vector
    database.

    Args:
        source_entity: Name of the source entity
        target_entity: Name of the target entity
        updated_data: Dictionary containing updated attributes, e.g. {\"description\": \"new
    description\", \"keywords\": \"new keywords\"}

    Returns:
        Dictionary containing updated relation information

    Args:
        source (str):
        target (str):
        relation_type (str):
        api_key_header_value (Union[None, Unset, str]):
        body (RelationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RelationResponse]]
    """

    kwargs = _get_kwargs(
        source=source,
        target=target,
        body=body,
        relation_type=relation_type,
        api_key_header_value=api_key_header_value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source: str,
    target: str,
    *,
    client: AuthenticatedClient,
    body: RelationRequest,
    relation_type: str,
    api_key_header_value: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, RelationResponse]]:
    r"""Edit Relation

     Updates relation (edge) information in the knowledge graph and re-embeds the relation in the vector
    database.

    Args:
        source_entity: Name of the source entity
        target_entity: Name of the target entity
        updated_data: Dictionary containing updated attributes, e.g. {\"description\": \"new
    description\", \"keywords\": \"new keywords\"}

    Returns:
        Dictionary containing updated relation information

    Args:
        source (str):
        target (str):
        relation_type (str):
        api_key_header_value (Union[None, Unset, str]):
        body (RelationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, RelationResponse]
    """

    return (
        await asyncio_detailed(
            source=source,
            target=target,
            client=client,
            body=body,
            relation_type=relation_type,
            api_key_header_value=api_key_header_value,
        )
    ).parsed
