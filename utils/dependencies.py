from fastapi import Header


def get_app_name(
    x_app_name: str | None = Header(default=None)
):
    return x_app_name