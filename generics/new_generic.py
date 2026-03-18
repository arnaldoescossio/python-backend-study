from typing import override


class Dto():
    name : str

class CreateDto(Dto):
    @override
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__()

class UpdateDto(Dto):
    @override
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__()

class BaseUseCase[D:Dto]:
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

