#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import json
import random


class UserAgent():


    @staticmethod
    def get_random():

        with open('models/user_agent/user-agents.json') as file:
            user_agents = json.load(file)

        return random.choice(user_agents)
