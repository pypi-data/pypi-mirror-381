# Shared Types

```python
from julep.types import (
    AlgoliaIntegrationDef,
    AlgoliaSearchArguments,
    AlgoliaSetup,
    ArxivIntegrationDef,
    ArxivSearchArguments,
    Bash20241022Def,
    BraveIntegrationDef,
    BraveSearchArguments,
    BraveSearchSetup,
    BrowserbaseCompleteSessionArguments,
    BrowserbaseCompleteSessionIntegrationDef,
    BrowserbaseContextArguments,
    BrowserbaseContextIntegrationDef,
    BrowserbaseCreateSessionArguments,
    BrowserbaseCreateSessionIntegrationDef,
    BrowserbaseExtensionArguments,
    BrowserbaseExtensionIntegrationDef,
    BrowserbaseGetSessionArguments,
    BrowserbaseGetSessionIntegrationDef,
    BrowserbaseGetSessionLiveURLsArguments,
    BrowserbaseGetSessionLiveURLsIntegrationDef,
    BrowserbaseListSessionsArguments,
    BrowserbaseListSessionsIntegrationDef,
    BrowserbaseSetup,
    CloudinaryEditArguments,
    CloudinaryEditIntegrationDef,
    CloudinarySetup,
    CloudinaryUploadArguments,
    CloudinaryUploadIntegrationDef,
    Computer20241022Def,
    DocOwner,
    DocReference,
    DummyIntegrationDef,
    EmailArguments,
    EmailIntegrationDef,
    EmailSetup,
    FfmpegIntegrationDef,
    FfmpegSearchArguments,
    FunctionCallOption,
    FunctionDef,
    IfElseStepInput,
    IfElseStepOutput,
    LlamaParseFetchArguments,
    LlamaParseIntegrationDef,
    LlamaParseSetup,
    MailgunIntegrationDef,
    MailgunSendEmailArguments,
    MailgunSetup,
    NamedToolChoice,
    PromptStepInput,
    RemoteBrowserArguments,
    RemoteBrowserIntegrationDef,
    RemoteBrowserSetup,
    SecretRef,
    SpiderFetchArguments,
    SpiderIntegrationDef,
    SpiderSetup,
    SystemDef,
    TextEditor20241022Def,
    UnstructuredIntegrationDef,
    UnstructuredPartitionArguments,
    UnstructuredSetup,
    WeatherGetArguments,
    WeatherIntegrationDef,
    WeatherSetup,
    WikipediaIntegrationDef,
    WikipediaSearchArguments,
)
```

# Agents

Types:

```python
from julep.types import Agent, AgentDeleteResponse, AgentListModelsResponse
```

Methods:

- <code title="post /agents">client.agents.<a href="./src/julep/resources/agents/agents.py">create</a>(\*\*<a href="src/julep/types/agent_create_params.py">params</a>) -> <a href="./src/julep/types/agent.py">Agent</a></code>
- <code title="patch /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/julep/types/agent_update_params.py">params</a>) -> <a href="./src/julep/types/agent.py">Agent</a></code>
- <code title="get /agents">client.agents.<a href="./src/julep/resources/agents/agents.py">list</a>(\*\*<a href="src/julep/types/agent_list_params.py">params</a>) -> <a href="./src/julep/types/agent.py">SyncOffsetPagination[Agent]</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/julep/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="post /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">create_or_update</a>(agent_id, \*\*<a href="src/julep/types/agent_create_or_update_params.py">params</a>) -> <a href="./src/julep/types/agent.py">Agent</a></code>
- <code title="get /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">get</a>(agent_id) -> <a href="./src/julep/types/agent.py">Agent</a></code>
- <code title="get /agents/models">client.agents.<a href="./src/julep/resources/agents/agents.py">list_models</a>() -> <a href="./src/julep/types/agent_list_models_response.py">AgentListModelsResponse</a></code>
- <code title="put /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">reset</a>(agent_id, \*\*<a href="src/julep/types/agent_reset_params.py">params</a>) -> <a href="./src/julep/types/agent.py">Agent</a></code>

## Tools

Types:

```python
from julep.types.agents import (
    BrowserbaseSetupUpdate,
    ToolCreateResponse,
    ToolUpdateResponse,
    ToolListResponse,
    ToolDeleteResponse,
    ToolResetResponse,
)
```

Methods:

- <code title="post /agents/{agent_id}/tools">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/tool_create_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_create_response.py">ToolCreateResponse</a></code>
- <code title="patch /agents/{agent_id}/tools/{tool_id}">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">update</a>(tool_id, \*, agent_id, \*\*<a href="src/julep/types/agents/tool_update_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_update_response.py">ToolUpdateResponse</a></code>
- <code title="get /agents/{agent_id}/tools">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/tool_list_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_list_response.py">SyncOffsetPagination[ToolListResponse]</a></code>
- <code title="delete /agents/{agent_id}/tools/{tool_id}">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">delete</a>(tool_id, \*, agent_id) -> <a href="./src/julep/types/agents/tool_delete_response.py">ToolDeleteResponse</a></code>
- <code title="put /agents/{agent_id}/tools/{tool_id}">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">reset</a>(tool_id, \*, agent_id, \*\*<a href="src/julep/types/agents/tool_reset_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_reset_response.py">ToolResetResponse</a></code>

## Docs

Types:

```python
from julep.types.agents import DocDeleteResponse, DocBulkDeleteResponse, DocSearchResponse
```

Methods:

- <code title="post /agents/{agent_id}/docs">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_create_params.py">params</a>) -> <a href="./src/julep/types/doc.py">Doc</a></code>
- <code title="get /agents/{agent_id}/docs">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_list_params.py">params</a>) -> <a href="./src/julep/types/doc.py">SyncOffsetPagination[Doc]</a></code>
- <code title="delete /agents/{agent_id}/docs/{doc_id}">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">delete</a>(doc_id, \*, agent_id) -> <a href="./src/julep/types/agents/doc_delete_response.py">DocDeleteResponse</a></code>
- <code title="delete /agents/{agent_id}/docs">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">bulk_delete</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_bulk_delete_params.py">params</a>) -> <a href="./src/julep/types/agents/doc_bulk_delete_response.py">DocBulkDeleteResponse</a></code>
- <code title="post /agents/{agent_id}/search">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">search</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_search_params.py">params</a>) -> <a href="./src/julep/types/agents/doc_search_response.py">DocSearchResponse</a></code>

# Files

Types:

```python
from julep.types import File, FileListResponse, FileDeleteResponse
```

Methods:

- <code title="post /files">client.files.<a href="./src/julep/resources/files.py">create</a>(\*\*<a href="src/julep/types/file_create_params.py">params</a>) -> <a href="./src/julep/types/file.py">File</a></code>
- <code title="get /files">client.files.<a href="./src/julep/resources/files.py">list</a>() -> <a href="./src/julep/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/julep/resources/files.py">delete</a>(file_id) -> <a href="./src/julep/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /files/{file_id}">client.files.<a href="./src/julep/resources/files.py">get</a>(file_id) -> <a href="./src/julep/types/file.py">File</a></code>

# Sessions

Types:

```python
from julep.types import (
    BaseTokenLogProb,
    ChatInput,
    ChatResponse,
    ChosenBash20241022,
    ChosenComputer20241022,
    ChosenFunctionCall,
    ChosenTextEditor20241022,
    Entry,
    History,
    HybridDocSearch,
    LogProbResponse,
    SchemaCompletionResponseFormat,
    Session,
    SimpleCompletionResponseFormat,
    TextOnlyDocSearch,
    TokenLogProb,
    VectorDocSearch,
    SessionDeleteResponse,
    SessionChatResponse,
    SessionRenderResponse,
)
```

Methods:

- <code title="post /sessions">client.sessions.<a href="./src/julep/resources/sessions.py">create</a>(\*\*<a href="src/julep/types/session_create_params.py">params</a>) -> <a href="./src/julep/types/session.py">Session</a></code>
- <code title="patch /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">update</a>(session_id, \*\*<a href="src/julep/types/session_update_params.py">params</a>) -> <a href="./src/julep/types/session.py">Session</a></code>
- <code title="get /sessions">client.sessions.<a href="./src/julep/resources/sessions.py">list</a>(\*\*<a href="src/julep/types/session_list_params.py">params</a>) -> <a href="./src/julep/types/session.py">SyncOffsetPagination[Session]</a></code>
- <code title="delete /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">delete</a>(session_id) -> <a href="./src/julep/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /sessions/{session_id}/chat">client.sessions.<a href="./src/julep/resources/sessions.py">chat</a>(session_id, \*\*<a href="src/julep/types/session_chat_params.py">params</a>) -> <a href="./src/julep/types/session_chat_response.py">SessionChatResponse</a></code>
- <code title="post /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">create_or_update</a>(session_id, \*\*<a href="src/julep/types/session_create_or_update_params.py">params</a>) -> <a href="./src/julep/types/session.py">Session</a></code>
- <code title="get /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">get</a>(session_id) -> <a href="./src/julep/types/session.py">Session</a></code>
- <code title="get /sessions/{session_id}/history">client.sessions.<a href="./src/julep/resources/sessions.py">history</a>(session_id) -> <a href="./src/julep/types/history.py">History</a></code>
- <code title="post /sessions/{session_id}/render">client.sessions.<a href="./src/julep/resources/sessions.py">render</a>(session_id, \*\*<a href="src/julep/types/session_render_params.py">params</a>) -> <a href="./src/julep/types/session_render_response.py">SessionRenderResponse</a></code>
- <code title="put /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">reset</a>(session_id, \*\*<a href="src/julep/types/session_reset_params.py">params</a>) -> <a href="./src/julep/types/session.py">Session</a></code>

# Users

Types:

```python
from julep.types import User, UserDeleteResponse
```

Methods:

- <code title="post /users">client.users.<a href="./src/julep/resources/users/users.py">create</a>(\*\*<a href="src/julep/types/user_create_params.py">params</a>) -> <a href="./src/julep/types/user.py">User</a></code>
- <code title="patch /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">update</a>(user_id, \*\*<a href="src/julep/types/user_update_params.py">params</a>) -> <a href="./src/julep/types/user.py">User</a></code>
- <code title="get /users">client.users.<a href="./src/julep/resources/users/users.py">list</a>(\*\*<a href="src/julep/types/user_list_params.py">params</a>) -> <a href="./src/julep/types/user.py">SyncOffsetPagination[User]</a></code>
- <code title="delete /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">delete</a>(user_id) -> <a href="./src/julep/types/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="post /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">create_or_update</a>(user_id, \*\*<a href="src/julep/types/user_create_or_update_params.py">params</a>) -> <a href="./src/julep/types/user.py">User</a></code>
- <code title="get /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">get</a>(user_id) -> <a href="./src/julep/types/user.py">User</a></code>
- <code title="put /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">reset</a>(user_id, \*\*<a href="src/julep/types/user_reset_params.py">params</a>) -> <a href="./src/julep/types/user.py">User</a></code>

## Docs

Types:

```python
from julep.types.users import DocDeleteResponse, DocBulkDeleteResponse, DocSearchResponse
```

Methods:

- <code title="post /users/{user_id}/docs">client.users.docs.<a href="./src/julep/resources/users/docs.py">create</a>(user_id, \*\*<a href="src/julep/types/users/doc_create_params.py">params</a>) -> <a href="./src/julep/types/doc.py">Doc</a></code>
- <code title="get /users/{user_id}/docs">client.users.docs.<a href="./src/julep/resources/users/docs.py">list</a>(user_id, \*\*<a href="src/julep/types/users/doc_list_params.py">params</a>) -> <a href="./src/julep/types/doc.py">SyncOffsetPagination[Doc]</a></code>
- <code title="delete /users/{user_id}/docs/{doc_id}">client.users.docs.<a href="./src/julep/resources/users/docs.py">delete</a>(doc_id, \*, user_id) -> <a href="./src/julep/types/users/doc_delete_response.py">DocDeleteResponse</a></code>
- <code title="delete /users/{user_id}/docs">client.users.docs.<a href="./src/julep/resources/users/docs.py">bulk_delete</a>(user_id, \*\*<a href="src/julep/types/users/doc_bulk_delete_params.py">params</a>) -> <a href="./src/julep/types/users/doc_bulk_delete_response.py">DocBulkDeleteResponse</a></code>
- <code title="post /users/{user_id}/search">client.users.docs.<a href="./src/julep/resources/users/docs.py">search</a>(user_id, \*\*<a href="src/julep/types/users/doc_search_params.py">params</a>) -> <a href="./src/julep/types/users/doc_search_response.py">DocSearchResponse</a></code>

# Jobs

Types:

```python
from julep.types import JobStatus
```

Methods:

- <code title="get /jobs/{job_id}">client.jobs.<a href="./src/julep/resources/jobs.py">get</a>(job_id) -> <a href="./src/julep/types/job_status.py">JobStatus</a></code>

# Docs

Types:

```python
from julep.types import Doc, EmbedQueryResponse, Snippet
```

Methods:

- <code title="post /embed">client.docs.<a href="./src/julep/resources/docs.py">embed</a>(\*\*<a href="src/julep/types/doc_embed_params.py">params</a>) -> <a href="./src/julep/types/embed_query_response.py">EmbedQueryResponse</a></code>
- <code title="get /docs/{doc_id}">client.docs.<a href="./src/julep/resources/docs.py">get</a>(doc_id, \*\*<a href="src/julep/types/doc_get_params.py">params</a>) -> <a href="./src/julep/types/doc.py">Doc</a></code>

# Tasks

Types:

```python
from julep.types import (
    CaseThenOutput,
    ErrorWorkflowStep,
    EvaluateStep,
    ForeachDoOutput,
    ForeachStepOutput,
    GetStep,
    LogStep,
    ParallelStepOutput,
    PromptStepOutput,
    ReturnStep,
    SetStep,
    SleepFor,
    SleepStep,
    SwitchStepOutput,
    Task,
    ToolCallStep,
    WaitForInputInfo,
    WaitForInputStep,
    YieldStep,
)
```

Methods:

- <code title="post /agents/{agent_id}/tasks">client.tasks.<a href="./src/julep/resources/tasks.py">create</a>(agent_id, \*\*<a href="src/julep/types/task_create_params.py">params</a>) -> <a href="./src/julep/types/task.py">Task</a></code>
- <code title="get /agents/{agent_id}/tasks">client.tasks.<a href="./src/julep/resources/tasks.py">list</a>(agent_id, \*\*<a href="src/julep/types/task_list_params.py">params</a>) -> <a href="./src/julep/types/task.py">SyncOffsetPagination[Task]</a></code>
- <code title="post /agents/{agent_id}/tasks/{task_id}">client.tasks.<a href="./src/julep/resources/tasks.py">create_or_update</a>(task_id, \*, agent_id, \*\*<a href="src/julep/types/task_create_or_update_params.py">params</a>) -> <a href="./src/julep/types/task.py">Task</a></code>
- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/julep/resources/tasks.py">get</a>(task_id) -> <a href="./src/julep/types/task.py">Task</a></code>

# Executions

Types:

```python
from julep.types import Execution, Transition
```

Methods:

- <code title="post /tasks/{task_id}/executions">client.executions.<a href="./src/julep/resources/executions/executions.py">create</a>(task_id, \*\*<a href="src/julep/types/execution_create_params.py">params</a>) -> <a href="./src/julep/types/execution.py">Execution</a></code>
- <code title="get /tasks/{task_id}/executions">client.executions.<a href="./src/julep/resources/executions/executions.py">list</a>(task_id, \*\*<a href="src/julep/types/execution_list_params.py">params</a>) -> <a href="./src/julep/types/execution.py">SyncOffsetPagination[Execution]</a></code>
- <code title="put /executions/{execution_id}">client.executions.<a href="./src/julep/resources/executions/executions.py">change_status</a>(execution_id, \*\*<a href="src/julep/types/execution_change_status_params.py">params</a>) -> object</code>
- <code title="get /executions/{execution_id}">client.executions.<a href="./src/julep/resources/executions/executions.py">get</a>(execution_id) -> <a href="./src/julep/types/execution.py">Execution</a></code>

## Transitions

Methods:

- <code title="get /executions/{execution_id}/transitions/{transition_id}">client.executions.transitions.<a href="./src/julep/resources/executions/transitions.py">retrieve</a>(transition_id, \*, execution_id) -> <a href="./src/julep/types/transition.py">Transition</a></code>
- <code title="get /executions/{execution_id}/transitions">client.executions.transitions.<a href="./src/julep/resources/executions/transitions.py">list</a>(execution_id, \*\*<a href="src/julep/types/executions/transition_list_params.py">params</a>) -> <a href="./src/julep/types/transition.py">SyncOffsetPagination[Transition]</a></code>
- <code title="get /executions/{execution_id}/transitions.stream">client.executions.transitions.<a href="./src/julep/resources/executions/transitions.py">stream</a>(execution_id, \*\*<a href="src/julep/types/executions/transition_stream_params.py">params</a>) -> object</code>

## Status

Methods:

- <code title="get /executions/{execution_id}">client.executions.status.<a href="./src/julep/resources/executions/status.py">get</a>(execution_id) -> <a href="./src/julep/types/execution.py">Execution</a></code>
- <code title="get /executions/{execution_id}/status.stream">client.executions.status.<a href="./src/julep/resources/executions/status.py">stream</a>(execution_id) -> None</code>

# Secrets

Types:

```python
from julep.types import Secret, SecretListResponse, SecretDeleteResponse
```

Methods:

- <code title="post /secrets">client.secrets.<a href="./src/julep/resources/secrets.py">create</a>(\*\*<a href="src/julep/types/secret_create_params.py">params</a>) -> <a href="./src/julep/types/secret.py">Secret</a></code>
- <code title="put /secrets/{secret_id}">client.secrets.<a href="./src/julep/resources/secrets.py">update</a>(secret_id, \*\*<a href="src/julep/types/secret_update_params.py">params</a>) -> <a href="./src/julep/types/secret.py">Secret</a></code>
- <code title="get /secrets">client.secrets.<a href="./src/julep/resources/secrets.py">list</a>(\*\*<a href="src/julep/types/secret_list_params.py">params</a>) -> <a href="./src/julep/types/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /secrets/{secret_id}">client.secrets.<a href="./src/julep/resources/secrets.py">delete</a>(secret_id) -> <a href="./src/julep/types/secret_delete_response.py">SecretDeleteResponse</a></code>

# Projects

Types:

```python
from julep.types import ProjectCreateResponse, ProjectListResponse
```

Methods:

- <code title="post /projects">client.projects.<a href="./src/julep/resources/projects.py">create</a>(\*\*<a href="src/julep/types/project_create_params.py">params</a>) -> <a href="./src/julep/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /projects">client.projects.<a href="./src/julep/resources/projects.py">list</a>(\*\*<a href="src/julep/types/project_list_params.py">params</a>) -> <a href="./src/julep/types/project_list_response.py">SyncOffsetPagination[ProjectListResponse]</a></code>

# Healthz

Methods:

- <code title="get /healthz">client.healthz.<a href="./src/julep/resources/healthz.py">check</a>() -> object</code>
