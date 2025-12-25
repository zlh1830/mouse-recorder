import json
import time
import threading
from pynput import mouse


class MouseRecorder:
    """Simple mouse recorder using pynput.

    Usage:
        mr = MouseRecorder()
        mr.record_for(5)
        mr.save('events.json')
    """

    def __init__(self):
        self.events = []
        self._listener = mouse.Listener(on_move=self._on_move, on_click=self._on_click, on_scroll=self._on_scroll)

    def _on_move(self, x, y):
        self.events.append({"type": "move", "time": time.time(), "x": x, "y": y})

    def _on_click(self, x, y, button, pressed):
        self.events.append({"type": "click", "time": time.time(), "x": x, "y": y, "button": str(button), "pressed": pressed})

    def _on_scroll(self, x, y, dx, dy):
        self.events.append({"type": "scroll", "time": time.time(), "x": x, "y": y, "dx": dx, "dy": dy})

    def start(self):
        self._listener.start()

    def stop(self):
        self._listener.stop()
        self._listener.join()

    def record_for(self, seconds: int):
        """Record for a given number of seconds (blocking)."""
        self.events = []
        self.start()
        timer = threading.Timer(seconds, self.stop)
        timer.start()
        self._listener.join()
        timer.cancel()
        return self.events

    def save(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.events, f, ensure_ascii=False, indent=2)
