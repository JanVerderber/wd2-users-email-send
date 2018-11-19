#!/usr/bin/env python
import webapp2
from cron.delete_old_topics import DeleteOldTopicsCron
from cron.send_email_users import SendEmailUsersCron
from handlers.base import MainHandler, CookieAlertHandler
from handlers.comments import CommentAdd
from handlers.topics import TopicAdd, TopicDetails, TopicDelete


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic/<topic_id:\d+>', TopicDetails, name="topic-details"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAdd, name="comment-add"),
    webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDelete, name="topic-delete"),
    webapp2.Route('/cron/delete-old-topics', DeleteOldTopicsCron),
    webapp2.Route('/cron/send-email-users', SendEmailUsersCron)
], debug=True)
