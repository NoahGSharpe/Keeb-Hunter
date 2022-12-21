import os
import praw
import time
from dotenv import load_dotenv


def Comment_On_New_Giveaways(posts):
    for post in posts:
        if (post.id not in visited_post_ids and post.title.lower().find('giveaway') != -1 or post.link_flair_text == "Giveaway"):
            # Comment on the post
            post.add_comment('Thanks for the giveaway')

            # Add post id to list
            visited_post_ids.add(post.id)

            # Append post id to file
            with open('storage.txt', 'a') as file:
                file.write(f"\n{post.id}")


# Load environment variables
load_dotenv()
CLIENT_ID = os.environ['CLIENT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
USER_AGENT = os.environ['USER_AGENT']
USERNAME = os.environ['REDDIT_USERNAME']
PASSWORD = os.environ['REDDIT_PASSWORD']

# Create a reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=SECRET_KEY,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD
)

print(f"Logged in as {reddit.user.me()}\n")

# Instantiate subreddit
subreddit = reddit.subreddit('MechanicalKeyboards')

# Access already visited posts
with open('storage.txt', 'r') as file:
    contents = file.read()
    visited_post_ids = set(contents.split('\n'))

# Grab most recent posts
print('Finding new giveaway posts\n')
posts = subreddit.new(limit=200)
Comment_On_New_Giveaways(posts)

# Write post ids to storage file
print("Writing posts to a file")
with open('storage.txt', 'w') as file:
    file.write('\n'.join(visited_post_ids))

# Check for new posts every ten seconds and comment on new posts
while(True):
    # wait ten seconds
    time.sleep(10)

    # Grab new posts
    posts = subreddit.new(limit=2)
    Comment_On_New_Giveaways(posts)
