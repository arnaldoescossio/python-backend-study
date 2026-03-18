from typing import Generic, TypeVar, override

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


# Type checker infers:
x = first([1, 2, 3])  # x: int
y = first(["a", "b"])  # y: str

print(x)  # Output: 1
print(y)  # Output: "a"

## Creating a especific Typevar
Numeric = TypeVar("Numeric", int, float)


def add(a: Numeric, b: Numeric) -> Numeric:
    return a + b


result1 = add(1, 2)  # result1: int
result2 = add(1.5, 2.5)  # result2: float
result3 = add(1, 2.5)  # result3: float


print(result1)  # Output: 3
print(result2)  # Output: 4.0
print(result3)  # Output: 3.5

# print(add("Hello, ", "world!")) # This will raise a type error at runtime


# Generic class

class Dto():
    name : str 

D = TypeVar("D", bound=Dto)

class CreateDto(Dto):
    @override
    def __init__(self, name: str) -> None:
        self.name = name

class UpdateDto(Dto):
    @override
    def __init__(self, name: str) -> None:
        self.name = name

class BaseUseCase(Generic[D]):
    def execute(self, data: D) -> None:
        print(f"Executing use case with data: {data.name}")
    
class CreateUseCase(BaseUseCase[CreateDto]):
    pass

class UpdateUseCase(BaseUseCase[UpdateDto]):
    pass


create_use_case = CreateUseCase()
create_use_case.execute(CreateDto(name="Create Example"))
update_use_case = UpdateUseCase()
update_use_case.execute(UpdateDto(name="Update Example"))



