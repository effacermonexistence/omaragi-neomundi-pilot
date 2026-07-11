# Pilot 02 protocol change control

## Default rule

`v0.2` is immutable. Do not edit its research object, endpoint hierarchy, track authority, action scope, H5 arms, or claim boundaries in place.

## Legitimate change route

A proposed change must:

1. identify one allowed trigger recorded in `pilot02_endpoint_lock.json`;
2. create a new version directory rather than modifying `v0.2`;
3. state the exact old and new language;
4. explain construct-validity, statistical-power, implementation, cost, and contamination effects;
5. identify whether the locked corpus has been accessed;
6. include an approval record from the protocol owners;
7. regenerate the integrity manifest and pass all tests.

If the locked corpus has been accessed, endpoint and threshold changes are prohibited for that evaluation. A later study must receive a new protocol identity.

## What is not a protocol change

DEV-30 may calibrate only the numerical items explicitly listed under `calibration_items`. Filling those preregistered fields before opening the locked corpus does not alter the endpoint ontology.

## Drift response

If a draft, message, code path, or analysis conflicts with v0.2:

1. quarantine the conflicting artifact;
2. retain v0.2 as the active authority;
3. classify the conflict as wording drift, endpoint drift, threshold drift, action-scope drift, or corpus-contamination risk;
4. use the versioned change route only if a legitimate trigger exists;
5. otherwise discard the conflicting change.
