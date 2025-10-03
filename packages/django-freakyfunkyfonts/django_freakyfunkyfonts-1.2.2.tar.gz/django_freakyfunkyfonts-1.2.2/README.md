# Freaky Funky Fonts Middleware (Django)

For when you feel the funk that freaks you fonts

## What it this?

Freaky Funky Fonts Middleware is essentially a Django “font chaos” middleware package with configurable behaviour.

It intercespts the html of Djangos reponses

## Usage

- Install the package
- Apply the middleare in your Django project settings as middleare
- (Optional but recommended) Configure in your `freakyfunkyfonts.toml` (or `.ini` for versions before python 3.11)


### Installing

```bash
pip install django-freakyfunkyfonts
```

### Applying

In the project settings

```py
MIDDLEWARE = [
    # ...
    "freakyfunkyfonts.middleware.FreakyFunkyFontsMiddleware",
]
```

### Configs

Example: 

```toml
[fonts]
# List of fonts to cycle through
pool = [
  "Times New Roman",
  "Georgia",
  "Merriweather",
  "Lora"
]

[inject]
# Extra tags to inject into <head> (Like a link tag to google fonts)
# More than one tag can be applied, just append to the list
# Make sure that the fonts in the pool are convered
tags = [
  '<link href="https://fonts.googleapis.com/css2?family=Merriweather&family=Lora&display=swap" rel="stylesheet">'
]

[behaviour]
# Scopes to operate on: "all" (If it should work on the whole html document), "body", or any tag names (article, main)
scopes = ["body", "article", "main"]

# HTML tags to skip completely
skip_tags = ['head', 'title', 'meta', 'link', 'style', 'script'] 

[date_ranges]
# List of date ranges with optional time ranges
include = [
  { range = "2025-10-01:2025-10-10", temporal = ["08:00-18:00"] },
  { range = "2025-12-24:2025-12-26", temporal = ["00:00-23:59"] }
]
exclude = [
  { range = "2025-12-31:2026-01-01", temporal = ["00:00-23:59"] }
]

# The middleware will only apply during the included date/time ranges, and will be skipped during excluded ranges.
# If no temporal is specified, the range applies for the whole day.
# If no ranges are defined, the middleware is always applied
```

## Dev

### Installing

```bash
pip install -e .
```