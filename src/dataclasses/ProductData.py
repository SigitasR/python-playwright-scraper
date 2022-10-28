from dataclasses import dataclass


@dataclass
class ProductData:
    title: str
    price: str
    in_stock: bool
