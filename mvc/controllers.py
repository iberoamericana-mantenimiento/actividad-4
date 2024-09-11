users = []
posts = []
comments = []

# Controller to get all users
def get_users():
    return users

# Controller to get one user
def get_user(user_id):
    result = None
    for user in users:
        if user.id == user_id:
            result = user
            break
    return result

# Controller to get user posts
def get_user_posts(user_id):
    result = []
    for post in posts:
        if post.user_id == user_id:
            result.append(post)
    return result

# Controller to create a user
def create_user(user):
    users.append(user)

# Controller to update a user
def update_user(user_id, user):
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i] = user
            break

# Controller to delete a user
def delete_user(user_id):
    for i, user in enumerate(users):
        if user.id == user_id:
            users.pop(i)
            break

# Controller to get all posts
def get_posts():
    return posts

# Controller to get one post
def get_post(post_id):
    result = None
    for post in posts:
        if post.id == post_id:
            result = post
            break
    return result

# Controller to get post comments
def get_post_comments(post_id):
    result = []
    for comment in comments:
        if comment.post_id == post_id:
            result.append(comment)
    return result

# Controller to create a post
def create_post(post):
    posts.append(post)

# Controller to update a post
def update_post(post_id, post):
    for i, post in enumerate(posts):
        if post.id == post_id:
            posts[i] = post
            break

# Controller to delete a post
def delete_post(post_id):
    for i, post in enumerate(posts):
        if post.id == post_id:
            posts.pop(i)

# Controller to get all comments
def get_comments():
    return comments

# Controller to get one comment
def get_comment(comment_id):
    result = None
    for comment in comments:
        if comment.id == comment_id:
            result = comment

# Controller to create a comment
def create_comment(comment):
    comments.append(comment)

# Controller to update a comment
def update_comment(comment_id, comment):
    for i, comment in enumerate(comments):
        if comment.id == comment_id:
            comments[i] = comment
            break

# Controller to delete a comment
def delete_comment(comment_id):
    for i, comment in enumerate(comments):
        if comment.id == comment_id:
            comments.pop(i)
            break
