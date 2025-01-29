from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CostShippingByProduct:
    product_dimensions: int
    weight: int
    delivery_address: str
    delivery_time: float
    insurance_value: float
    carrier: Carrier

    @property
    def price_shipping(
        self,
    ) -> float:
        return self.carrier.calculate(
            self.product_dimensions,
            self.weight,
            self.delivery_address,
            self.delivery_time,
            self.insurance_value,
        )


class Carrier(ABC):
    @abstractmethod
    def calculate(
        self,
        product_dimensions: int,
        weight: int,
        delivery_address: str,
        delivery_time: float,
        insurance_value: float,
    ) -> float:
        pass


class Correios(Carrier):
    def calculate(
        self,
        product_dimensions: int,
        weight: int,
        delivery_address: str,
        delivery_time: float,
        insurance_value: float,
    ) -> float:
        return weight * delivery_time


class Express(Carrier):
    def calculate(
        self,
        product_dimensions: int,
        weight: int,
        delivery_address: str,
        delivery_time: str,
        insurance_value: float,
    ) -> float:
        return product_dimensions * delivery_time
    

correios = Correios()
express = Express()
bed = CostShippingByProduct(
    200,20,"Rua 05",20,2,correios
)

print(bed.price_shipping)

bed.carrier = express
print(bed.price_shipping)
