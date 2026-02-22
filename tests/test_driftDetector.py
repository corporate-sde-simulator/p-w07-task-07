"""Tests for Infrastructure drift detector."""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from driftDetector import DriftDetector
from stateComparator import StateComparator

class TestMain:
    def test_basic(self):
        obj = DriftDetector()
        assert obj.process({"key": "val"}) is not None
    def test_empty(self):
        obj = DriftDetector()
        assert obj.process(None) is None
    def test_stats(self):
        obj = DriftDetector()
        obj.process({"x": 1})
        assert obj.get_stats()["processed"] == 1

class TestSupport:
    def test_basic(self):
        obj = StateComparator()
        assert obj.process({"key": "val"}) is not None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
