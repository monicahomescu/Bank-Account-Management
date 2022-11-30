#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
from functions import *


def print_transactions(transactions):
    for transaction in transactions:
        print(to_string(transaction))


def handle_list(transactions, parameters, history):
    parameters = parameters.split()
    if len(parameters) == 0:
        print_transactions(list_all(transactions))
    elif len(parameters) == 1:
        type = parameters[0]
        check_type(type)
        print_transactions(list_type(transactions, type))
    elif len(parameters) == 2:
        if parameters[0] == '<' or parameters[0] == '=' or parameters[0] == '>':
            condition = parameters[0]
            amount = parameters[1]
            check_amount(amount)
            print_transactions(list_condition_amount(transactions, condition, amount))
        elif parameters[0] == 'balance':
            day = parameters[1]
            check_day(day)
            print(list_balance_day(transactions, day))
        else:
            raise ValueError('-List- command should contain -[<|=|>]- or -balance- keyword!')
    else:
        raise ValueError('Invalid number of parameters for any list command!')


def print_menu():
    print("\n     add <value> <type> <description>")
    print("     insert <day> <value> <type> <description>")
    print("     remove <day>")
    print("     remove <start day> to <end day>")
    print("     remove <type>")
    print("     replace <day> <type> <description> with <value>")
    print("     list")
    print("     list <type>")
    print("     list [ < | = | > ] <value>")
    print("     list balance <day>")
    print("     filter <type>")
    print("     filter <type> <value>")
    print("     undo\n")


def start_program():
    transactions = startup_transactions()
    commands = {'add': handle_add, 'insert': handle_insert, 'remove': handle_remove, 'replace': handle_replace,
                'list': handle_list, 'filter': handle_filter, 'undo': handle_undo}
    history = []
    while True:
        print_menu()
        text = input("input: ")
        command, parameters = split_text(text)
        if command in commands:
            try:
                commands[command](transactions, parameters, history)
            except ValueError as ve:
                print(str(ve))
        elif command == 'exit':
            break
        else:
            print("Invalid command!")
