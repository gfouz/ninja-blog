from ninja import ModelSchema, Schema
from posts.models import Post, Category
from django.contrib.auth.models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User
        exclude = ["password", "last_login", "user_permissions"]


class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        fields = ["name", "description"]


class PostSchema(ModelSchema):
    author: UserSchema

    # categories: CategorySchema
    class Meta:
        model = Post
        fields = ["id", "title", "content"]


class PostCreateSchema(Schema):
    title: str
    content: str
    author_id: int = None


class PostUpdateSchema(PostCreateSchema):
    pass
