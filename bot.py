#!/usr/bin/python
import praw
import pdb
import re
import os
from scrapper_stock import stock_data

reddit = praw.Reddit('bot1')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

with open("company_list.txt", "r") as f:
    company_list = f.read()
    company_list = company_list.split("\n")
    company_list = list(filter(None, company_list))

subreddit = reddit.subreddit('test')

for submission in subreddit.hot(limit=10):
    if submission.id not in posts_replied_to:
        for stock in company_list:
            if re.search(stock, submission.title, re.IGNORECASE):
                stock_info = stock_data(stock)
                reply = 'Stock Price: ' + stock_info['stock_price'] + 
                        '52 week high: ' + stock_info['high_52_week']
                submission.reply(reply)
                print("Bot replying to : ", submission.title)
                posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")


