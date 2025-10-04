# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Union, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ItemsWrapper
from ...types.doc import Doc
from ...pagination import SyncOffsetPagination, AsyncOffsetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.agents import doc_list_params, doc_create_params, doc_search_params, doc_bulk_delete_params
from ...types.agents.doc_delete_response import DocDeleteResponse
from ...types.agents.doc_search_response import DocSearchResponse
from ...types.agents.doc_bulk_delete_response import DocBulkDeleteResponse

__all__ = ["DocsResource", "AsyncDocsResource"]


class DocsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return DocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return DocsResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        content: Union[str, SequenceNotStr[str]],
        title: str,
        connection_pool: object | Omit = omit,
        embed_instruction: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Doc:
        """
        Create Agent Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}/docs",
            body=maybe_transform(
                {
                    "content": content,
                    "title": title,
                    "embed_instruction": embed_instruction,
                    "metadata": metadata,
                },
                doc_create_params.DocCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"connection_pool": connection_pool}, doc_create_params.DocCreateParams),
            ),
            cast_to=Doc,
        )

    def list(
        self,
        agent_id: str,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        include_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: Dict[str, object] | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[Doc]:
        """
        List Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/agents/{agent_id}/docs",
            page=SyncOffsetPagination[Doc],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "include_embeddings": include_embeddings,
                        "limit": limit,
                        "metadata_filter": metadata_filter,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    doc_list_params.DocListParams,
                ),
            ),
            model=Doc,
        )

    def delete(
        self,
        doc_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocDeleteResponse:
        """
        Delete Agent Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return self._delete(
            f"/agents/{agent_id}/docs/{doc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocDeleteResponse,
        )

    def bulk_delete(
        self,
        agent_id: str,
        *,
        delete_all: bool | Omit = omit,
        metadata_filter: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocBulkDeleteResponse:
        """
        Bulk delete documents owned by an agent based on metadata filter

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._delete(
            f"/agents/{agent_id}/docs",
            body=maybe_transform(
                {
                    "delete_all": delete_all,
                    "metadata_filter": metadata_filter,
                },
                doc_bulk_delete_params.DocBulkDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ItemsWrapper[DocBulkDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DocBulkDeleteResponse], ItemsWrapper[DocBulkDeleteResponse]),
        )

    @overload
    def search(
        self,
        agent_id: str,
        *,
        text: str,
        connection_pool: object | Omit = omit,
        include_embeddings: bool | Omit = omit,
        lang: str | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: object | Omit = omit,
        trigram_similarity_threshold: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocSearchResponse:
        """
        Searches for documents associated with a specific agent.

        Parameters: x_developer_id (UUID): The unique identifier of the developer
        associated with the agent. search_params (TextOnlyDocSearchRequest |
        VectorDocSearchRequest | HybridDocSearchRequest): The parameters for the search.
        agent_id (UUID): The umnique identifier of the agent associated with the
        documents. Returns: DocSearchResponse: The search results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def search(
        self,
        agent_id: str,
        *,
        vector: Iterable[float],
        connection_pool: object | Omit = omit,
        confidence: float | Omit = omit,
        include_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: object | Omit = omit,
        mmr_strength: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocSearchResponse:
        """
        Searches for documents associated with a specific agent.

        Parameters: x_developer_id (UUID): The unique identifier of the developer
        associated with the agent. search_params (TextOnlyDocSearchRequest |
        VectorDocSearchRequest | HybridDocSearchRequest): The parameters for the search.
        agent_id (UUID): The umnique identifier of the agent associated with the
        documents. Returns: DocSearchResponse: The search results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def search(
        self,
        agent_id: str,
        *,
        text: str,
        vector: Iterable[float],
        connection_pool: object | Omit = omit,
        alpha: float | Omit = omit,
        confidence: float | Omit = omit,
        include_embeddings: bool | Omit = omit,
        k_multiplier: int | Omit = omit,
        lang: str | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: object | Omit = omit,
        mmr_strength: float | Omit = omit,
        trigram_similarity_threshold: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocSearchResponse:
        """
        Searches for documents associated with a specific agent.

        Parameters: x_developer_id (UUID): The unique identifier of the developer
        associated with the agent. search_params (TextOnlyDocSearchRequest |
        VectorDocSearchRequest | HybridDocSearchRequest): The parameters for the search.
        agent_id (UUID): The umnique identifier of the agent associated with the
        documents. Returns: DocSearchResponse: The search results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["text"], ["vector"], ["text", "vector"])
    def search(
        self,
        agent_id: str,
        *,
        text: str | Omit = omit,
        connection_pool: object | Omit = omit,
        include_embeddings: bool | Omit = omit,
        lang: str | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: object | Omit = omit,
        trigram_similarity_threshold: Optional[float] | Omit = omit,
        vector: Iterable[float] | Omit = omit,
        confidence: float | Omit = omit,
        mmr_strength: float | Omit = omit,
        alpha: float | Omit = omit,
        k_multiplier: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocSearchResponse:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}/search",
            body=maybe_transform(
                {
                    "text": text,
                    "include_embeddings": include_embeddings,
                    "lang": lang,
                    "limit": limit,
                    "metadata_filter": metadata_filter,
                    "trigram_similarity_threshold": trigram_similarity_threshold,
                    "vector": vector,
                    "confidence": confidence,
                    "mmr_strength": mmr_strength,
                    "alpha": alpha,
                    "k_multiplier": k_multiplier,
                },
                doc_search_params.DocSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"connection_pool": connection_pool}, doc_search_params.DocSearchParams),
            ),
            cast_to=DocSearchResponse,
        )


class AsyncDocsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return AsyncDocsResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        content: Union[str, SequenceNotStr[str]],
        title: str,
        connection_pool: object | Omit = omit,
        embed_instruction: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Doc:
        """
        Create Agent Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}/docs",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "title": title,
                    "embed_instruction": embed_instruction,
                    "metadata": metadata,
                },
                doc_create_params.DocCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"connection_pool": connection_pool}, doc_create_params.DocCreateParams
                ),
            ),
            cast_to=Doc,
        )

    def list(
        self,
        agent_id: str,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        include_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: Dict[str, object] | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Doc, AsyncOffsetPagination[Doc]]:
        """
        List Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/agents/{agent_id}/docs",
            page=AsyncOffsetPagination[Doc],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "include_embeddings": include_embeddings,
                        "limit": limit,
                        "metadata_filter": metadata_filter,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    doc_list_params.DocListParams,
                ),
            ),
            model=Doc,
        )

    async def delete(
        self,
        doc_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocDeleteResponse:
        """
        Delete Agent Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return await self._delete(
            f"/agents/{agent_id}/docs/{doc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocDeleteResponse,
        )

    async def bulk_delete(
        self,
        agent_id: str,
        *,
        delete_all: bool | Omit = omit,
        metadata_filter: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocBulkDeleteResponse:
        """
        Bulk delete documents owned by an agent based on metadata filter

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._delete(
            f"/agents/{agent_id}/docs",
            body=await async_maybe_transform(
                {
                    "delete_all": delete_all,
                    "metadata_filter": metadata_filter,
                },
                doc_bulk_delete_params.DocBulkDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ItemsWrapper[DocBulkDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DocBulkDeleteResponse], ItemsWrapper[DocBulkDeleteResponse]),
        )

    @overload
    async def search(
        self,
        agent_id: str,
        *,
        text: str,
        connection_pool: object | Omit = omit,
        include_embeddings: bool | Omit = omit,
        lang: str | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: object | Omit = omit,
        trigram_similarity_threshold: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocSearchResponse:
        """
        Searches for documents associated with a specific agent.

        Parameters: x_developer_id (UUID): The unique identifier of the developer
        associated with the agent. search_params (TextOnlyDocSearchRequest |
        VectorDocSearchRequest | HybridDocSearchRequest): The parameters for the search.
        agent_id (UUID): The umnique identifier of the agent associated with the
        documents. Returns: DocSearchResponse: The search results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def search(
        self,
        agent_id: str,
        *,
        vector: Iterable[float],
        connection_pool: object | Omit = omit,
        confidence: float | Omit = omit,
        include_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: object | Omit = omit,
        mmr_strength: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocSearchResponse:
        """
        Searches for documents associated with a specific agent.

        Parameters: x_developer_id (UUID): The unique identifier of the developer
        associated with the agent. search_params (TextOnlyDocSearchRequest |
        VectorDocSearchRequest | HybridDocSearchRequest): The parameters for the search.
        agent_id (UUID): The umnique identifier of the agent associated with the
        documents. Returns: DocSearchResponse: The search results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def search(
        self,
        agent_id: str,
        *,
        text: str,
        vector: Iterable[float],
        connection_pool: object | Omit = omit,
        alpha: float | Omit = omit,
        confidence: float | Omit = omit,
        include_embeddings: bool | Omit = omit,
        k_multiplier: int | Omit = omit,
        lang: str | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: object | Omit = omit,
        mmr_strength: float | Omit = omit,
        trigram_similarity_threshold: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocSearchResponse:
        """
        Searches for documents associated with a specific agent.

        Parameters: x_developer_id (UUID): The unique identifier of the developer
        associated with the agent. search_params (TextOnlyDocSearchRequest |
        VectorDocSearchRequest | HybridDocSearchRequest): The parameters for the search.
        agent_id (UUID): The umnique identifier of the agent associated with the
        documents. Returns: DocSearchResponse: The search results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["text"], ["vector"], ["text", "vector"])
    async def search(
        self,
        agent_id: str,
        *,
        text: str | Omit = omit,
        connection_pool: object | Omit = omit,
        include_embeddings: bool | Omit = omit,
        lang: str | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: object | Omit = omit,
        trigram_similarity_threshold: Optional[float] | Omit = omit,
        vector: Iterable[float] | Omit = omit,
        confidence: float | Omit = omit,
        mmr_strength: float | Omit = omit,
        alpha: float | Omit = omit,
        k_multiplier: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocSearchResponse:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}/search",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "include_embeddings": include_embeddings,
                    "lang": lang,
                    "limit": limit,
                    "metadata_filter": metadata_filter,
                    "trigram_similarity_threshold": trigram_similarity_threshold,
                    "vector": vector,
                    "confidence": confidence,
                    "mmr_strength": mmr_strength,
                    "alpha": alpha,
                    "k_multiplier": k_multiplier,
                },
                doc_search_params.DocSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"connection_pool": connection_pool}, doc_search_params.DocSearchParams
                ),
            ),
            cast_to=DocSearchResponse,
        )


class DocsResourceWithRawResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

        self.create = to_raw_response_wrapper(
            docs.create,
        )
        self.list = to_raw_response_wrapper(
            docs.list,
        )
        self.delete = to_raw_response_wrapper(
            docs.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            docs.bulk_delete,
        )
        self.search = to_raw_response_wrapper(
            docs.search,
        )


class AsyncDocsResourceWithRawResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

        self.create = async_to_raw_response_wrapper(
            docs.create,
        )
        self.list = async_to_raw_response_wrapper(
            docs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            docs.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            docs.bulk_delete,
        )
        self.search = async_to_raw_response_wrapper(
            docs.search,
        )


class DocsResourceWithStreamingResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

        self.create = to_streamed_response_wrapper(
            docs.create,
        )
        self.list = to_streamed_response_wrapper(
            docs.list,
        )
        self.delete = to_streamed_response_wrapper(
            docs.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            docs.bulk_delete,
        )
        self.search = to_streamed_response_wrapper(
            docs.search,
        )


class AsyncDocsResourceWithStreamingResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

        self.create = async_to_streamed_response_wrapper(
            docs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            docs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            docs.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            docs.bulk_delete,
        )
        self.search = async_to_streamed_response_wrapper(
            docs.search,
        )
