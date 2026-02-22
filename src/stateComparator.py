"""
State Comparator — normalizes infrastructure state for comparison.

Handles type coercion, key sorting, and format normalization.

Author: Suresh Kumar (DevOps team)
Last Modified: 2026-03-19
"""

from typing import Any, Dict, List


class StateComparator:
    """Normalizes and compares infrastructure state objects."""

    def normalize(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize a state dict for consistent comparison."""
        normalized = {}
        for key, value in sorted(state.items()):
            normalized[key] = self._normalize_value(value)
        return normalized

    def _normalize_value(self, value: Any) -> Any:
        """Recursively normalize a value."""
        if value is None:
            return None

        if isinstance(value, dict):
            return {k: self._normalize_value(v) for k, v in sorted(value.items())}

        if isinstance(value, list):
            return sorted([self._normalize_value(v) for v in value], key=str)

        if isinstance(value, bool):
            return value

        # Coerce numeric strings to numbers
        if isinstance(value, str):
            try:
                if '.' in value:
                    return float(value)
                return int(value)
            except ValueError:
                return value.lower().strip()

        return value

    def compare(self, desired: Dict[str, Any], actual: Dict[str, Any]) -> List[Dict]:
        """Compare two states after normalization."""
        norm_desired = self.normalize(desired)
        norm_actual = self.normalize(actual)

        differences = []
        all_keys = set(list(norm_desired.keys()) + list(norm_actual.keys()))

        for key in sorted(all_keys):
            d_val = norm_desired.get(key)
            a_val = norm_actual.get(key)
            if d_val != a_val:
                differences.append({
                    'field': key,
                    'desired': d_val,
                    'actual': a_val,
                })

        return differences
