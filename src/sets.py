def add_item_to_set(items: set, item: str) -> set:
    items.add(item)
    return items


def get_difference(main: set, secondary: set) -> set:
    return set(main).difference(secondary)
