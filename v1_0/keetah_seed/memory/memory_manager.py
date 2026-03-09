import json
import os

LTM_FILE = "memory/ltm.json"

def load_memory():

    if not os.path.exists(LTM_FILE):
        return {}

    with open(LTM_FILE,"r") as f:
        return json.load(f)


def save_memory(data):

    with open(LTM_FILE,"w") as f:
        json.dump(data,f,indent=2)