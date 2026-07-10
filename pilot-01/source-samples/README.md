# NeoMundi synthetic public input samples

This folder contains a small set of **synthetic public examples** used to illustrate the Pilot 01 signal flow:

```text
NeoMundi synthetic runtime observability signal
→ OmarAGI / REVAS processing
→ sanitized REVAS pre-action admissibility artifact
→ Pilot 01 readout
```

These files are included only to make the public repository easier to inspect. They are not production records, customer records, ControlTower exports, provider logs, benchmark proof, certification material, or third-party validation.

## Redaction boundary

The public samples intentionally omit raw prompts, raw model outputs, timestamps, private URLs, account identifiers, emails, keys, tokens, operational traces, internal metadata, and any proprietary or sensitive fields not needed to show the signal flow.

Each sample maps to a corresponding sanitized REVAS artifact in `../artifacts/` through its `maps_to_revas_artifact` field.

## Included cases

1. `neomundi_synthetic_public_input_01_stable_but_fragile.json`
2. `neomundi_synthetic_public_input_02_variable_and_uncertain.json`
3. `neomundi_synthetic_public_input_03_supported_but_limited.json`
4. `neomundi_synthetic_public_input_04_contradiction_or_overclaim.json`
5. `neomundi_synthetic_public_input_05_partial_measurement.json`
