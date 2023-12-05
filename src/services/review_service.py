from typing import Type
from src.base.base_service import BaseService
from src.repositories.review_repository import ReviewRepository

class ReviewService(BaseService):
    @property
    def repository(self) -> type[ReviewRepository]:
        return ReviewRepository