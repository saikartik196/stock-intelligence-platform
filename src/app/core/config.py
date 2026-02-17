from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parents[3]


def load_config(config_path: str = "configs/base.yaml") -> dict:
    full_path = BASE_DIR / config_path
    with open(full_path, "r") as file:
        return yaml.safe_load(file)
