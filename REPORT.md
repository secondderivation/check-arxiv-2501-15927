# Observational implications of Wald-Gauss-Bonnet topological dark energy

[2501.15927v3](https://arxiv.org/abs/2501.15927v3) · Review 0.1.0-rc2

**Confirmed finding.** The author confirmed the denominator coefficient error in Eq. (19) and its public CLASS implementation.

**Limit:** Confirmation covers this local coefficient error; effects on cosmological inference and the complete corrected implementation remain unverified.

Confirmation basis: author\_confirmed.

## Checked scope

- The author confirmed the denominator coefficient error in Eq. (19) and its public CLASS implementation.

Not checked: Confirmation covers this local coefficient error; effects on cosmological inference and the complete corrected implementation remain unverified.

## Review record

| Claim | Method | Outcome / adequacy | Evidence |
|---|---|---|---|
| F1: Eq. (19) and public implementation — Confirmed denominator coefficient error in Eq. (19) and the public CLASS implementation: -6 must become +24 in the code integral convention (equivalently +6 becomes -24 in the redshift-integral convention). | source\_check | held:discrepancy / pass | [EVIDENCE.md](EVIDENCE.md), [DERIVATION.md](DERIVATION.md), [inputs/grid.json](inputs/grid.json), [reference/raw-stdlib-checks.json](reference/raw-stdlib-checks.json), [reference/stdlib-summary.json](reference/stdlib-summary.json) |

[Protocol and provenance](PROTOCOL.md). This review record is retrospective.

## Review provenance

Prepared with AI assistance. Historical Claude first pass and Codex independent review/critique remain distinct; this assembly reads saved evidence and is neither blind B nor new P2. No scientific code was run in this assembly. The later informed correction audit disclosed prewritten but uncommitted convention/grid amendments before its diagnostic run; this G2 deviation remains historical. Author confirmation is limited to the named coefficient error.

Tools: Claude (historical A); Codex (historical B/C and current informed assembly). Human involvement: Owner selected the preparation scope and approved the predecessor release published on 10 November 2026; the owner approved publication of this editorial revision on 11 November 2026.

## Replay

~~~sh
python3 replay.py --output replay-new
~~~

Original diagnostic cap: 60 seconds; wrapper timeout: 65 seconds. Python standard library only.. Fixed sixteen-point local denominator/derivative/integral diagnostic and comparison with immutable saved reference. Retains documented interpolation failures; no observational inference or CLASS replay.
