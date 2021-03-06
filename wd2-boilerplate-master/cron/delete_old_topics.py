from handlers.base import BaseHandler
from models.topic import Topic
import datetime

class DeleteOldTopicsCron(BaseHandler):
    def get(self):
        topics = Topic.query(Topic.deleted == True, Topic.updated < datetime.datetime.now() - datetime.timedelta(minutes=10)).fetch()

        for topic in topics:
            topic.key.delete()
