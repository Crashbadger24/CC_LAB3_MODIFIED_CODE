from products import dao
from dataclasses import dataclass, asdict
#entire code has been changed 
@dataclass
class Product:
    id: int
    name: str
    description: str
    cost: float
    qty: int = 0

    @classmethod
    def load(cls, data: dict):
        return cls(**data)

def list_products():
    return map(Product.load, dao.list_products())

def get_product(product_id: int):
    return Product.load(dao.get_product(product_id))

def add_product(product: dict):
    dao.add_product(asdict(product) if isinstance(product, Product) else product)

def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
