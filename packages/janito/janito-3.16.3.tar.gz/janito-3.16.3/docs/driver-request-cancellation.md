# Driver Request Cancellation in Janito

## Overview

Driver request cancellation refers to the ability to halt or abort an in-progress request to an LLM driver (such as OpenAI, Anthropic, etc.) before it completes. This is important for responsive user interfaces, resource management, and handling user-initiated aborts (e.g., pressing Ctrl+C in the CLI).

## Current Handling

Janito's core driver flow is event-driven and supports cooperative, programmatic cancellation of in-progress requests using a `threading.Event` (commonly named `cancel_event`). This event is passed through the agent and driver layers and can be set by the consumer to signal that the current request should be aborted as soon as possible.

### How Cooperative Cancellation Works

- A `threading.Event` object is created and passed as `cancel_event` to the agent or driver interface (e.g., `agent.chat(..., cancel_event=cancel_event)`).
- Drivers and agents check the state of `cancel_event` at key points during request processing (before starting, after API calls, and during long-running operations).
- If `cancel_event.is_set()` returns True, the driver should abort further processing, avoid sending new requests, and clean up resources promptly.
- This allows both user-initiated (e.g., Ctrl+C) and programmatic cancellation (e.g., from a UI button or another thread).

### User-Initiated Cancellation

- In CLI mode, users may interrupt a request using standard terminal signals (e.g., Ctrl+C). The Python runtime will raise a `KeyboardInterrupt`, which is handled by the CLI session loop to stop further processing and clean up.
- The agent logic will set the `cancel_event` in response to user interruption, ensuring downstream drivers respond promptly.

### Agent/Tool-Initiated Cancellation

- Agents, tools, or external consumers can programmatically set the `cancel_event` to abort an in-progress request.
- This enables responsive UIs and advanced workflows where cancellation may be triggered by logic other than user interruption.

## Implementation Details

- The `cancel_event` is an optional field in the `DriverInput` dataclass (see `janito/llm/driver_input.py`).
- Drivers are expected to check for cancellation at the start of processing and after any blocking or long-running operation (see `janito/llm/driver.py` and driver subclasses).
- Example usage and code references are available in `docs/llm-drivers.md`.

## Future Directions

- **Streaming APIs:** For drivers that support streaming, partial results may be available up to the point of cancellation.
- **Graceful Cleanup:** Continued improvements to resource management and cleanup on cancellation are planned.

## Affected Flows When Cancellation is Performed at the Agent Level

When a cancellation is triggered at the agent level (e.g., by setting the `cancel_event` or via user interruption such as Ctrl+C), the following flows are affected:

1. **Agent Main Loop (`chat` method)**: The main conversation loop passes the `cancel_event` to the driver and monitors for user interruptions. If a cancellation is detected, it stops further processing and signals downstream components.
2. **Event Processing (`_process_next_response`)**: This method waits for events from the driver. On user interruption, it creates a `RequestFinished` event with status `cancelled` and puts it in the input queue, propagating cancellation.
3. **Driver Input Preparation (`_prepare_driver_input`)**: The `cancel_event` is attached to the `DriverInput` object, ensuring it is available to the driver for cooperative cancellation.
4. **Driver Processing (`process_driver_input` in `LLMDriver` and subclasses)**:
   - Before starting, the driver checks if `cancel_event` is set and aborts if so.
   - After API calls (and during long-running operations in subclasses), the driver checks `cancel_event` again and aborts if set.
   - If cancellation is detected, a `RequestFinished` event with status `cancelled` is emitted to the output queue.
5. **Tool/Function Execution (within `_handle_response_received`)**: If tool calls are in progress, cancellation may prevent further tool execution or message handling, depending on when the event is set.

This cooperative cancellation mechanism ensures that all major flows—agent loop, driver processing, and tool execution—respond promptly to cancellation requests, providing a responsive and robust user experience.

## Recommendations

- Use the `cancel_event` mechanism for both user-initiated and programmatic cancellation.
- For UI or API integrations, expose a way to set the `cancel_event` to allow users or logic to abort requests.
- For more details, see `docs/llm-drivers.md` and the relevant code in `janito/llm/agent.py`, `janito/llm/driver.py`, and driver implementations.

## References

- See `docs/llm-drivers.md` for architecture and example usage.
- See CLI session handling for interruption logic.
- See `janito/llm/driver_input.py`, `janito/llm/agent.py`, and driver implementations for code-level details.
