import tweepy
import json

env_dict = {}
with open('env.json') as data_file:
    env_dict = json.load(data_file)

auth = tweepy.OAuthHandler(env_dict['CONSUMER_KEY'], env_dict['CONSUMER_SECRET'])
auth.set_access_token(env_dict['ACCESS_KEY'], env_dict['ACCESS_SECRET'])
api = tweepy.API(auth)
twelve_hours = 12*60*60
import time

import random
import os.path

def call_f():
    f = open('dir_to_lookup/files_to_lookup.txt', 'r')
    files = f.readlines()
    f.close()
    files = [f.strip() for f in files]
    while True:
        to_open = random.choice(files)
        fname = 'dir_to_lookup/' + to_open
        if os.path.isfile(fname):
            f = open(fname, 'r')
            break
    data = f.readlines()
    title = data[0].strip()
    while True:
        to_send = random.choice(data[2:]).strip()
        if len(to_send) < 280 - 3 - len(title) - 9 and len(to_send) > 5:
            break
    return to_send + " : " + title + " - by bot"


while True:
    to_write = call_f()
    print (to_write)
    api.update_status(to_write)
    time.sleep(twelve_hours)



