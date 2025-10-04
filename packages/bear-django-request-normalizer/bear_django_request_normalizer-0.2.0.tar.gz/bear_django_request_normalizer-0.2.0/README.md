# Django Request Normalizer

A configurable Django middleware that automatically cleans and normalizes incoming request data before it reaches your views.

## Features

-   **Trims Whitespace:** Strips leading/trailing whitespace from all string values.
-   **Normalizes Booleans:** Converts string values like `"true"` and `"false"` to actual booleans.
-   **Normalizes Nulls:** Converts string `"null"`, empty strings `""` for ID fields, and integer `0` for ID fields to `None`.
-   **Cleans Email:** Removes spaces and lowercases email fields.
-   **Handles All Data:** Works seamlessly with `GET` parameters, `application/json`, `multipart/form-data`, and `x-www-form-urlencoded` data.
-   **Configurable:** You can enable/disable the middleware or specify which URL prefixes it should act on.

## Installation

```bash
pip install django-request-normalizer
```

## Usage

1.  Add the middleware to your `MIDDLEWARE` list in `settings.py`. It should be placed before any middleware that accesses request data, such as DRF's authentication classes or your own views.

```python
# settings.py
MIDDLEWARE = [
    # ...
    'request_normalizer.middleware.RequestNormalizerMiddleware',
    # ...
]
```
