# PR Review - Infrastructure drift detector (by Deepak)

## Reviewer: Nisha Gupta
---

**Overall:** Good foundation but critical bugs need fixing before merge.

### `driftDetector.py`

> **Bug #1:** Deep comparison of nested config treats order-sensitive arrays as unordered and misses ordering drift
> This is the higher priority fix. Check the logic carefully and compare against the design doc.

### `stateComparator.py`

> **Bug #2:** Drift report marks added resources as removed and removed as added because labels are swapped
> This is more subtle but will cause issues in production. Make sure to add a test case for this.

---

**Deepak**
> Acknowledged. I have documented the issues for whoever picks this up.
