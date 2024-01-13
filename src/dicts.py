def add_item_to_dict(items: dict, key: str, value: int) -> dict:
    items[key] = value
    return items


def get_item_from_dict(items: dict, key: str) -> int:
    return items[key]