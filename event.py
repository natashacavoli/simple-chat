"""."""
import json


class Event():
    """."""

    def __init__(self):
        """."""
        self._time = ""
        self._message = ""

    @property
    def message(self):
        """."""
        return self._message

    @message.setter
    def message(self, value):
        """."""
        self._message = value

    @property
    def time(self):
        """."""
        return self._time

    @time.setter
    def time(self, value):
        """."""
        self._time = value

    def get_event(self):
        """."""
        data = {
            "type": "json",
            "time": self.time,
            "message": self.message
        }

        return json.dumps(data)
