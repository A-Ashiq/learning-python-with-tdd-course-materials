def add_item_to_list(items: list[int], item: int) -> list[int]:
    items.append(item)
    return items


def remove_item_from_list(items: list[int], item: int) -> list[int]:
    items.remove(item)
    return items


def add_list_to_list(items: list[int], items_to_be_added: list[int]) -> list[int]:
    items.extend(items_to_be_added)
    return items


def get_index_of_item(items: list[str], item: str) -> int:
    return items.index(item)


def insert_item_at_index(items: list[str], index: int, item: str) -> list[str]:
    return items.insert(index, item)


def sort_items_in_list(items: list[str]) -> list[str]:
    return items.sort()


def count_items(items: list[str]) -> int:
    return len(items)