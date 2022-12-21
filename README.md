# Keeb-Hunter

A script for finding and entering reddit giveaways on r/MechanicalKeyboards

# How it works

When you run the program, it initially searches a large sample of the most recent posts for posts with the keyword 'giveaway' in the title or posts with the Giveaway flair. If it finds a post not already listed in the storage text file, it will comment on that post, add it to the list, and email you to tell you that it commented on the post with a link to the post.

After that, it will check for new posts it hasn't commented on every ten seconds and repeat the above process when it finds an unentered giveaway.

# How to use

1. Download `main.py` and `emailer.py`
2. Create a file called `.env` and include the following environment variables
   - CLIENT_ID='client id of your reddit api'
   - SECRET_KEY='secret key of your reddit api'
   - USER_AGENT='A name for your reddit api/bot'
   - REDDIT_USERNAME='the reddit username of your bot'
   - REDDIT_PASSWORD='your bots reddit password'
   - BOT_EMAIL_ADDRESS='your bots email address'
   - BOT_EMAIL_PASSWORD='the app password of your bots google account'
   - MY_EMAIL_ADDRESS='your email address the emails will be sent to'
3. Create an empty storage.txt file
4. Run `main.py`

Note: Put all your files in the same directory
