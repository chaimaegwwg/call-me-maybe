from pydantic import BaseModel, ConfigDict


class Function_calling_test(BaseModel):
    prompt: str
    model_config = ConfigDict(
        extra="forbid")


class Parameter(BaseModel):
    type: str


class Returns(BaseModel):
    type: str


class Function_definition(BaseModel):
    name: str
    description: str
    parameters: dict[str, Parameter]
    returns: Returns

    model_config = ConfigDict(
        extra="forbid")
