"""Reproduce the zero-price JSON shards from the attributed Parquet snapshot."""
import argparse, hashlib, json
from pathlib import Path
import pyarrow.parquet as pq
p=argparse.ArgumentParser();p.add_argument('parquet');p.add_argument('--out',default='.');a=p.parse_args()
out=Path(a.out);(out/'data').mkdir(parents=True,exist_ok=True)
source=Path(a.parquet);table=pq.read_table(source);rows=table.to_pylist()
free=sorted((r for r in rows if r.get('price')==0),key=lambda r:int(r['appID']))
ids=[r['appID'] for r in free]
assert len(ids)==len(set(ids)), 'duplicate app IDs'
files=[]
for i in range(0,len(free),500):
 name=f'data/games-{i//500:04d}.json'; data=json.dumps({'rows':[{'row':r} for r in free[i:i+500]]},ensure_ascii=False,separators=(',',':')).encode()
 (out/name).write_bytes(data);files.append({'path':name,'rows':len(free[i:i+500]),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
manifest={'source':'https://huggingface.co/datasets/FronkonGames/steam-games-dataset','revision':'ba4e26785af33bee500e96597068c6e77f4edea9','parquet_sha256':hashlib.file_digest(source.open('rb'),'sha256').hexdigest(),'source_rows':len(rows),'selected_rows':len(free),'selection':'price == 0; not a guarantee of currently available free games','files':files}
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'source_rows':len(rows),'zero_price_rows':len(free),'files':len(files),'bytes':sum(f['bytes'] for f in files)}))
