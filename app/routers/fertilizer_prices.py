"""Minimal fertilizer pricing defaults for local tests."""
DEFAULT_PRICES_BY_CURRENCY = {}


def get_default_price_for_currency(_slug: str, _currency: str) -> float:
    return {}


def load_default_fertilizers(_db=None):
    from app.services.fertiirrigation_ai_optimizer import _load_hydro_fertilizers_catalog

    catalog = _load_hydro_fertilizers_catalog()
    return [{"id": f["id"], "name": f.get("name", f["id"])} for f in catalog if f.get("id")]


def build_price_map(*_args, **_kwargs):
    return {}


def get_user_currency(*_args, **_kwargs):
    return {"code": "MXN"}
