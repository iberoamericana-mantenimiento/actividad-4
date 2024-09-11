class Comment:
    def __init__(self):
        self.id = 0
        self.post_id = 0
        self.content = ""

    def __str__(self):
        return f"id: {self.id}, post_id: {self.post_id}, content: {self.content}"

class Post:
    def __init__(self):
        self.id = 0
        self.user_id = 0
        self.content = ""
        self.comments = []
    
    def __str__(self):
        return f"id: {self.id}, user_id: {self.user_id}, content: {self.content}"

class User:
    def __init__(self):
        self.id = 0
        self.username = ""
        self.posts = []
        self.comments = []

    def __str__(self):
        return f"id: {self.id}, username: {self.username}"