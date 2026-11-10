# Narrow confirmed finding and executable evidence

The author-confirmed Finding 1 is the denominator discrepancy between Eq. 19 and the result implied by Eq. 18 (also Eqs. 13 and 16) in arXiv:2501.15927v3. Public claim F1 maps to that historical Finding 1 only.

[DERIVATION.md](DERIVATION.md) gives exact locations, conventions and the local continuity derivation. [inputs/grid.json](inputs/grid.json) is the unchanged sixteen-point historical diagnostic grid; printed negative coupling is a diagnostic example, not a new fit. [check-stdlib.py](check-stdlib.py) implements independent quadrature and finite-difference/spline diagnostics without importing CLASS. The original source code is byte-identical; [replay.py](replay.py) isolates writes and compares saved outputs.

The grid uses a matter-only late-time convention, not a full observational model. The comparison tolerance is the original absolute 1e-9 plus relative 1e-6. Frozen [raw output](reference/raw-stdlib-checks.json) and [summary](reference/stdlib-summary.json) include interpolation failures; a faithful replay must retain these failures rather than claim a universal pass. Runtime fields are not scientific comparisons.

Author agreement was recorded on 21 October 2026 and concerns the denominator only. No private correspondence is distributed. Confirmation does not establish a verified complete correction, observational impact, perturbation prediction or code-to-original-chain provenance. This package does not run CLASS, a likelihood, posterior, or compiled corrected code.

The historical derivation/protocol is linked in [PROTOCOL.md](PROTOCOL.md); packaging adapters are retrospective and require exact-package validation. Preparation itself is not P2 or publication approval.

The 10 November fresh informed P2 successfully replayed these unchanged executable/grid/reference bytes within their narrow scope, retaining the original interpolation failures. This editorial revision still requires an exact-target documentary delta; no new blind confirmation or publication is implied.
