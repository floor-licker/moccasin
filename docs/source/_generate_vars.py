from pathlib import Path

import tomli_w

from moccasin.constants.vars import (
    DEFAULT_NETWORKS_BY_NAME,
    ERAVM,
    FORK_NETWORK_DEFAULTS,
    LOCAL_NETWORK_DEFAULTS,
    PYEVM,
)

AUTOGENERATED_DIR = Path(__file__).parent.joinpath("_autogenerated")

PYEVM_FILE = "pyevm_defaults.rst"
ERAVM_FILE = "eravm_defaults.rst"
FORKS_FILE = "fork_defaults.rst"
EXPLORER_FILE = "explorer_defaults.rst"


def clean_dict_for_toml(data):
    if isinstance(data, dict):
        return {k: clean_dict_for_toml(v) for k, v in data.items()}
    elif data is None:
        return "None"
    elif isinstance(data, bool):
        return str(data).lower()
    else:
        return data


def clean_networks_for_toml(networks_dict):
    return clean_dict_for_toml(networks_dict)


if __name__ == "__main__":
    with open(AUTOGENERATED_DIR.joinpath(PYEVM_FILE), "wb") as f:
        cleaned_defaults = clean_dict_for_toml(LOCAL_NETWORK_DEFAULTS[PYEVM])
        tomli_w.dump(cleaned_defaults, f)

    with open(AUTOGENERATED_DIR.joinpath(ERAVM_FILE), "wb") as f:
        cleaned_defaults = clean_dict_for_toml(LOCAL_NETWORK_DEFAULTS[ERAVM])
        tomli_w.dump(cleaned_defaults, f)

    with open(AUTOGENERATED_DIR.joinpath(FORKS_FILE), "wb") as f:
        defaults = clean_dict_for_toml(FORK_NETWORK_DEFAULTS)
        tomli_w.dump(cleaned_defaults, f)

    with open(AUTOGENERATED_DIR.joinpath(EXPLORER_FILE), "wb") as f:
        defaults = clean_dict_for_toml(DEFAULT_NETWORKS_BY_NAME)
        tomli_w.dump(defaults, f)
