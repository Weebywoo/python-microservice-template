from pydantic import BaseModel


class GetHealthResponse(BaseModel):
    status: str
