"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    qty = int(value.strip())
    if qty < 0:
        raise ValueError("quantity must not be negative")
    return qty
