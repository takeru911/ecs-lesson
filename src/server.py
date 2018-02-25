#!/usr/bin/env python
# coding:utf-8

import sys
import CallbackServer

def callback(query):
    if len(query) > 2:
      return str(int(query['param1'][0]) + int(query['param2'][0]))
    return "cant calc."

if __name__ == '__main__':
    port = sys.argv[1]
    CallbackServer.start(port, callback)
