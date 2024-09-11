from models import User, Post, Comment
from user_service import UserService
from post_service import PostService
from comment_service import CommentService

class App:
    def __init__(self):
        self.userService = UserService()
        self.postService = PostService()
        self.commentService = CommentService()

    def createUsers(self):
        self.user1 = User()
        self.user1.id = 1
        self.user1.username = "Diego"
        self.userService.create(self.user1)

        self.user2 = User()
        self.user2.id = 2
        self.user2.username = "Ana"
        self.userService.create(self.user2)

    def createPosts(self):
        self.post1 = Post()
        self.post1.id = 1
        self.post1.user_id = 1
        self.post1.content = "First post"
        self.postService.create(self.post1)

        self.post2 = Post()
        self.post2.id = 2
        self.post2.user_id = 2
        self.post2.content = "Second post"
        self.postService.create(self.post2)

        self.post3 = Post()
        self.post3.id = 3
        self.post3.user_id = 1
        self.post3.content = "Third post"
        self.postService.create(self.post3)

    def createComments(self):
        self.comment1 = Comment()
        self.comment1.id = 1
        self.comment1.post_id = 1
        self.comment1.content = "comment1"
        self.commentService.create(self.comment1)

        self.comment2 = Comment()
        self.comment2.id = 2
        self.comment2.post_id = 2
        self.comment2.content = "comment2"
        self.commentService.create(self.comment2)

    def run(self):
        print("Initializing testing data")
        self.createUsers()
        self.createPosts()
        self.createComments()

        print("Getting user data form user service")
        user = self.userService.get(1)
        print(f"User data:")
        print(user)
        user.posts = self.postService.getUserPosts(1)
        print(f"User posts:")
        for post in user.posts:
            print(post)
            post.comments = self.commentService.getPostComments(post.id)
            print(f"Post comments:")
            for comment in post.comments:
                print(comment)
        print("End of user data from user service")
        print("------------------------------------------------")

        print("Getting post data from post service")
        post = self.postService.get(1)
        print(f"Post data:")
        print(post)
        post.comments = self.commentService.getPostComments(1)
        print(f"Post comments:")
        for comment in post.comments:
            print(comment)
        print("End of post data from post service")

        

app = App()
app.run()