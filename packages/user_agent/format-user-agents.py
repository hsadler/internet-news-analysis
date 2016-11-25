
import json


with open('user-agents.txt') as file:
    content = file.readlines()


user_agents = []

for line in content:
    user_agents.append(line[1: -2])


print json.dumps(user_agents)
