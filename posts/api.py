from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from posts.models import Post
from posts.schemas import PostSchema, PostCreateSchema, PostUpdateSchema, UserSchema

app = NinjaAPI()


@app.get("/hello")
def hello(request):
    return "Hello world"


@app.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@app.get("/users", response={200: list[UserSchema]})
def get_users(request):
    return User.objects.all()


@app.get(
    "/posts",
    response={200: list[PostSchema]},
    description="this returns a list of posts",
)
def get_posts(request):
    return Post.objects.all()


@app.post("/posts", response=PostSchema, description="this creates one post")
def create_post(request, payload: PostCreateSchema):
    post = Post.objects.create(**payload.dict())
    return post


# to continue later...
@app.put("/posts/{post_id}", description="this updates one post")
def update_post(request, post_id: int, payload: PostUpdateSchema):  # <===
    post = get_object_or_404(Post, id=post_id)
    for attr, value in payload.dict().items():
        setattr(post, attr, value)
        post.save()
        return {"updated": True}


# to continue later...


@app.delete("/posts/{post_id}", description="this delete one post")
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return {"deleted": True}
