import os
import pandas as pd
import tweepy

# 1. Load your Bearer Token from the environment
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
if not BEARER_TOKEN:
    raise RuntimeError(
        "Please set the TWITTER_BEARER_TOKEN environment variable before running this script."
    )

# 2. Authenticate
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# 3. Fetch tweets
query = "#privacy OR #security lang:en -is:retweet"
response = client.search_recent_tweets(
    query=query,
    max_results=100,
    tweet_fields=["text"]
)

# 4. Extract texts
texts = [tweet.text for tweet in response.data] if response.data else []

# 5. Save to CSV
out_path = os.path.join(os.getcwd(), 'data', 'raw_social_posts.csv')
pd.DataFrame({'text': texts}).to_csv(out_path, index=False)
print(f"Saved {len(texts)} tweets to {out_path}")
