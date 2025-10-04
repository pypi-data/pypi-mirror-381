# Message Handler Model

This document describes the message handler model used in Janito for both CLI and web output. For details on the styled terminal output, see the [Rich Message Handler](rich-message-handler.md). The model ensures that all output—whether from tools or from assistant/LLM content—is routed through a single, consistent API, simplifying both backend and frontend logic.

## Overview

- **Single handler** for all output: tools, assistant, or system messages.
- **Consistent message format**: every message is sent with a message string and a message type.
- **Easy to extend**: add new message types or styles as needed.

## Message Format

A message is always represented as:

- **message**: The text to display (string)
- **msg_type**: The type/category of the message (string)

For queue/web integration, each message is sent as a tuple:

```
('message', message, msg_type)
```

### Common `msg_type` Values
- `info`: Informational or neutral messages (default)
- `success`: Successful operations (e.g., file created)
- `error`: Errors or failures
- `content`: Assistant/LLM responses or natural language content
- (You can add more types as needed)

## Handler API

### Python (Backend)

```python
handler.handle_message(msg, msg_type=None)
```
- `msg`: Either a string (content) or a dict with `{"type": ..., "message": ...}` (tool progress)
- `msg_type`: Optional; used if `msg` is a string

#### Example Usage
```python
# Tool output
handler.handle_message({"type": "success", "message": "✅ File created"})

# Assistant/content output
handler.handle_message("Here is your summary...", msg_type="content")
```

### Web Queue Integration

- All output is sent to the frontend as:
  - `('message', message, msg_type)`
- The frontend displays the message with styling based on `msg_type`.

## Frontend Handling

- Render all messages using a single handler/component.
- Style by `msg_type` (e.g., green for `success`, red for `error`, etc).
- No need to distinguish tool/content at the backend—just use `msg_type`.

## Benefits
- **Consistent**: Same styling and logic everywhere.
- **Extensible**: Add more message types or custom styles easily.
- **Simple**: Less boilerplate, easier to maintain.

---

This model applies to both CLI and web output, making the Janito user experience clean, predictable, and easy to evolve.
