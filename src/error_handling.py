def divide_numbers(x: int, y: int) -> int | str:
    try:
        return x / y
    except (TypeError, ZeroDivisionError):
        return "N/A"


def get_item_from_dict(items: dict, key: str) -> str:
    try:
        return items[key]
    except KeyError:
        return "N/A"
    except TypeError:
        return "Invalid"


class FoodNotAvailableForBreedError(Exception):
    ...


def get_food_type_for_breed(breed: str) -> str:
    if breed == "Poodle":
        raise FoodNotAvailableForBreedError
