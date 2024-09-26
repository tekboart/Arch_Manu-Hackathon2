import requests
import json
from pprint import pprint
import os
import pandas as pd
import numpy as np

# TODO: Add logging??? (too much of a headache)

# TODO: at the end turn each section/task into a different file/module, so keep only main/high_lvl parts in this file.

# TODO: get node_list & edge_list from the server
# XXX: take the "node-light" version

response = requests.get(
    url="https://archmanucox.pythonanywhere.com/bimverse/nodes-light.json/"
)

# response_unserial = json.loads(response.json())
# response_unserial = response.json().load

# pprint(response.json()[0])
# print(response_unserial)

data = os.path.join("data", "")
addr_node_list = data + "node_list.json"

with open(addr_node_list, 'w') as f:
    json.dump(response.json(), f)

# TODO: make the node_list & edge_list (for networkx/igraph)

df = pd.DataFrame(columns=response.json()[0].keys())
#  print(df)

for item in response.json():
    #  print(item.__class__)
    #  print(item)
    #  df['id'] = item.get['id']
    #  df['label'] = item.get['name']
    df.loc[item.get('id')] = item.values()
    #  for key in item.keys():
        #  df.concat(item.values(), axis=0)
        #  df.loc[item.get['id']] = []


df = df.rename({'name': 'label'}, axis=1)
df = df.drop('id', axis=1)

print(df)
df.to_csv(data + 'node_list.csv')

#TODO: create a graph (e.g., networkX), BOn server requests



# TODO: do SNA analysis (e.g., centralities) on the network

# TODO: Visualize the restulsts (e.g., node_size: betweenness)
# TODO: export each of them to a ".png" file


