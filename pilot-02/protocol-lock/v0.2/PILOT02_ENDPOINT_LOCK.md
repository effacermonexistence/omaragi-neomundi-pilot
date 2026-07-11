# Pilot 02 v0.2 — endpoint architecture lock

## Locked research object

Pilot 02 asks whether NeoMundi-informed REVAS can improve runtime intervention decisions while producing measurable resource benefit under predeclared quality and safety non-inferiority constraints.

The framing is decision-first. The confirmatory outcome is not decision accuracy alone and is not raw token reduction alone.

## Non-compensatory study-level outcome

The primary study result uses ordered hard gates:

1. **Quality and safety gate:** quality non-inferiority and all frozen severe-intervention thresholds must pass. Savings cannot compensate for a failed quality or safety gate.
2. **Resource and economic gate:** paired output-token benefit must meet the preregistered threshold and confidence rule, while total net cost including observation, decision, regeneration, and routing overhead must not increase.

Failure of either gate prevents a positive Pilot 02 result. A scientifically informative negative result remains reportable.

## Track-specific authority

### Verifiable-output track

Checkpoint-level decision correctness or intervention regret is co-primary only when all of the following are frozen before outputs are evaluated:

- requirement map;
- executable verifier;
- completion obligations;
- acceptable stop interval;
- checkpoint schedule;
- action oracle and failure severity.

A test pass by itself is not sufficient when the prompt also requires explanation, usability, or other uncaptured obligations.

### Bounded natural-language track

Quality non-inferiority is established by preregistered blinded human evaluation supported by fixed automated evidence. Decision confusion matrices and intervention-regret measures are confirmatory secondary mechanism metrics. They must disclose that their labels derive from the same bounded utility and sufficiency judgments used in quality evaluation; they are not an independent universal ground truth.

## Primary action lane

The primary lane is:

- `CONTINUE`
- `STOP`
- `ABSTAIN`

`REGENERATE`, `ROUTE`, and `ESCALATE` remain separate action-specific modules until their counterfactuals, costs, and success oracles are independently frozen.

## H5 incremental-value design

H5 compares identical prompts, source outputs, checkpoints, action scope, and evaluation rules across:

1. simple heuristic;
2. REVAS without NeoMundi;
3. REVAS with NeoMundi;
4. REVAS with the cheapest credible direct substitute for the useful NeoMundi signal.

NeoMundi is incrementally valuable only if its arm improves preregistered decision or outcome measures beyond both REVAS without NeoMundi and the direct substitute after added latency and cost are included.

## Freeze boundary

- DEV-30 is calibration-only and cannot establish performance.
- Numerical margins explicitly marked for calibration may be finalized using DEV-30 only.
- The locked evaluation corpus is evaluation-only and must remain unopened until policy, thresholds, cadence, action scope, evaluators, and analysis are frozen.
- v0.2 is never edited in place. A legitimate change requires a new version and change record.

## Prohibited substitutions

- raw token reduction as the sole primary endpoint;
- decision accuracy as the sole primary endpoint;
- universal-human-utility claims from a frozen bounded evaluator population;
- a positive Pilot 02 claim when quality/safety fails or net cost increases;
- treating reasoning-token scaling as evidence that visible output continuation is always useful;
- changing endpoint ontology after locked-corpus access.
