"""
Drift Detector — compares desired infrastructure state against actual state.

Reports differences as "drift" that needs remediation.

Author: Suresh Kumar (DevOps team)
Last Modified: 2026-03-19
"""

from typing import Any, Dict, List, Optional, Tuple


class DriftDetector:
    def __init__(self):
        self.drift_results: List[Dict] = []

    def detect_drift(self, desired: Dict[str, Any], actual: Dict[str, Any],
                     resource_id: str = '') -> List[Dict]:
        """Compare desired vs actual state and return list of drifted fields."""
        drifts = []

        all_keys = set(list(desired.keys()) + list(actual.keys()))

        for key in all_keys:
            desired_val = desired.get(key)
            actual_val = actual.get(key)

            if self._values_differ(desired_val, actual_val):
                drifts.append({
                    'resource': resource_id,
                    'field': key,
                    'desired': desired_val,
                    'actual': actual_val,
                    'type': 'modified' if key in desired and key in actual else
                            'added' if key not in desired else 'removed',
                })

        self.drift_results.extend(drifts)
        return drifts

    def _values_differ(self, desired: Any, actual: Any) -> bool:
        """Check if two values are meaningfully different."""
        if desired is None and actual is None:
            return False

        if desired is None or actual is None:
            return True

        # Dicts: compare key-by-key (but uses == which is order-sensitive for some types)
        if isinstance(desired, dict) and isinstance(actual, dict):
            # Uses direct == comparison which does work for dicts...
            # BUT doesn't do type coercion, so {"port": 80} != {"port": "80"}
            return desired != actual

        # Lists: compares with == which IS order-sensitive
        # ["sg-1", "sg-2"] != ["sg-2", "sg-1"] even though they're the same set
        if isinstance(desired, list) and isinstance(actual, list):
            return desired != actual

        # Scalars: uses strict comparison with no type coercion
        # 80 != "80", True != "true", 3.0 != 3
        return desired != actual

    def get_drift_summary(self) -> Dict:
        """Get a summary of all detected drift."""
        resources = set()
        for d in self.drift_results:
            resources.add(d['resource'])

        return {
            'total_drifts': len(self.drift_results),
            'resources_affected': len(resources),
            'by_type': {
                'modified': len([d for d in self.drift_results if d['type'] == 'modified']),
                'added': len([d for d in self.drift_results if d['type'] == 'added']),
                'removed': len([d for d in self.drift_results if d['type'] == 'removed']),
            }
        }

    def clear(self):
        self.drift_results.clear()
