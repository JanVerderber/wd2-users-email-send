from handlers.base import BaseHandler
from models.topic import Topic
from models.user import Users
from google.appengine.api import mail
import datetime


class SendEmailUsersCron(BaseHandler):
    def get(self):
        topics = Topic.query(Topic.deleted == False, Topic.updated < datetime.datetime.now() - datetime.timedelta(hours=24)).fetch()
        users123 = Users.query().fetch()

        for user in users123:
            mail.send_mail(sender="server@gmail.com",
                           to=user,
                           subject="New topics",
                           body="""New topic {0}""".format(topics))



