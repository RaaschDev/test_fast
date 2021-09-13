from typing import List, Optional

from pydantic import BaseModel


class Model(BaseModel):
    id: Optional[str] = None


class Usuario(Model):
    name: str
    phone: str
    my_products: List(Produto)
    my_sales: List(Pedido)
    my_requests: List(Pedido)


class Produto(Model):
    usuario: Usuario
    nome: str
    details: str
    price: float
    available: bool = False


class Pedido(Model):
    usuario: Usuario
    produto: Produto
    quantity: int
    delivery: bool = False
    address: str
    notes: Optional[str] = 'Sem observacoes'
