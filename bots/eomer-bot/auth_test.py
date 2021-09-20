import praw

reddit = praw.Reddit(
    client_id="XA_-N_nhk_TFMBgW_4am0g",
    client_secret="QwYgUjACX2ozx8L11_GBRw7_40WqAg",
    password="Google235",
    user_agent="eomer-bot by u/jimbot13",
    username="jimbot13",
)

print(reddit.user.me())