from pydantic import BaseModel


class Customer(BaseModel):
    id: int
    name: str
    description: str | None = None
    email: str
    age: int
    

class Transaccion(BaseModel):
    id: int
    amount: int
    description: str

class Invoce(BaseModel):
    id: int
    customer: Customer
    transaccion: list[Transaccion]
    total: int

    @property
    def ammount_total(self):
        return sum([t.amount for t in self.transaccion])