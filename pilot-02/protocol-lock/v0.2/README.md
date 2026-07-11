# Pilot 02 v0.2 endpoint lock

Status: **frozen for DEV-30 design**.

This package prevents silent objective and endpoint drift. It separates:

- the public research framing: runtime intervention quality with quantified impact;
- the confirmatory study outcome: resource benefit under quality and safety constraints;
- the verifiable-track decision co-primary;
- bounded natural-language decision diagnostics, whose labels remain derived from human utility judgments.

## Authoritative files

- `pilot02_endpoint_lock.json` — machine-readable source of truth
- `PILOT02_ENDPOINT_LOCK.md` — human-readable rendering
- `CHANGE_CONTROL.md` — only valid route for later changes
- `LOCK_MANIFEST.json` — SHA-256 integrity manifest

## Verify

From the repository root:

```bash
python3 tools/verify_pilot02_lock.py
python3 -m unittest tests/test_pilot02_lock.py -v
```

Passing verification proves that the checked-out artifact matches the frozen semantic contract and recorded hashes. It does not claim that future evidence can never justify a new, explicitly versioned protocol.
SPOOF_TEST_ONLY
