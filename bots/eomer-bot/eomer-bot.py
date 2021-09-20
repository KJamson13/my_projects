#!/usr/bin/env python3


import praw
from praw.models import MoreComments
import json
import random

with open("eomer-bot-credentials.json", "r") as credential_details:
    creds = json.loads(credential_details.read())
    credential_details.close()


    reddit = praw.Reddit(
    user_agent = creds.get("user_agent"),
    client_id = creds.get("client_id"),
    client_secret = creds.get("client_secret"),
    username = creds.get("username"),
    password = creds.get("password"),
)
    
    
with open("eomer_quotes.json", "r") as quote_file:
    quotes = json.loads(quote_file.read())
    quote_file.close()


BOT_NAME = "eomer-bot"

lotrmemes = reddit.subreddit("lotrmemes")
bottest = reddit.subreddit("BotTestingPlace")

def has_replied(comment):
    
    comment.refresh()
    for reply in comment.replies:
        if reply.author and reply.author.name == BOT_NAME:
            return True

    return False

def check_triggers(quote, comment):

    if quote.get("any", None):
        for trig in quote["triggers"]:
            if trig in comment:
                return True
    else:
        for trig in quote["triggers"]:
            if trig not in comment:
                return False
        
        return True

for comment in lotrmemes.stream.comments():

    if isinstance(comment, MoreComments):
        continue

    if comment.author and comment.author.name == BOT_NAME:
        continue
    
    if has_replied(comment):
        print("found already replied")
        continue

    com_clean = comment.body.lower()

    for quote in quotes:

        if check_triggers(quote, com_clean):
            reply = random.choice(quote["replies"])
            if "<<NAME>>" in reply:
                name = (
                    comment.author.name if comment.author is not None else "My King"
                )
                reply = reply.replace("<<NAME>>", name)

            comment.reply(reply)
            print("I wrote something")
            break

   