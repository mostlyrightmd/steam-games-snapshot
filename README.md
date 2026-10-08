# Steam metadata snapshot for Mojipixel

Zero-price entries from [FronkonGames / Martin Bustos's Steam Games Dataset](https://huggingface.co/datasets/FronkonGames/steam-games-dataset), converted from Parquet to JSON for ingestion by Mostly Right.

Source revision: `ba4e26785af33bee500e96597068c6e77f4edea9`.

This is a third-party snapshot, not a live Steam feed or an exhaustive list of currently available free games. Zero price can include playtests or unavailable products. The downstream dataset intersects these entries with the Steam free-game catalog and reports its actual coverage. No CLEF labels or emoji annotations have been generated in this source mirror.

Every original field of each selected row is retained. Image and video values remain publisher URLs; no media binaries are included. `manifest.json` records row counts and SHA-256 hashes. Source attribution and snapshot provenance must accompany reuse.

The upstream dataset card declares MIT for its compilation. This mirror does not grant rights to Valve or game publishers' descriptions, branding, artwork or other third-party material.

## Reproduce

Download `data/train-00000-of-00001.parquet` at the source revision, then run:

```sh
uv run --with pyarrow python convert.py path/to/source.parquet --out .
```
