# Import the Bot class from the instabot library
from instabot import Bot

# Create an object of the Bot class
bot = Bot()

# Login to Instagram using username and password
bot.login(
    username="your_username_here",      # Instagram username
    password="your_password_here"       # Instagram password
)

# Follow a user by their username (NOT a hashtag)
bot.follow("target_username_here")

# Example: follow another account
# bot.follow("account_name")

# Upload a photo to Instagram
# photo path must end with .jpg
# caption is the text below the photo
# bot.upload_photo("photo_path.jpg", caption="Your caption here")

# Unfollow a user by username
bot.unfollow("username_to_unfollow")

# Send a direct message to a user
bot.send_message(
    "I love Python 🐍",                 # Message text
    ["receiver_username_here"]          # List of usernames
)

# Get followers of a user
followers = bot.get_user_followers("username_whose_followers_you_want")

# Loop through each follower ID
for follower in followers:
    # Print detailed information about each follower
    print(bot.get_user_info(follower))

# Get following list of a user
following = bot.get_user_following("username_whose_following_you_want")

# Loop through each following ID
for user in following:
    # Print detailed information about each following user
    print(bot.get_user_info(user))
