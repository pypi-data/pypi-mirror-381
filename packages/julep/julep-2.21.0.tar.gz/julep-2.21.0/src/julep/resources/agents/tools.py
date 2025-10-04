# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPagination, AsyncOffsetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.agents import tool_list_params, tool_reset_params, tool_create_params, tool_update_params
from ...types.shared_params.system_def import SystemDef
from ...types.agents.tool_list_response import ToolListResponse
from ...types.agents.tool_reset_response import ToolResetResponse
from ...types.shared_params.function_def import FunctionDef
from ...types.agents.tool_create_response import ToolCreateResponse
from ...types.agents.tool_delete_response import ToolDeleteResponse
from ...types.agents.tool_update_response import ToolUpdateResponse
from ...types.shared_params.bash20241022_def import Bash20241022Def
from ...types.shared_params.computer20241022_def import Computer20241022Def
from ...types.shared_params.text_editor20241022_def import TextEditor20241022Def

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        name: str,
        type: Literal[
            "function",
            "integration",
            "system",
            "api_call",
            "computer_20241022",
            "text_editor_20241022",
            "bash_20241022",
        ],
        api_call: Optional[tool_create_params.APICall] | Omit = omit,
        bash_20241022: Optional[Bash20241022Def] | Omit = omit,
        computer_20241022: Optional[Computer20241022Def] | Omit = omit,
        description: Optional[str] | Omit = omit,
        function: Optional[FunctionDef] | Omit = omit,
        integration: Optional[tool_create_params.Integration] | Omit = omit,
        system: Optional[SystemDef] | Omit = omit,
        text_editor_20241022: Optional[TextEditor20241022Def] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateResponse:
        """
        Create Agent Tool

        Args:
          api_call: API call definition

          computer_20241022: Anthropic new tools

          function: Function definition

          integration: Brave integration definition

          system: System definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}/tools",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "api_call": api_call,
                    "bash_20241022": bash_20241022,
                    "computer_20241022": computer_20241022,
                    "description": description,
                    "function": function,
                    "integration": integration,
                    "system": system,
                    "text_editor_20241022": text_editor_20241022,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCreateResponse,
        )

    def update(
        self,
        tool_id: str,
        *,
        agent_id: str,
        api_call: Optional[tool_update_params.APICall] | Omit = omit,
        bash_20241022: Optional[tool_update_params.Bash20241022] | Omit = omit,
        computer_20241022: Optional[tool_update_params.Computer20241022] | Omit = omit,
        description: Optional[str] | Omit = omit,
        function: Optional[FunctionDef] | Omit = omit,
        integration: Optional[tool_update_params.Integration] | Omit = omit,
        name: Optional[str] | Omit = omit,
        system: Optional[tool_update_params.System] | Omit = omit,
        text_editor_20241022: Optional[tool_update_params.TextEditor20241022] | Omit = omit,
        type: Optional[
            Literal[
                "function",
                "integration",
                "system",
                "api_call",
                "computer_20241022",
                "text_editor_20241022",
                "bash_20241022",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolUpdateResponse:
        """
        Patch Agent Tool

        Args:
          api_call: API call definition

          computer_20241022: Anthropic new tools

          function: Function definition

          integration: Brave integration definition

          system: System definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._patch(
            f"/agents/{agent_id}/tools/{tool_id}",
            body=maybe_transform(
                {
                    "api_call": api_call,
                    "bash_20241022": bash_20241022,
                    "computer_20241022": computer_20241022,
                    "description": description,
                    "function": function,
                    "integration": integration,
                    "name": name,
                    "system": system,
                    "text_editor_20241022": text_editor_20241022,
                    "type": type,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolUpdateResponse,
        )

    def list(
        self,
        agent_id: str,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ToolListResponse]:
        """
        List Agent Tools

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/agents/{agent_id}/tools",
            page=SyncOffsetPagination[ToolListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            model=ToolListResponse,
        )

    def delete(
        self,
        tool_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolDeleteResponse:
        """
        Delete Agent Tool

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._delete(
            f"/agents/{agent_id}/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolDeleteResponse,
        )

    def reset(
        self,
        tool_id: str,
        *,
        agent_id: str,
        name: str,
        type: Literal[
            "function",
            "integration",
            "system",
            "api_call",
            "computer_20241022",
            "text_editor_20241022",
            "bash_20241022",
        ],
        api_call: Optional[tool_reset_params.APICall] | Omit = omit,
        bash_20241022: Optional[Bash20241022Def] | Omit = omit,
        computer_20241022: Optional[Computer20241022Def] | Omit = omit,
        description: Optional[str] | Omit = omit,
        function: Optional[FunctionDef] | Omit = omit,
        integration: Optional[tool_reset_params.Integration] | Omit = omit,
        system: Optional[SystemDef] | Omit = omit,
        text_editor_20241022: Optional[TextEditor20241022Def] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolResetResponse:
        """
        Update Agent Tool

        Args:
          api_call: API call definition

          computer_20241022: Anthropic new tools

          function: Function definition

          integration: Brave integration definition

          system: System definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._put(
            f"/agents/{agent_id}/tools/{tool_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "api_call": api_call,
                    "bash_20241022": bash_20241022,
                    "computer_20241022": computer_20241022,
                    "description": description,
                    "function": function,
                    "integration": integration,
                    "system": system,
                    "text_editor_20241022": text_editor_20241022,
                },
                tool_reset_params.ToolResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResetResponse,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        name: str,
        type: Literal[
            "function",
            "integration",
            "system",
            "api_call",
            "computer_20241022",
            "text_editor_20241022",
            "bash_20241022",
        ],
        api_call: Optional[tool_create_params.APICall] | Omit = omit,
        bash_20241022: Optional[Bash20241022Def] | Omit = omit,
        computer_20241022: Optional[Computer20241022Def] | Omit = omit,
        description: Optional[str] | Omit = omit,
        function: Optional[FunctionDef] | Omit = omit,
        integration: Optional[tool_create_params.Integration] | Omit = omit,
        system: Optional[SystemDef] | Omit = omit,
        text_editor_20241022: Optional[TextEditor20241022Def] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateResponse:
        """
        Create Agent Tool

        Args:
          api_call: API call definition

          computer_20241022: Anthropic new tools

          function: Function definition

          integration: Brave integration definition

          system: System definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}/tools",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "api_call": api_call,
                    "bash_20241022": bash_20241022,
                    "computer_20241022": computer_20241022,
                    "description": description,
                    "function": function,
                    "integration": integration,
                    "system": system,
                    "text_editor_20241022": text_editor_20241022,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCreateResponse,
        )

    async def update(
        self,
        tool_id: str,
        *,
        agent_id: str,
        api_call: Optional[tool_update_params.APICall] | Omit = omit,
        bash_20241022: Optional[tool_update_params.Bash20241022] | Omit = omit,
        computer_20241022: Optional[tool_update_params.Computer20241022] | Omit = omit,
        description: Optional[str] | Omit = omit,
        function: Optional[FunctionDef] | Omit = omit,
        integration: Optional[tool_update_params.Integration] | Omit = omit,
        name: Optional[str] | Omit = omit,
        system: Optional[tool_update_params.System] | Omit = omit,
        text_editor_20241022: Optional[tool_update_params.TextEditor20241022] | Omit = omit,
        type: Optional[
            Literal[
                "function",
                "integration",
                "system",
                "api_call",
                "computer_20241022",
                "text_editor_20241022",
                "bash_20241022",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolUpdateResponse:
        """
        Patch Agent Tool

        Args:
          api_call: API call definition

          computer_20241022: Anthropic new tools

          function: Function definition

          integration: Brave integration definition

          system: System definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._patch(
            f"/agents/{agent_id}/tools/{tool_id}",
            body=await async_maybe_transform(
                {
                    "api_call": api_call,
                    "bash_20241022": bash_20241022,
                    "computer_20241022": computer_20241022,
                    "description": description,
                    "function": function,
                    "integration": integration,
                    "name": name,
                    "system": system,
                    "text_editor_20241022": text_editor_20241022,
                    "type": type,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolUpdateResponse,
        )

    def list(
        self,
        agent_id: str,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ToolListResponse, AsyncOffsetPagination[ToolListResponse]]:
        """
        List Agent Tools

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/agents/{agent_id}/tools",
            page=AsyncOffsetPagination[ToolListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            model=ToolListResponse,
        )

    async def delete(
        self,
        tool_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolDeleteResponse:
        """
        Delete Agent Tool

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._delete(
            f"/agents/{agent_id}/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolDeleteResponse,
        )

    async def reset(
        self,
        tool_id: str,
        *,
        agent_id: str,
        name: str,
        type: Literal[
            "function",
            "integration",
            "system",
            "api_call",
            "computer_20241022",
            "text_editor_20241022",
            "bash_20241022",
        ],
        api_call: Optional[tool_reset_params.APICall] | Omit = omit,
        bash_20241022: Optional[Bash20241022Def] | Omit = omit,
        computer_20241022: Optional[Computer20241022Def] | Omit = omit,
        description: Optional[str] | Omit = omit,
        function: Optional[FunctionDef] | Omit = omit,
        integration: Optional[tool_reset_params.Integration] | Omit = omit,
        system: Optional[SystemDef] | Omit = omit,
        text_editor_20241022: Optional[TextEditor20241022Def] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolResetResponse:
        """
        Update Agent Tool

        Args:
          api_call: API call definition

          computer_20241022: Anthropic new tools

          function: Function definition

          integration: Brave integration definition

          system: System definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._put(
            f"/agents/{agent_id}/tools/{tool_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "api_call": api_call,
                    "bash_20241022": bash_20241022,
                    "computer_20241022": computer_20241022,
                    "description": description,
                    "function": function,
                    "integration": integration,
                    "system": system,
                    "text_editor_20241022": text_editor_20241022,
                },
                tool_reset_params.ToolResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResetResponse,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_raw_response_wrapper(
            tools.create,
        )
        self.update = to_raw_response_wrapper(
            tools.update,
        )
        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.delete = to_raw_response_wrapper(
            tools.delete,
        )
        self.reset = to_raw_response_wrapper(
            tools.reset,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_raw_response_wrapper(
            tools.create,
        )
        self.update = async_to_raw_response_wrapper(
            tools.update,
        )
        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tools.delete,
        )
        self.reset = async_to_raw_response_wrapper(
            tools.reset,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_streamed_response_wrapper(
            tools.create,
        )
        self.update = to_streamed_response_wrapper(
            tools.update,
        )
        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = to_streamed_response_wrapper(
            tools.delete,
        )
        self.reset = to_streamed_response_wrapper(
            tools.reset,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_streamed_response_wrapper(
            tools.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tools.delete,
        )
        self.reset = async_to_streamed_response_wrapper(
            tools.reset,
        )
