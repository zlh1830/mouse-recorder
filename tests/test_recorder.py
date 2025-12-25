import json
from mouse_recorder.recorder import MouseRecorder


def test_save(tmp_path):
    mr = MouseRecorder()
    mr.events = [{"type": "move", "time": 0, "x": 0, "y": 0}]
    p = tmp_path / "out.json"
    mr.save(str(p))
    assert p.exists()
    data = json.loads(p.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert data[0]["type"] == "move"
