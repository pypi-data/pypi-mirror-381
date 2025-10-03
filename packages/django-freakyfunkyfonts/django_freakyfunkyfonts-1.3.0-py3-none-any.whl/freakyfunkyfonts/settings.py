import os
import sys
import configparser

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
    "date_ranges": None,
    "paths": {
        "include": [],  # e.g. ["/^/funky/", "/^/blog/"]
        "exclude": ["/^/admin/", "/^/api/"]
    }
}

def load_config():
    path_toml = os.path.join(os.getcwd(), "freakyfunkyfonts.toml")
    path_ini = os.path.join(os.getcwd(), "freakyfunkyfonts.ini")
    # Try TOML first
    if os.path.exists(path_toml):
        if sys.version_info >= (3, 11):
            import tomllib
            with open(path_toml, "rb") as f:
                return tomllib.load(f)
        else:
            try:
                import tomli
                with open(path_toml, "rb") as f:
                    return tomli.load(f)
            except ImportError:
                pass
    # Fallback to INI
    if os.path.exists(path_ini):
        config = configparser.ConfigParser()
        config.read(path_ini)
        # Convert INI sections to dict
        return {section: dict(config.items(section)) for section in config.sections()}
    return DEFAULTS.copy()
