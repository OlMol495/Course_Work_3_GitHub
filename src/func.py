import os
import json
from datetime import datetime

def load_data(op_f):
    """downloads json file"""
    if not os.path.exists(op_f):
        return print("No data found")
    with open(op_f, 'r', encoding="utf-8") as f:
        full_data = json.load(f)
        return full_data

def load_executed(file):
    """filters list for records with Executed status"""
    executed_list = []
    for f in file:
        if "state" not in f.keys():
            continue
        else:
            if f["state"] == "EXECUTED":
                executed_list.append(f)
    return executed_list

def sort_by_date(raw_data):
    """sort the list by the date of a transaction in reverse order"""
    return sorted(raw_data, key=lambda d: d["date"], reverse=True)

def five_recent_trns(tr_list):
    """takes slice of five first items in list"""
    return tr_list[:5]

def print_stats(filted_list):
    """print information for user about five recent transactions
    with date, type of transaction, from, to, amount and currency"""
    for i in filted_list:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i["description"]
        if "from" not in i.keys():
            num_from = ""
            name_from = ""
        else:
            from_sep = i["from"].split()
            num_list = []
            word_list = []
            for d in from_sep:
                if d.isnumeric():
                    num_list.append(d)
                else:
                    word_list.append(d)
            if len(num_list[0]) == 16:
                card_num = num_list[0]. replace(num_list[0][6:12], "******")
                num_from = " ".join([card_num[:4], card_num[4:8], card_num[8:12], card_num[12:]])
            else:
                num_from = num_list[0].replace(num_list[0][:-4], "**")
            name_from = " ".join(word_list)
        to_sep = i["to"].split()
        to_num_list = []
        to_word_list = []
        for t in to_sep:
            if t.isnumeric():
                to_num_list.append(t)
            else:
                to_word_list.append(t)
        if len(to_num_list[0]) != 16:
            num_to = to_num_list[0].replace(to_num_list[0][:-4], "**")
        else:
            to_card_num = to_num_list[0]. replace(to_num_list[0][6:12], "******")
            num_to = " ".join([to_card_num[:4], to_card_num[4:8], to_card_num[8:12], to_card_num[12:]])
        name_to = " ".join(to_word_list)
        amount = i["operationAmount"]["amount"]
        currency = i["operationAmount"]["currency"]["name"]
        print(f"{date} {description}\n"
              f"{name_from} {num_from} => {name_to} {num_to}\n"
              f"{amount} {currency}\n")





























