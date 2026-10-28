"""Generate deterministic F02 scalar--tensor reference; synthetic mathematical calculation."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from toe001.me007_covariant import simulate

if __name__=='__main__':
    p=Path('results/me007_covariant_reference.json')
    p.parent.mkdir(parents=True,exist_ok=True)
    obj=simulate(steps=2400,dt=.001)
    p.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in obj.items() if k.startswith('max_') or k.startswith('toy_') or k.startswith('constant_')},indent=2))
