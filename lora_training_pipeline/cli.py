import argparse
from pathlib import Path
import toml

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()

    cfg_path = Path(args.config)
    if not cfg_path.exists():
        raise FileNotFoundError(cfg_path)

    cfg = toml.load(cfg_path)
    print("Loaded config:")
    print(cfg)
