
from app.models import Post
from app.repositories import PostRepository


class PostService:
    def __init__(self):
        self.repository = PostRepository()

    def get_all(self) -> list[Post]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Post:
        return self.repository.get_by_id(id)

    def create(self, entity: Post)-> Post:
        return self.repository.create(entity)

    def update(self, id, Post) -> Post:
        return self.repository.update(id, Post)

    def delete(self, id)->bool:
        return self.repository.delete(id)