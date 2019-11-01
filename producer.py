from time import sleep
from json import dumps
from kafka import KafkaProducer
from hackernews import HackerNews

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
hn=HackerNews()
latest_id=0
last_10=hn.new_stories(limit=10)
# print(last_10)
print("Will publish last 10 stories initially, then will incrementally publish new story as it is posted on site.")
for item in last_10:
    text=item.title
    id=item.item_id
    if(id>latest_id):
        latest_id=id
    data={id:text}
    print('publishing {}'.format(data))
    producer.send('story',value=data)
    print('\n')
    # sleep(3)

while(True):

    story=hn.new_stories(limit=1)
    if(len(story)==0 or story[0].item_id<=latest_id):
        continue
    else:
        curr_story=story[0]
        text=curr_story.title
        id=curr_story.item_id
        data={id:text}
        latest_id=id
        print('publishing {}'.format(data))
        producer.send('story',value=data)
        print('\n')
    # sleep(5)
