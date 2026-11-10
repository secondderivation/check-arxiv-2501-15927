#!/usr/bin/env python3
"""Retrospective packaging adapter; never changes the frozen diagnostic or reference."""
from pathlib import Path
import argparse,json,math,shutil,subprocess,sys
p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
root=Path(__file__).resolve().parent;work=Path(args.output).resolve()
if work.exists():raise SystemExit('Output must be a new directory')
work.mkdir(parents=True);(work/'results').mkdir();shutil.copyfile(root/'inputs/grid.json',work/'results/grid.json')
subprocess.run([sys.executable,str(root/'check-stdlib.py')],cwd=work,check=True,timeout=65)
from compare_reference import compare
issues=[]
for name in ['raw-stdlib-checks.json','stdlib-summary.json']:
 compare(json.loads((root/'reference'/name).read_text()),json.loads((work/'results'/name).read_text()),issues,name)
result={'reference_replay_pass':not issues,'issues':issues,'comparison':'absolute 1e-9 + relative 1e-6; elapsed_seconds excluded','scientific_scope':'fixed local diagnostic only; original interpolation failures remain failures'}
(work/'comparison.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
raise SystemExit(bool(issues))
