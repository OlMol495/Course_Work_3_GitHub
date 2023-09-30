import os
import json
from datetime import datetime

def load_data(op_f):
    if not os.path.exists(op_f):
        return print("No data of transactions found")
    with open(op_f, 'r', encoding="utf-8") as f:
        full_data = json.load(f)
        return full_data

def load_executed(file):
    executed_list = []
    for f in file:
        if f["state"] == "EXECUTED":
            executed_list.append(f)
    return executed_list

tl = [{"id": 4949, "date": "2019-08-26T10:50:58.294041"}, {"id": 4969, "date": "2018-08-26T10:50:58.294041"},{"id": 4049, "date": "2020-08-26T10:50:58.294041"}]

def sort_by_date(raw_data):
    for d in raw_data:
        d["date"] = datetime.strptime(d["date"], '%Y-%m-%dT%H:%M:%S.%f').date()
    sorted_list = sorted(raw_data, key=lambda d: d["date"], reverse=True)
    return sorted_list

def five_recent_trns(list):
    return list[:5]





















