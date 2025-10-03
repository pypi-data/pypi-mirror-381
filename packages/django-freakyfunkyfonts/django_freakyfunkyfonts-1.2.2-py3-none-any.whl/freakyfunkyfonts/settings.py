import os
import tomllib  # Python 3.11+; for older use `tomli`

DEFAULTS = {
    "fonts": {
        "pool": ["Arial", "Courier New", "Times New Roman", "Verdana", "Comic Sans MS"],
    },
    "inject": {
        "google_fonts_link": None,
    },
    "behaviour": {
        "skip_tags": ['head', 'title', 'meta', 'link', 'style', 'script'],
        "scope": ["body", "main", "article"]
    },
    "date_ranges": None
}

def load_config():
    path = os.path.join(os.getcwd(), "freakyfunkyfonts.toml")
    if os.path.exists(path):
        with open(path, "rb") as f:
            return tomllib.load(f)
    return DEFAULTS.copy()
