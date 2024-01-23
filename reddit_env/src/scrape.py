from kcu import kjson
from reddit_scraper import RedditScraper, PostType

def scrape(subs, num_posts):
    for sub in subs:
        posts = RedditScraper.get_posts(
                sub=sub, max_count=num_posts, 
                post_types=[PostType.Text], 
                include_nsfw=True)
        kjson.save(sub + '.json', [post.json for post in posts])

if __name__ == "__main__":
    subs = ['depression','bpd']

