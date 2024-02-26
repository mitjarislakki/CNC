from typing import Any, Dict

GlobalCache = Dict[str, Any]

_global_cache: GlobalCache = dict()


def get_global_cache() -> GlobalCache:
    return _global_cache


def set_global_cache(key: str, value):
    _global_cache[key] = value


def delete_from_cache(key: str):
    del _global_cache[key]
