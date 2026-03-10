from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    country: str


addr = Address("Shibuya Crossing", "Tokyo", "Japan")

print(addr)
