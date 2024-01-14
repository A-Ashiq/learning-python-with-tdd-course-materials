def divide_numbers(x: int, y: int) -> int | str:
    try:
        return x / y
    except TypeError:
        return "N/A"
