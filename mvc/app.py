from models import User, Post, Comment
from controllers import create_user, create_post, create_comment, get_user, get_user_posts, get_post, get_post_comments

# For this example we are going to use print as our view, but in a real application we would use a template engine
# like the file in this folder called index.html
class App:    

    def createUsers(self):
        self.user1 = User()
        self.user1.id = 1
        self.user1.username = "Diego"
        create_user(self.user1)

        self.user2 = User()
        self.user2.id = 2
        self.user2.username = "Ana"
        create_user(self.user2)

    def createPosts(self):
        self.post1 = Post()
        self.post1.id = 1
        self.post1.user_id = 1
        self.post1.content = "First post"
        create_post(self.post1)

        self.post2 = Post()
        self.post2.id = 2
        self.post2.user_id = 2
        self.post2.content = "Second post"
        create_post(self.post2)

        self.post3 = Post()
        self.post3.id = 3
        self.post3.user_id = 1
        self.post3.content = "Third post"
        create_post(self.post3)

    def createComments(self):
        self.comment1 = Comment()
        self.comment1.id = 1
        self.comment1.post_id = 1
        self.comment1.content = "comment1"
        create_comment(self.comment1)

        self.comment2 = Comment()
        self.comment2.id = 2
        self.comment2.post_id = 2
        self.comment2.content = "comment2"
        create_comment(self.comment2)

    def run(self):
        print("Initializing testing data")
        self.createUsers()
        self.createPosts()
        self.createComments()

        print("Getting user data form user service")
        user = get_user(1)
        print(f"User data:")
        print(user)
        user.posts = get_user_posts(1)
        print(f"User posts:")
        for post in user.posts:
            print(post)
            post.comments = get_post_comments(post.id)
            print(f"Post comments:")
            for comment in post.comments:
                print(comment)
        print("End of user data from user service")
        print("------------------------------------------------")

        print("Getting post data from post service")
        post = get_post(1)
        print(f"Post data:")
        print(post)
        post.comments = get_post_comments(1)
        print(f"Post comments:")
        for comment in post.comments:
            print(comment)
        print("End of post data from post service")

app = App()
app.run()