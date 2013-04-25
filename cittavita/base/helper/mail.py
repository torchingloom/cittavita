# -*- coding: utf-8 -*-

from django import template
from django.contrib.sites.models import Site, get_current_site
from django.core.mail.message import EmailMessage
from settings import EMAIL_DEFAULT_FROM
from django.contrib.sites.models import Site
import re

class ToUsers(object):
    recipients = None
    tpl = None
    from_email = EMAIL_DEFAULT_FROM
    context_vars = {}

    def __init__(self, recipients=None, tpl=None, from_email=None, context_vars=None):
        self.set_recipients(recipients)
        self.set_template(tpl)
        self.set_from_email(from_email)
        self.set_context_vars(context_vars)

    def set_recipients(self, recipients=None):
        self.recipients = recipients

    def set_template(self, tpl=None):
        self.message_tpl = tpl

    def set_context_vars(self, context_vars={}):
        if context_vars:
            self.context_vars = context_vars

    def set_from_email(self, from_email=None):
        if from_email:
            self.from_email = from_email

    def prepare_message(self, resipient=None):
        context_vars = self.context_vars
        context_vars['recipient'] = resipient
        context_vars['site'] = Site.objects.get_current()
        raise BaseException(context_vars)
        str = template.loader.get_template('mail_templates/%s.html' % (self.message_tpl)).render(template.Context(context_vars))
        return {'subject': re.sub(r'.*SUBJECT\[\[\[(.*?)\]\]\].*', r'\1', str, flags=re.DOTALL), 'body': re.sub(r'.*BODY\[\[\[(.*?)\]\]\].*', r'\1', str, flags=re.DOTALL)}

    def send(self):
        for recipient in self.recipients:
            msg = self.prepare_message(recipient)
            msg = EmailMessage(msg['subject'], msg['body'], self.from_email, [recipient.email,],)
            msg.content_subtype = 'html'
            msg.send()



