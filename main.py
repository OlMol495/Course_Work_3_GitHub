from src import func


def main():
    json_path = "operations.json"
    transaction_list = func.load_data(json_path)
    exec_filtered = func.load_executed(transaction_list)
    date_sorted = func.sort_by_date(exec_filtered)
    recent_five = func.five_recent_trns(date_sorted)
    print_stats = func.print_stats(recent_five)
    for i in print_stats:
        print(i)



if __name__=="__main__":
    main()

