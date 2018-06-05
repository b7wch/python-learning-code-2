#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/27
from collections import deque


class actor_sche(object):
    def __init__(self):
        self._actor_msg = deque()
        self._actors = dict()

    def new_actor(self, name, actor):
        self._actor_msg.append((actor, None))
        self._actors[name] = actor

    def send(self, name, msg):
        actor = self._actors.get(name)
        if actor:
            self._actor_msg.append((actor, msg))

    def run(self):
        while self._actor_msg:
            actor, msg = self._actor_msg.popleft()
            try:
                actor.send(msg)
            except Exception, e:
                print e


if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print('Got:', msg)


    def counter(sche):
        while True:
            n = yield
            if n == 0:
                break
            sche.send('printer', n)
            sche.send('counter', n - 1)


    sche1 = actor_sche()
    sche1.new_actor('printer', printer())
    sche1.new_actor('counter', counter(sche1))
    sche1.send('counter', 10)
    sche1.run()
