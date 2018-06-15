#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import create_app, db, cli
from app.models import User, Post, Notification, Message

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post, 'Message':message, 'Notification': Notification}

app.run(host='0.0.0.0')