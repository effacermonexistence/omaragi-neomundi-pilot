# Pilot 01 — NeoMundi synthetic signals to REVAS admissibility artifacts

Pilot 01 is an early interoperability pilot showing how synthetic NeoMundi runtime observability inputs can be mapped into OmarAGI / REVAS pre-action admissibility artifacts.

## Signal flow

```text
NeoMundi synthetic input sample
→ OmarAGI / REVAS processing
→ sanitized REVAS pre-action admissibility artifact
→ Pilot 01 readout
```

## Input type

The public inputs are synthetic NeoMundi observation examples describing AI behavior signals such as stability, coherence, factual fragility, semantic variability, risk level, and measurement coverage.

They live in `source-samples/` and are explicitly labeled as synthetic public examples. They are not production records, ControlTower exports, customer records, private logs, or certification evidence.

## Output type

The outputs are sanitized OmarAGI REVAS scored artifacts in `artifacts/`. Each artifact maps one NeoMundi synthetic signal into a conservative REVAS pre-action admissibility decision.

## Five mapped cases

1. stable but fragile
2. variable and uncertain
3. supported but limited
4. contradiction or overclaim
5. partial measurement

## Goal

The goal is to convert runtime observability signals into pre-action admissibility decisions while preserving uncertainty, measurement boundaries, route structure, and fallback safety.

This pilot does not claim final truth, safety, legal authority, execution admissibility, production readiness, official partnership, customer status, third-party validation, or benchmark proof.
