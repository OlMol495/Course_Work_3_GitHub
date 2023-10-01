import pytest
import os
import json
from datetime import datetime
from src import func

def test_load_data():
    file_path = "..\operations.json"
    data = func.load_data(file_path)
    assert isinstance(data, list)

def test_load_data_nofile():
    file_path = "new_file.json"
    assert func.load_data(file_path) == print("No data found")

def test_load_executed(test_data):
    data = func.load_executed(test_data)
    assert len(data) == 6

def test_load_executed_empty():
    file = [{"id": 857, "from": "Master"}, {"id": 91872, "to": "Visa"}]
    assert func.load_executed(file) == []

def test_sort_by_date(test_data):
    data = func.sort_by_date(test_data)
    assert date[0]["date"] == "2019-08-26T10:50:58.294041"




