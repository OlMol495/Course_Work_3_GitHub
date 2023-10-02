import pytest


@pytest.fixture
def test_data():
    return [
        {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount":
            {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации",
        "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"},
        {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount":
            {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод со счета на счет",
         "from": "Счет 44812258784861134719", "to": "Счет 74489636417521191160"},
        {"id": 214024827, "state": "EXECUTED", "date": "2018-12-20T16:43:26.929246", "operationAmount": {
            "amount": "70946.18", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации",
         "from": "Счет 10848359769870775355", "to": "Счет 21969751544412966366"},
        {"id": 522357576, "state": "EXECUTED", "date": "2019-07-12T20:41:47.882230", "operationAmount": {
            "amount": "51463.70", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации",
         "from": "Счет 48894435694657014368", "to": "Счет 38976430693692818358"},
        {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916", "operationAmount": {
            "amount": "56883.54", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод с карты на карту",
         "from": "Visa Classic 6831982476737658", "to": "Visa Platinum 8990922113665229"},
        {"id": 596171168, "state": "EXECUTED", "date": "2018-07-11T02:26:18.671407", "operationAmount": {
            "amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Открытие вклада",
         "to": "Счет 72082042523231456215"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "operationAmount": {
            "amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации",
         "from": "Visa Platinum 1246377376343588", "to": "Счет 14211924144426031657"}
    ]

def test_data_2():
    return [
        {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount":
            {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации",
        "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689", "operationAmount": {
            "amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации",
         "from": "Visa Platinum 1246377376343588", "to": "Счет 14211924144426031657"}
    ]