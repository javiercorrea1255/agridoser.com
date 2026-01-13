"""Minimal security helpers for local test runs."""


def create_access_token(*_args, **_kwargs) -> str:
    return "local-test-token"
