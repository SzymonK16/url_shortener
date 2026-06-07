import re
import json
from datetime import datetime
from confluent_kafka import Producer

ban_words = ['python','java','c++','c','rust']
producer = Producer({'bootstrap.servers': 'kafka:9092'})

def send_word_to_kafka(word, full_url):
    event = {
        "event_type": "BANNED_WORD_DETECTED",
        "banned_word": word,
        "url": full_url,
        "timestamp": datetime.now().isoformat()
    }


    producer.produce(
        topic='banned_urls_logs',
        value=json.dumps(event).encode('utf-8')
    )

    producer.poll(0)

def check_word_in_url(url):

    url_str = str(url).lower()
    url_words = re.split(r'\W+', url_str)

    for word in url_words:
        if word in ban_words:
            send_word_to_kafka(word, url_str)
            producer.flush()

            
