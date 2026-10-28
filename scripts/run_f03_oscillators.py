"""F03 deterministic synthetic run plus opt-in real-data CSV analysis."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from toe001.me007_experiment import Calibration,coupled_langevin,csv_read,csv_write,file_sha256,summarize

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',help='External CSV with time,phi,chi')
    p.add_argument('--calibration',help='Independent physical calibration JSON; required with --input')
    p.add_argument('--out',default='results/f03_oscillator_reference.json')
    p.add_argument('--steps',type=int,default=200000)
    p.add_argument('--burn',type=int,default=20000)
    p.add_argument('--stride',type=int,default=6)
    p.add_argument('--bootstrap',type=int,default=120)
    p.add_argument('--seed',type=int,default=20261028)
    p.add_argument('--synthetic-csv',help='Optional explicitly synthetic CSV export')
    args=p.parse_args()
    if args.input:
        if not args.calibration:p.error('--input requires separately measured --calibration JSON')
        fields=json.loads(Path(args.calibration).read_text())
        if any(k not in Calibration.__dataclass_fields__ for k in fields):
            p.error('Unknown calibration field')
        cal=Calibration(**fields)
        records=csv_read(args.input)
        origin={'type':'external-measurement-file',
                'measurement_claim':'UNVERIFIED_USER_SUPPLIED',
                'sha256':file_sha256(args.input),'input_path':str(args.input),
                'calibration_path':str(args.calibration),
                'calibration_sha256':file_sha256(args.calibration)}
    else:
        if args.calibration:p.error('Calibration file used only with --input')
        cal=Calibration()
        records=list(coupled_langevin(cal,steps=args.steps,burn=args.burn,
                                      stride=args.stride,seed=args.seed))
        origin={'type':'independently simulated stochastic Langevin time-series',
                'seed':args.seed,'steps':args.steps,'burn':args.burn,
                'stride':args.stride,'measurement_claim':'SYNTHETIC_ONLY'}
        if args.synthetic_csv:
            Path(args.synthetic_csv).parent.mkdir(parents=True,exist_ok=True)
            csv_write(args.synthetic_csv,records)
            origin['synthetic_csv_sha256']=file_sha256(args.synthetic_csv)
    result={'protocol':'F03_TWO_MODE_INFORMATION_BRIDGE_V1',
            'calibration':vars(cal),'origin':origin,
            'analysis':summarize(records,cal,bootstrap=args.bootstrap),
            'historical_ME006_tensor_identified':False,
            'new_efmw_physics_established':False,
            'note':'Agreement only validates conventional coupled stochastic dynamics; F02 q is not measured.'}
    destination=Path(args.out)
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(destination),'source':origin['type'],
                      'observed_MI':result['analysis']['observed_MI_nats'],
                      'equilibrium_MI':result['analysis']['theory_MI_nats_from_independently_specified_stiffness'],
                      'CI':result['analysis']['paired_block_bootstrap_95pct']},indent=2))
if __name__=='__main__':main()
