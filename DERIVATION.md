# Confirmed denominator discrepancy: derivation and limits

The exact reviewed source is arXiv:2501.15927v3. The equation locators below were checked against PDF/TeX in the historical audit. This public edition records that evidence; it does not inspect a journal revision or rerun an inference.

## Fixed-source transcription

Paper Eq. 7, p.3 / TeX lines 338-343: psi(z) = 0.015 (1+z)^2.7 / [1+((1+z)/2.9)^5.6], in solar masses/year/Mpc³. a=(1+z)^(-1), a0=1.

Paper Eq. 9, p.3 / lines 377-381: H²=H0² Omega_m0 (1+z)^3 + Lambda/3 -8 A integral_zi^z psi/(1+z) dz. Define A=tilde(alpha) C; this is paper C_n in Eq. 11 (lines 398-401).

Paper Eq. 12, p.3 / lines 417-420: rho_DE=-3 A/(pi G) integral_zi^z psi/(1+z) dz. As printed, this omits the additive Lambda/(8 pi G) required by Eq. 9 for nonzero Lambda. Its derivative is nevertheless the correct derivative of that full density. Do not silently treat Eq. 12 as the full Model II density.

Paper Eq. 13, p.3 / lines 434-438: w=-1-2 A psi/[Lambda/4-6 A integral_zi^z psi/(1+z) dz]. This agrees with the full Eq. 9 density (including Lambda).

Paper Eq. 16, p.4 / lines 522-525: Lambda=3(1-Omega_m0)H0² -24 A integral_0^zi psi/(1+z) dz.

Paper Eq. 18, p.5 / lines 539-542: E²=Omega_m0(1+z)^3+1-Omega_m0 -8 A/H0² integral_0^z psi/(1+z) dz. The printed expression lacks the final differential in Eq. 18; its meaning is fixed by surrounding integral definitions.

Paper Eq. 19, p.5 / lines 547-551: w=-1-8 A psi/[3(1-Omega_m0)H0²+6 A integral_0^z psi/(1+z) dz]. Both TeX and PDF have +6. No transcription uncertainty accounts for the discrepancy below.

## Local derivation

Use q=A/H0², with compatible units and the numeric ψ convention held fixed. Paper C_n and code Cn_wgb must not be equated numerically: code reads Cn_wgb directly without the H0 conversion. Calling q dimensionless presupposes absorbing the quoted SFR units; only qψ and qI need be dimensionless here. The historical audit did not establish an empirical unit conversion for a paper inference run.

Let I(a)=integral_a^1 psi(x)/x dx. Then I'=-psi/a. Define the code integral I_code(a)=integral_1^a psi(x)/x dx=-I(a), so I_code'=psi/a. The historical symbol Iz in the code diagnostic means I_code, not the paper redshift integral I_z,paper=integral_0^z psi(z')/(1+z') dz'=I(a). With r=1-Omega_m0 in the paper's flat matter-only model, the full density is rho_DE=(3 H0²/8piG) R(a), R=r-8q I. D=3R=3r-24q I=3r+24q I_code. From continuity, w=-1-a rho'_DE/(3rho_DE)=-1-8q psi/D. Alternatively substituting Eq. 16 in Eq. 13 gives exactly the same denominator. Thus Eq. 18 and Eq. 13+16 imply -24, not the +6 in Eq. 19.

psi(a)=0.015 a^(-2.7)/[1+(2.9a)^(-5.6)]. With t=(2.9a)^(-5.6), psi'=psi[-2.7/a+5.6t/(a(1+t))]. D'=24q psi/a, so w'=8q[-psi' D+24q psi²/a]/D². The denominator in the immediate parent is D_old=3r+6q I=3r-6q I_code; its derivative expression is internally consistent with that different w.


The author agreement concerns the Eq. 19 denominator correction only. Corrected code, complete manuscript correction and observational impact have not been independently verified. Other code/interpolation diagnostics remain separate and unconfirmed. The historical correction audit was informed, not a newly blind B.

Thus the paper redshift-integral coefficient +6 becomes -24, while the code-integral coefficient -6 becomes +24. The saved diagnostic constructs the code integral by subtracting the table value at a=1. This clarifies the original convention without changing any formula, executable, reference or empirical inference claim.
