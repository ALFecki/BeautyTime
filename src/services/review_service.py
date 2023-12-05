from typing import Type
from base.base_service import BaseService
from repositories.review_repository import ReviewRepository

class ReviewService(BaseService):
    @property
    def repository(self) -> type[ReviewRepository]:
        return ReviewRepository