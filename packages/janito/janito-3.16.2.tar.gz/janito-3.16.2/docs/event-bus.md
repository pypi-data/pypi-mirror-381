# Event Bus System Documentation

## Overview
The event bus is a central mechanism for publish/subscribe (pub/sub) communication in the system. It enables decoupled components to communicate by publishing and subscribing to events of various types.

- **Location:** `janito/event_bus/bus.py`
- **Singleton Instance:** `event_bus`

## Event Architecture
- **Events** are Python dataclasses (see `janito/event_types.py`) that represent occurrences or state changes in the system.
- **Event Types** are defined as subclasses of the base `Event` class (now located in `janito/event_bus/event.py`).
- **Subscribers** are functions or objects that listen for specific event types.

## Defining Events
1. **Base Event Class:**
   - Located at `janito/event_bus/event.py`:
     ```python
     from dataclasses import dataclass
     from typing import ClassVar
     @dataclass
     class Event:
         category: ClassVar[str] = "generic"
     ```
2. **Custom Event Types:**
   - Define new events by subclassing `Event` or its descendants in `janito/event_types.py`.
   - Example:
     ```python
     @dataclass
     class RequestStarted(DriverEvent):
class RequestFinished(DriverEvent):
         payload: Any
         # ...
     ```

## Subscribing to Events
To listen for events, subscribe a callback to an event type:
```python
from janito.event_bus.bus import event_bus
from janito.driver_events import RequestStarted, RequestFinished

def on_request_started(event):
    print(f"Request started: {event}")

event_bus.subscribe(RequestStarted, on_request_started)
event_bus.subscribe(RequestFinished, on_request_finished)
```

## Unsubscribing from Events
To stop listening:
```python
event_bus.unsubscribe(RequestStarted, on_request_started)
event_bus.unsubscribe(RequestFinished, on_request_finished)
```

## Publishing Events
To notify subscribers of an event:
```python
from janito.driver_events import RequestStarted, RequestFinished
from janito.event_bus.bus import event_bus

my_event = RequestStarted(driver_name="driver1", request_id="abc123", payload={...})
event_bus.publish(my_event)
```

### Automatic Timestamping
- Every event published will have a `timestamp` attribute (UNIX epoch seconds) automatically set by the event bus.
- This is injected at publish time and is available to all subscribers:
  ```python
  def on_request_started(event):
      print(event.timestamp)  # Set automatically by event bus
  ```

## Example
```python
from janito.driver_events import RequestStarted, RequestFinished
from janito.event_bus.bus import event_bus

def log_event(event):
    print(f"[{event.timestamp}] Event: {event}")

event_bus.subscribe(RequestStarted, log_event)

# Later in code...
event = RequestStarted(driver_name="driver1", request_id="abc123", payload={"foo": "bar"})
event_bus.publish(event)
```

## Best Practices
- Do not manually add a `timestamp` field to event dataclasses; it is managed by the event bus.
- Use specific event types for clarity and maintainability.
- Unsubscribe handlers when they are no longer needed to avoid memory leaks.

---
For more details, see the source code in `janito/event_bus/bus.py` and `janito/event_types.py`.
