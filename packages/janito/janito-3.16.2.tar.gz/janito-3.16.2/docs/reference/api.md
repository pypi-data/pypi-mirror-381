# API Reference

Welcome to the API reference for this project. This document provides an overview of the main classes and their locations within the codebase. Use this as a starting point for understanding and extending the core functionality.

---

## Core Modules and Main Classes

### janito.agent.config

- **SingletonMeta**: Metaclass for singleton pattern.
- **BaseConfig**: Base configuration class.
- **FileConfig**: File-based configuration.
- **EffectiveConfig**: Represents the effective configuration.

### janito.agent.conversation

- **ConversationHandler**: Manages conversation state and flow.
    - `__init__`: Initializes the handler with configuration and state.
    - `handle_conversation`: Processes a conversation turn and updates state.
    - `api_call`: Makes a direct API call for conversation handling.

### janito.agent.conversation_exceptions

- **MaxRoundsExceededError**: Raised when conversation round limit is exceeded.
- **EmptyResponseError**: Raised when no response is generated.
- **ProviderError**: Raised for provider-specific errors.

### janito.agent.message_handler

- **QueueMessageHandler**: Handles message queuing.

### janito.agent.openai_client

- **Agent**: Main agent class for OpenAI integration.
    - `__init__`: Initializes the agent with model and API settings.
    - `chat`: Sends a list of messages to the LLM and returns the response.
    - `usage_history`: Tracks and returns usage statistics.

### janito.agent.profile_manager

- **AgentProfileManager**: Manages agent profiles and prompt templates (currently only the "base" profile is supported).
    - `__init__`: Loads and initializes profile data.
    - `set_role`: Sets the current agent role.
    - `render_prompt`: Renders the prompt template for the agent.
    - `refresh_prompt`: Reloads and refreshes the prompt template.

### janito.agent.queued_message_handler

- **QueuedMessageHandler**: Handles queued messages.

### janito.agent.rich_live

- **LiveMarkdownDisplay**: Displays live markdown output.

### janito.agent.rich_message_handler

- **RichMessageHandler**: Handles rich message formatting.

### janito.agent.runtime_config

- **RuntimeConfig**: Runtime configuration derived from BaseConfig.
- **UnifiedConfig**: Unified configuration interface.

### janito.agent.tool_base

- **ToolBase**: Abstract base class for all tools.

---

## Tool Implementations (janito.agent.tools)

Each tool inherits from `ToolBase` and implements a specific function:

- **AskUserTool**
- **CreateDirectoryTool**
- **CreateFileTool**
- **FetchUrlTool**
- **FindFilesTool**
- **GetFileOutlineTool**
- **ViewFileTool**
- **StoreMemoryTool**
- **RetrieveMemoryTool**
- **MoveFileTool**
- **PyCompileFileTool**
- **RemoveDirectoryTool**
- **RemoveFileTool**
- **ReplaceFileTool**
- **ReplaceTextInFileTool**
- **RunBashCommandTool**
- **RunPythonCommandTool**
- **SearchFilesTool**

---

## CLI and Web Interfaces

### janito.cli

- CLI entry points and utilities for command-line usage.

---

For detailed class and method documentation, see the source code or future expanded API docs.


