# PLATFORM-2967: Investigate infrastructure drift detector giving false positives

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 29 · **Story Points:** 8
**Reporter:** Suresh Kumar (DevOps Lead) · **Assignee:** You (Intern)
**Due:** End of sprint (Friday)
**Labels:** `backend`, `python`, `infrastructure`, `devops`
**Task Type:** Code Debugging

---

## Description

The infra drift detector compares the desired state (Terraform/config) vs actual state (cloud API response). It's reporting drift on resources that haven't changed, causing alert fatigue.

**DEBUGGING task — no hint comments. You must investigate the symptoms.**

## Symptoms

- Drift report says 50 resources drifted, but manual inspection shows only 2 actual changes
- Tags like `{"env": "prod"}` reported as drifted when both desired and actual have the same value
- Array-type fields (e.g., security groups) always show as drifted even when identical
- Numeric fields like `port: 80` sometimes show drift against `port: "80"` (string vs number)

## Acceptance Criteria

- [ ] Root cause found and fixed
- [ ] False positive rate drops to near zero
- [ ] All unit tests pass
