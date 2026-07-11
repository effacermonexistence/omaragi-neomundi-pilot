# Pilot 02 endpoint governance

For Pilot 02 work in this repository, the authoritative endpoint architecture is:

`pilot-02/protocol-lock/v0.2/pilot02_endpoint_lock.json`

Before editing Pilot 02 protocol, benchmark, evaluator, or claim language:

1. Run `python3 tools/verify_pilot02_lock.py`.
2. Preserve every semantic invariant in the v0.2 lock.
3. Do not silently replace the joint efficiency-under-quality/safety outcome with raw token reduction alone or decision accuracy alone.
4. Do not treat bounded natural-language decision labels as independent ground truth.
5. Do not open or tune on the locked evaluation corpus before DEV-30 calibration is complete and versioned.
6. Any legitimate architecture change requires a new version directory, a change record, review, and new hashes. Never overwrite v0.2 in place.

The lock governs endpoint architecture and claim boundaries. DEV-30 may calibrate numerical thresholds explicitly marked as calibration items; it may not redefine the research object without the versioned change process.
