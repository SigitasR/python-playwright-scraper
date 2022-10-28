from dataclasses import dataclass


@dataclass
class ProductInfo:
    title: str
    price: str
    in_stock: bool
