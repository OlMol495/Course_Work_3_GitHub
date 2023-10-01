from src import func

json_path = "operations.json"
def main():
    transaction_list = func.load_data(json_path)
    exec_filtered = func.load_executed(transaction_list)
    date_sorted = func.sort_by_date(exec_filtered)
    recent_five = func.five_recent_trns(date_sorted)
    result_for_user = func.print_stats(recent_five)
    return result_for_user


if __name__=="__main__":
    main()

