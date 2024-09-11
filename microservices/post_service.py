# Class for Post Service
class PostService:
    def __init__(self):
        self.posts = list()

    def get(self, post_id):
        result = None
        for post in self.posts:
            if post.id == post_id:
                result = post
                break
        return result
    
    def getUserPosts(self, user_id):
        result = []
        for post in self.posts:
            if post.user_id == user_id:
                result.append(post)
        return result
    
    def create(self, post):
        self.posts.append(post)

    def update(self, post_id, post):
        for i, post in enumerate(self.posts):
            if post.id == post_id:
                self.posts[i] = post
                break
    
    def delete(self, post_id):
        for i, post in enumerate(self.posts):
            if post.id == post_id:
                self.posts.pop(i)
                break
    