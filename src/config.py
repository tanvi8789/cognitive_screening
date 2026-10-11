import yaml


def load_config(path: str = "src/config.yaml"):
    """Load YAML configuration.
    Returns a dict with default values if file is missing.
    """
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}

