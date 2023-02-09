import uuid

from dataclasses import dataclass

from src.entities.url import Url, DtoUrl
from src.repositories import IUrlRepository


@dataclass
class GetUrlRequest:
    hash: str


@dataclass
class GetUrlResponse:
    object: Url


class GetUrlUseCase:
    
    def __init__(self, repository: IUrlRepository):
        self.repository = repository
        
    def execute(self, request: GetUrlRequest) -> GetUrlResponse:
        return GetUrlResponse(
            object=self.repository.get(str(request))
        )