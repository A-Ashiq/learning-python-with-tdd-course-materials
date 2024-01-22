def divide_numbers(x: int, y: int) -> int | str:
    try:
        return x / y
    except (TypeError, ZeroDivisionError):
        return "N/A"
