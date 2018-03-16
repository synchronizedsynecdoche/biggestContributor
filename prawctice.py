import praw
import operator
import os
reddit = praw.Reddit(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'], password=os.environ["password"], user_agent="biggestContributor", username="papertow3ls")

print(reddit.user.me())
dict = {}
sub = reddit.subreddit('pics').hot()
for submission in reddit.subreddit('BlackPeopleTwitter').new(limit=10):
    author = submission.author.name
    print(submission.score)
    if(not dict.has_key(author)):
        dict[author] = 1
    else:
        count = dict[author]
        count += 1
        dict[author] = count

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
sorted_dict.reverse()

stop_count = 0

for key in sorted_dict:
    if(stop_count == 10):
        break
    else:
        stop_count += 1
