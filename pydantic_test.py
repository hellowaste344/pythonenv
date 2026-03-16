from typing import List

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    conint,
    constr,
    field_validator,
    model_validator,
)


class UserProfile(BaseModel):
    name: str
    age: int
    department: str
    is_active: bool = True

    @field_validator("age")
    def check_age(cls, value):
        if value < 18:
            raise ValueError("Invalid Age")
        return value


try:
    user = UserProfile(name="Lucie", age=20, department="Information Technology")
    print(user.name)
    user.age = 21
    print(user.age)
    print(user.department)

except ValidationError as e:
    print(e.json())


class UserAuth(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(cls, model):
        if model.password != model.confirm_password:
            raise ValueError("Invalid Authentication")
        return model


print(UserAuth(password="password", confirm_password="password"))


class Address(BaseModel):
    street: str
    city: str


class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address


address = Address(street="The Wall Street", city="New York City")
user1 = User(name="x-ashe", age=20, email="@example.com", address=address)
print(user1)

data = """
    {
    "name": "lucie",
    "age": 20,
    "email": "@example.com",
    "address": {
        "street": "Shibuya",
        "city": "Tokyo"
        }
    }
"""
user2 = User.model_validate_json(data)

json_data = user2.model_dump_json()
print(json_data)


PositiveInt = conint(gt=0)


class Product(BaseModel):
    name: constr(min_length=1)
    price: PositiveInt
    tags: List[str] = []


p = Product(name="Dictionary", price=10, tags=["stationery"])

print(p)


class NewUser(BaseModel):
    user_name: str = Field(..., alias="name")
    age: int = Field(18, description="Age of the user")  # default and description


user3 = NewUser(name="Terra")
print(user3.model_dump())
