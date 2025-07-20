import random
import time
import datetime
import uuid
import logging

FIXED_MESSAGE = "This is something I advise on. Click here to find out more: https://tbg.link/housing"

NAMES = [
    "R. TBG Legal", "Govericks Advisory", "Legal Insight – TBG",
    "Gov+TBG Policy", "TBG Client Team"
]

DELAY_RANGE = (2.0, 4.0)

logging.basicConfig(
    filename="linkedin_log.txt",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def generate_comment():
    name = random.choice(NAMES)
    comment_text = FIXED_MESSAGE
    return name, comment_text

def post_comment_to_post(post_title, topic_tag):
    name, comment_text = generate_comment()
    message_id = str(uuid.uuid4())[:8]
    timestamp = datetime.datetime.utcnow().isoformat()

    print(f"\nPosting to LinkedIn post: “{post_title}”")
    print(f"Name: {name}")
    print(f"Comment: {comment_text}")
    print(f"Message ID: {message_id}")

    time.sleep(random.uniform(*DELAY_RANGE))

    log_entry = f"{timestamp} | linkedin | {topic_tag} | {post_title} | {name} | {message_id}"
    logging.info(log_entry)

if _name_ == "_main_":
    curated_posts = [
        {"title": "New Planning Law Update – July 2025", "topic": "property"},
        {"title": "Small Business Legal Advice Trends", "topic": "SMEs"},
        {"title": "UK Policy Shifts in Urban Development", "topic": "housing"}
    ]

    for post in curated_posts:
        post_comment_to_post(post["title"], post["topic"])
