import praw
import pprint

reddit = praw.Reddit(client_id='removed',
                     client_secret='removed',
                     user_agent='removed')

print(reddit.read_only)

# for submission in reddit.subreddit('learnpython').top(limit=10):
#     print(submission.title)

# for submission in reddit.subreddit('learnpython').top(limit=1):
#     print(submission)
#     for top_level_comment in submission.comments:

        # print(submission.title)
        # print(submission.selftext)
        # print(submission.score)
        # pprint.pprint(top_level_comment.body)

# for submission in reddit.subreddits.search_by_name("toast"):
#     print(submission.title)
#
#     sub_reddit = submission.title
#     for comments in reddit.subreddit(sub_reddit).top(limit=10):
#         for top_level_comment in sub_reddit.comments:
#             print(sub_reddit.title)
#             pprint.pprint(top_level_comment.body)

# for submission in reddit.subreddit('all').stream.submissions():
#     print(submission.title)


for submission in reddit.subreddits.search("removed"):
    sub_reddit = str(submission)
    print(f'Sub-reddit name: {sub_reddit}')
    for comments in reddit.subreddit(sub_reddit).top(limit=10):
        print(comments.title)
    print("\n\n\n")