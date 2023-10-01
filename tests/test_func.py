from src import func


def test_load_data():
    """checking that result is list type"""
    file_path = "..\operations.json"
    data = func.load_data(file_path)
    assert isinstance(data, list)


def test_load_data_nofile():
    """checking correct return with wrong file path"""
    file_path = "new_file.json"
    assert func.load_data(file_path) == print("No data found")


def test_load_executed(test_data):
    """checking that filter works for key word by length of result list"""
    data = func.load_executed(test_data)
    assert len(data) == 6


def test_load_executed_empty():
    """checking filter result with key word absent"""
    file = [{"id": 857, "from": "Master"}, {"id": 91872, "to": "Visa"}]
    assert func.load_executed(file) == []


def test_sort_by_date(test_data):
    """checking date sorting by date of first item in list"""
    data = func.sort_by_date(test_data)
    assert data[0]["date"] == "2019-08-26T10:50:58.294041"


def test_five_recent_trns(test_data):
    """checking length of result list"""
    data = func.five_recent_trns(test_data)
    assert len(data) == 5


def test_print_stats_empty_list():
    """checking that with empty list input result will be None"""
    data = []
    assert func.print_stats(data) == None

def test_print_stats(test_data):
    """"""
    data = []
    assert func.print_stats(data) == None

