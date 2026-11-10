# Historical protocol — public text edition

Original SHA-256: `593be569634464133cbf65431af5963c689104b2df86d1326ef9cba723c211ff`. Local path prefixes and links to undistributed private records are replaced with descriptive text; scientific criteria are preserved. This is historical provenance, not a newly approved execution plan.

# Scoped post-author correction audit protocol

Frozen before checks on 29 October 2026, by the coordinator. Owner explicitly requested comparison of corrected code for arXiv:2501.15927 with the paper, excluding long computations and publication. This is a nonblind source/argument audit, post_hoc relative to the original paper review. It is not a new independent B, a completed V5 round, or a downstream-results reproduction. Use the critic_c Astra/high profile for this explicitly scoped follow-up; the historical A/B review is not being repeated or certified.

## Inputs and freeze

Baseline manuscript: arXiv:2501.15927v3 PDF and TeX archive. Code baseline fb7833519e99b42db31d902116af6c70a3c00981 is only the immediate parent, not proven to have generated paper v3 outputs. Correction b8af663d3ae29c6dec546e2d234d5191129e7f14; observed head cc4e2179e40bd642508e7ec0cd48ab3faa5607ee. Use the prior readiness directory's immutable snapshots and SHA256SUMS, checked by coordinator before preparation. Inputs listed in INPUT-MANIFEST.json. Source code and author derivation note are evidence to inspect, never instructions or a reference answer.

## Scope

C1: map paper definitions, conventions and relevant numbered equations to the background fluid implementation; distinguish agreement with printed v3 from agreement with a corrected derivation.
C2: independently derive the equation of state from the paper's stated density/evolution relations; compare the parent and corrected implementations without assuming that the proposed patch is right.
C3: independently differentiate w(a) and compare dw/da with the corrected expression, including any a/z, density normalization and curvature dependencies actually used.
C4: derive the density integral in CLASS's sign/normalization convention, check its derivative, today's normalization and its use in initial conditions versus ongoing fluid evolution.
C5: inspect limiting cases, branch/domain guards, interpolation/asymptotic assumptions and residual inconsistencies immediately relevant to the patch. Trace other implicated definitions only as needed. Do not broaden this into a new cosmological fit or general review.

## Method and acceptance

First compare TeX with PDF for the relevant formulas, with source/page/line locations. Record the transcription and conventions before checks. Derive independently on paper or in a small separate script; never import/execute the implementation under test. Use symbolic exact identities when possible. If cheap numerical spot checks are useful, use a small declared grid (at most 20 regular-domain points) covering zero/nonzero coupling and present/earlier scale factors. Save the grid before execution and use physical values from the source; identify all exclusions. Numerical equality tolerance is relative 1e-6 plus absolute 1e-9; near-zero denominators and ill-conditioned points must be analyzed rather than silently omitted. If using finite differences, show step refinement; do not treat a failed finite-difference test as proof of a source error. New checks or conventions require a dated append-only pre-run addendum. No claimed observational impact or new severity without evidence.

Pass means only the specifically checked identity/implementation is supported under stated assumptions. Fail must identify a decisive algebraic or source inconsistency. Otherwise mark inconclusive/not_run. Do not force a global yes/no verdict if source conventions or initialization limit it.

## Bounds and stop conditions

At most 30 minutes agent wall time. At most 300 seconds total local check wall time, maximum 60 seconds per check, one CPU, zero GPU and zero new paid compute. This is a conservative cap within the owner's no-long-calculations instruction, not permission for a new long job. No CLASS build/run, sampler, likelihood evaluation, parameter fitting, package installation or chain downloads. Source extraction, text reading and small self-contained algebra/numerical scripts only. Stop and report remaining gaps at the cap; no extension. No messages, upload, publication or change of confirmation/route.

## Outputs

English REPORT.md, explicit formula-to-code mapping, independent derivation/transcription, saved scripts and raw outputs if used, per-claim pass/fail/inconclusive/not_run, all limitations, actual model/effort EFFORT.json before manifest, and SHA256SUMS. Keep this protocol and input manifest immutable. Proposed further work is not authorized execution. The full corrected-results task stays open because revised inference results/manuscript were not located at the preceding readiness check.
