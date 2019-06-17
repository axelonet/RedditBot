#!/usr/bin/python
import praw
import re
import random


reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pewdiepiesubmissions")

for comment in subreddit.stream.comments():
    print(comment.body)
    if comment.body == 'what?':
        marvin_reply = "You've never played Tuber Simulator before?"
        comment.reply(marvin_reply)
        print(marvin_reply)
