"""Minimal fertilizer pricing defaults for local tests."""
DEFAULT_PRICES_BY_CURRENCY = {}


def get_default_price_for_currency(_slug: str, _currency: str) -> float:
    return 0.0


def load_default_fertilizers():
    return []


def build_price_map(*_args, **_kwargs):
    return {}


def get_user_currency(*_args, **_kwargs):
    return {"code": "MXN"}
