import sys
import praw
from prawcore import NotFound
import webbrowser as wb
import datetime

# import praw credentials from praw.ini
reddit = praw.Reddit('bot1'',
                     user_agent="bot1_user_agent")

sub = ''.join(sys.argv[1])

# check if the subreddit exists
try:
    reddit.subreddits.search_by_name(sub, exact=True)
except NotFound:
    print >> sys.stderr, "Subreddit " + sub + " does not exist"
    sys.exit(1)

# output the top ten posts for the current day
print("Top posts for reddit/r/" + sub + " on " + datetime.date.today().strftime("%Y-%m-%d") + "\n")
for submission in reddit.subreddit(sub).hot(limit=10):
    wb.open_new_tab(submission.url)
    print(submission.title)
