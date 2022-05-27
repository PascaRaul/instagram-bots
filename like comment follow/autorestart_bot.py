#!/usr/bin/env python3
# coding: utf-8
from subprocess import Popen

filename = 'final_bot_all.py'
while True:
    print("Starting " + filename)
    p = Popen("python " + filename, shell=True)
    p.wait()
