import praw
import json

# Create reddit instance.
reddit = praw.Reddit(user_agent = True, client_id = "lRdHZehU8QxMGQzIvSYLiQ", 
                     client_secret = "4YDwccpbiJVnFkHHYNpxzKRPffEjKQ", 
                     username = "H2REBE2R", password = "b2n2n2432")

# Get subreddit instance. Change this field to the subreddit you want to scrape.
subreddit = reddit.subreddit("relationship_advice")

# Initialize empty list to store posts
posts = []

# Iterate through the new submission in the subreddit
for submission in subreddit.hot(limit=10):

    if submission.stickied:
        continue

    if submission.author is None or submission.author.name == "Justkeepitanonymous":
        continue

    # Append the submission title and URL to the posts list
    posts_data = {
        "title": submission.title,
        "post-author": str(submission.author),
        "text": submission.selftext,
        "comments": []
    }

    submission.comments.replace_more(limit=None)

    def get_comments(comments, commentSection):
        for comment in comments:
            if isinstance(comment, praw.models.MoreComments):
                continue
            if comment.author is None or comment.author.name == "Justkeepitanonymous": 
                continue
            comment_author = str(comment.author)
            commentSection.append({
                "body": comment.body,
                "comment-author": comment_author,
                "replies": []
            })
            get_comments(comment.replies, commentSection[-1]["replies"])

    get_comments(submission.comments, posts_data["comments"])

    posts.append(posts_data)

# Save the posts to a JSON file, change the final path to the json file you want
# to create.
with open("../../data/raw/reddit/relationship_advice.json", "w") as f:
    json.dump(posts, f, indent=4)
