class CommentService:
    def __init__(self):
        self.comments = list()

    def get(self, comment_id):
        result = None
        for comment in self.comments:
            if comment.id == comment_id:
                result = comment
                break
        return result
    
    def getPostComments(self, post_id):
        result = []
        for comment in self.comments:
            if comment.post_id == post_id:
                result.append(comment)
        return result

    def create(self, comment):
        print(f"Creating Comment {comment}")
        self.comments.append(comment)

    def update(self, comment_id, Comment):
        for i, comment in enumerate(self.comments):
            if comment.id == comment_id:
                self.comments[i] = Comment
                break

    def delete(self, comment_id):
        for i, comment in enumerate(self.comments):
            if comment.id == comment_id:
                self.comments.pop(i)
                break
