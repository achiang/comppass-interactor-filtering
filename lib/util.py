from glob import glob


def get_filtered_cwd():
    files = glob("*")
    blacklist = [
        "lib",
        "LICENSE",
        "README.md",
        "CompPASS_Interactor_Filtering.ipynb",
        "pyproject.toml",
    ]
    return [f for f in files if f not in blacklist]
