import praw 
r = praw.Reddit(user_agent='Comment Extraction (by/u/crystalballroom)',
                client_id='5Ofau0MfjYSsfw', client_secret="NFOZVdPeCNBgX6W7ThdrTUrGkpM", 
                username='gyrusdentatus', password='ou3-ynd-6tn-Kcb')
import logging
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('prawcore')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

sub = r.subreddit('NEO')

submission = r.submission(url="https://www.reddit.com/r/NEO/comments/7e8cz5/daily_discussion_november_20th_2017/")

submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)

submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    for second_level_comment in top_level_comment.replies:
        print(second_level_comment.body)

submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    print(comment.body)    

