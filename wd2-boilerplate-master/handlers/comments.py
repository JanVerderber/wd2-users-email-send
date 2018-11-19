from handlers.base import BaseHandler
from google.appengine.api import users
from models.comment import Comment
from models.topic import Topic
from utils.decorators import validate_csrf
from google.appengine.api import mail


class CommentAdd(BaseHandler):
    @validate_csrf
    def post(self, topic_id):
        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        text = self.request.get("comment-text")
        topic = Topic.get_by_id(int(topic_id))

        comment = Comment(content=text, author_email=user.email(), topic_id=topic.key.id(), topic_title=topic.title)
        comment.put()

        mail.send_mail(
            subject="New comment on your topic",
            body="""Your topic {0} received a new comment.
            Click <a href="http://localhost:8080/topic/{1}">this link</a> to see topic
            """.format(
                topic.title,
                topic.key.id()
            ),

            to=topic.author_email,
            sender="jan.verderber@gmail.com"

        )

        return self.redirect_to("topic-details", topic_id=topic.key.id())
