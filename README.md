# OmarAGI × NeoMundi Technical Pilot

This repository contains an early interoperability pilot mapping NeoMundi synthetic runtime observability signals into OmarAGI / REVAS pre-action admissibility artifacts.

OmarAGI is the public project identity for this repository. NeoMundi is framed only as the pilot counterpart and ControlTower-side signal source for this limited technical pilot.

## Pilot path

```text
NeoMundi synthetic input sample
→ OmarAGI / REVAS processing
→ sanitized REVAS pre-action admissibility artifact
→ Pilot 01 readout
```

The artifacts in this repository should be read as governance and interoperability artifacts, not as final truth judgments.

## Architecture note

For this pilot, REVAS acts as the interface layer inside OmarAGI’s broader RCC, Recursive Collapse Constraint, routing architecture.

The working question is whether runtime observability signals can be converted into conservative pre-action admissibility decisions before any downstream claim or action.

## Repository structure

- `pilot-01/source-samples/` — synthetic public NeoMundi input examples, carefully redacted and labeled as non-production examples.
- `pilot-01/artifacts/` — sanitized OmarAGI / REVAS pre-action admissibility artifacts mapped from the synthetic samples.
- `pilot-01/readout/` — Pilot 01 readout summarizing the signal-to-decision mapping.
- `pilot-02/` — planned ControlTower live test materials; no live test result is claimed here.
- `docs/` — terminology and claim-boundary notes.
- `archive/` — intentionally empty public archive note.

## Pilot 01

Pilot 01 maps five synthetic NeoMundi runtime observability cases into REVAS pre-action admissibility artifacts:

1. stable but fragile
2. variable and uncertain
3. supported but limited
4. contradiction or overclaim
5. partial measurement

The purpose is to preserve uncertainty, measurement boundaries, route structure, required next steps, and fallback safety.

## Pilot 02

Pilot 02 is a planned ControlTower live test. It is not represented here as completed, deployed, validated, or production-ready.

## Boundary note

This repository documents an early technical pilot. It should not be read as production validation, commercial deployment, official partnership, customer relationship, certification, benchmark proof, cost-reduction proof, OpenAI approval, OpenAI endorsement, or third-party validation.

The included scores are first-pass REVAS-side routing estimates, not calibrated production metrics.

## Authorship

Initial REVAS-side mapping and repository structure were prepared under the OmarAGI public identity. NeoMundi may fork or publish separately from its side if a broader collaboration history needs to be represented.
