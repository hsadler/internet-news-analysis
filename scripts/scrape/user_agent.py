#!/usr/local/bin/python

import json
import random


def get_rand_user_agent():

    with open('scripts/scrape/user-agents.json') as file:
        user_agents = json.load(file)

    return random.choice(user_agents)

