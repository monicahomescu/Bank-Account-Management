#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import copy
import random
from datetime import date


def check_day(day):
    '''
    Checks if day is an integer between 1 and 30, otherwise raises exception.
    :param day: day to check
    :return: -
    '''
    if not str(day).isnumeric():
        raise ValueError('Day should be of type integer!')
    if int(day) < 1 or int(day) > 30:
        raise ValueError('Day should be between 1 and 30!')


def check_amount(amount):
    '''
    Checks if amount is a positive integer, otherwise raises exception.
    :param amount: amount to check
    :return: -
    '''
    if not str(amount).isnumeric():
        raise ValueError('Amount should be of type integer!')
    if int(amount) < 0:
        raise ValueError('Amount should be positive!')


def check_type(type):
    '''
    Checks if type is -in- or -out-, otherwise raises exception.
    :param type:
    :return:
    '''
    if type != 'in' and type != 'out':
        raise ValueError('Type should be in or out!')


def create_transaction(day, amount, type, description):
    '''
    Creates a new transaction.
    :param day: day to use
    :param amount: amount to use
    :param type: type to use
    :param description: description to use
    :return: dictionary that represents a transaction
    '''
    return {'day': day, 'amount': amount, 'type': type, 'description': description}


def get_day(transaction):
    return transaction['day']


def get_amount(transaction):
    return transaction['amount']


def get_type(transaction):
    return transaction['type']


def get_description(transaction):
    return transaction['description']


def set_day(transaction, day):
    transaction['day'] = day


def set_amount(transaction, amount):
    transaction['amount'] = amount


def set_type(transaction, type):
    transaction['type'] = type


def set_description(transaction, description):
    transaction['description'] = description


def to_string(transaction):
    '''
    Transforms a transaction to a string form.
    :param transaction: transaction to convert
    :return: string formed by transaction
    '''
    return 'day: ' + str(get_day(transaction)) + '   amount: ' + str(get_amount(transaction)) + '   type: ' \
           + str(get_type(transaction)) + '   description: ' + str(get_description(transaction))


def startup_transactions():
    '''
    Generates 10 random transactions for program startup.
    :return: list of transactions generated
    '''
    transactions = []
    types = ['in', 'out']
    descriptions = ['pizza', 'salary', 'coffee', 'jeans', 'ticket', 'groceries', 'gift', 'bills', 'shirt', 'shoes',
                    'soda', 'water', 'bread', 'internet', 'candle']
    for i in range(0, 10):
        day = str(random.randint(1, 30))
        amount = str(random.randint(1, 100))
        type = str(random.choice(types))
        description = str(random.choice(descriptions))
        transaction = create_transaction(day, amount, type, description)
        transactions.append(transaction)
    return transactions


def split_text(text):
    '''
    Splits text into command (first word) and parameters (rest of words).
    :param text: text to split
    :return: command and parameters
    '''
    words = text.strip().split(' ', 1)
    command = words[0].strip()
    if len(words) == 1:
        parameters = ''
    else:
        parameters = words[1].strip()
    return command, parameters


def add_to_current_day(transactions, amount, type, description, history):
    '''
    Adds a new transaction to the current day.
    :param transactions: list of current transactions
    :param amount: amount to add
    :param type: type to add
    :param description: description to add
    :param history: history of changes to add to
    :return: -
    '''
    today = date.today()
    day = today.strftime("%d")
    transaction = create_transaction(day, amount, type, description)
    cpy = copy.deepcopy(transactions)
    history.append(cpy)
    transactions.append(transaction)


def insert_to_day(transactions, day, amount, type, description, history):
    '''
    Inserts a new transaction to a day.
    :param transactions: list of current transactions
    :param day: day to add to
    :param amount: amount to add
    :param type: type to add
    :param description: description to add
    :param history: history of changes to add to
    :return: -
    '''
    transaction = create_transaction(day, amount, type, description)
    cpy = copy.deepcopy(transactions)
    history.append(cpy)
    transactions.append(transaction)


def remove_from_day(transactions, day, history):
    '''
    Removes all transactions from a day.
    :param transactions: list of current transactions
    :param day: day to remove from
    :param history: history of changes to add to
    :return: -
    '''
    found = False
    cpy = copy.deepcopy(transactions)
    index = 0
    while index < len(transactions):
        if get_day(transactions[index]) == day:
            transactions.remove(transactions[index])
            found = True
        else:
            index += 1
    if found:
        history.append(cpy)
    else:
        raise ValueError('There are no transactions for that day!')


def remove_between_start_and_end(transactions, start, end, history):
    '''
    Removes all transactions between two days.
    :param transactions: list of current transactions
    :param start: start day
    :param end: end day
    :param history: history of changes to add to
    :return: -
    '''
    found = False
    cpy = copy.deepcopy(transactions)
    index = 0
    while index < len(transactions):
        if int(start) <= int(get_day(transactions[index])) <= int(end):
            transactions.remove(transactions[index])
            found = True
        else:
            index += 1
    if found:
        history.append(cpy)
    else:
        raise ValueError('There are no transactions between those days!')


def remove_from_type(transactions, type, history):
    '''
    Removes all transactions having a certain type.
    :param transactions: list of current transactions
    :param type: type to remove
    :param history: history of changes to add to
    :return: -
    '''
    found = False
    cpy = copy.deepcopy(transactions)
    index = 0
    while index < len(transactions):
        if get_type(transactions[index]) == type:
            transactions.remove(transactions[index])
            found = True
        else:
            index += 1
    if found:
        history.append(cpy)
    else:
        raise ValueError('There are no transactions of that type!')


def replace_amount(transactions, day, type, description, amount, history):
    '''
    Replaces a transaction's amount with a new amount.
    :param transactions: list of current transactions
    :param day: day to search for
    :param type: type to search for
    :param description: description to search for
    :param amount: amount to replace with
    :param history: history of changes to add to
    :return: -
    '''
    found = False
    cpy = copy.deepcopy(transactions)
    for transaction in transactions:
        if get_day(transaction) == day and get_type(transaction) == type and get_description(
                transaction) == description:
            history.append(cpy)
            set_amount(transaction, amount)
            found = True
            break
    if not found:
        raise ValueError('The transaction does not exist!')


def list_all(transactions):
    '''
    Lists all transactions.
    :param transactions: list of current transactions
    :return: list of all transactions
    '''
    if len(transactions) == 0:
        raise ValueError('There are no transactions!')
    else:
        return transactions


def list_type(transactions, type):
    '''
    Lists all transactions having a certain type.
    :param transactions: list of current transactions
    :param type: type to search for
    :return: list of transactions found
    '''
    new_transactions = []
    for transaction in transactions:
        if get_type(transaction) == type:
            new_transactions.append(transaction)
    if len(new_transactions) == 0:
        raise ValueError('There are no transactions of that type!')
    else:
        return new_transactions


def list_condition_amount(transactions, condition, amount):
    '''
    Lists all transactions that are smaller, equal or greater than a certain amount.
    :param transactions: list of current transactions
    :param condition: condition to take into account
    :param amount: amount to take into account
    :return: list of transactions found
    '''
    new_transactions = []
    for transaction in transactions:
        if condition == "<" and int(get_amount(transaction)) < int(amount):
            new_transactions.append(transaction)
        elif condition == "=" and get_amount(transaction) == amount:
            new_transactions.append(transaction)
        elif condition == ">" and int(get_amount(transaction)) > int(amount):
            new_transactions.append(transaction)
    if len(new_transactions) == 0:
        raise ValueError('There are no transactions that satisfy the condition!')
    else:
        return new_transactions


def list_balance_day(transactions, day):
    '''
    Lists the balance for a certain day.
    :param transactions: list of current transactions
    :param day: day to calculate balance for
    :return: calculated balance
    '''
    found = False
    balance_in = 0
    balance_out = 0
    for transaction in transactions:
        if get_day(transaction) == day:
            found = True
            if get_type(transaction) == 'in':
                balance_in += int(get_amount(transaction))
            else:
                balance_out += int(get_amount(transaction))
    if not found:
        raise ValueError('There are no transactions for that day!')
    else:
        return balance_in - balance_out


def filter_type(transactions, type, history):
    '''
    Filters out all transactions that do not have a certain type.
    :param transactions: list of current transactions
    :param type: type to keep
    :param history: history of changes to add to
    :return: -
    '''
    found = False
    cpy = copy.deepcopy(transactions)
    index = 0
    while index < len(transactions):
        if get_type(transactions[index]) != type:
            transactions.remove(transactions[index])
            found = True
        else:
            index += 1
    if found:
        history.append(cpy)
    else:
        raise ValueError('The transactions are already filtered!')


def filter_type_and_amount(transactions, type, amount, history):
    '''
    Filters out all transactions that do not have a certain type and an amount smaller than a certain amount.
    :param transactions: list of current transactions
    :param type: type to keep
    :param amount: amount to take into account
    :param history: history of changes to add to
    :return: -
    '''
    found = False
    cpy = copy.deepcopy(transactions)
    index = 0
    while index < len(transactions):
        if get_type(transactions[index]) != type or int(get_amount(transactions[index])) >= int(amount):
            transactions.remove(transactions[index])
            found = True
        else:
            index += 1
    if found:
        history.append(cpy)
    else:
        raise ValueError('The transactions are already filtered!')


def handle_add(transactions, parameters, history):
    '''
    Handles the add command.
    :param transactions: list of current transactions
    :param parameters: parameters for add command
    :param history: history of changes to add to
    :return: -
    '''
    parameters = parameters.split()
    if len(parameters) != 3:
        raise ValueError('Invalid number of parameters for add command!')
    amount = parameters[0]
    check_amount(amount)
    type = parameters[1]
    check_type(type)
    description = parameters[2]
    add_to_current_day(transactions, amount, type, description, history)


def handle_insert(transactions, parameters, history):
    '''
    Handles the insert command.
    :param transactions: list of current transactions
    :param parameters: parameters for insert command
    :param history: history of changes to add to
    :return: -
    '''
    parameters = parameters.split()
    if len(parameters) != 4:
        raise ValueError('Invalid number of parameters for insert command!')
    day = parameters[0]
    check_day(day)
    amount = parameters[1]
    check_amount(amount)
    type = parameters[2]
    check_type(type)
    description = parameters[3]
    insert_to_day(transactions, day, amount, type, description, history)


def handle_remove(transactions, parameters, history):
    '''
    Handles the remove command.
    :param transactions: list of current transactions
    :param parameters: parameters for remove command
    :param history: history of changes to add to
    :return: -
    '''
    parameters = parameters.split()
    if len(parameters) == 1:
        if str(parameters[0]).isnumeric():
            day = parameters[0]
            check_day(day)
            remove_from_day(transactions, day, history)
        else:
            type = parameters[0]
            check_type(type)
            remove_from_type(transactions, type, history)
    elif len(parameters) == 3:
        if parameters[1] == 'to':
            start = parameters[0]
            check_day(start)
            end = parameters[2]
            check_day(end)
            if int(start) > int(end):
                raise ValueError('Start day should be smaller than end day!')
            remove_between_start_and_end(transactions, start, end, history)
        else:
            raise ValueError('-Remove- command should contain -to- keyword!')
    else:
        raise ValueError('Invalid number of parameters for any remove command!')


def handle_replace(transactions, parameters, history):
    '''
    Handles the remove command.
    :param transactions: list of current transactions
    :param parameters: parameters for remove command
    :param history: history of changes to add to
    :return: -
    '''
    parameters = parameters.split()
    if len(parameters) != 5:
        raise ValueError('Invalid number of parameters for replace command!')
    if parameters[3] == 'with':
        day = parameters[0]
        check_day(day)
        type = parameters[1]
        check_type(type)
        description = parameters[2]
        amount = parameters[4]
        check_amount(amount)
        replace_amount(transactions, day, type, description, amount, history)
    else:
        raise ValueError('-Replace- command should contain -with- keyword!')


def handle_filter(transactions, parameters, history):
    '''
    Handles the filter command.
    :param transactions: list of current transactions
    :param parameters: parameters for filter command
    :param history: history of changes to add to
    :return: -
    '''
    parameters = parameters.split()
    if len(parameters) == 1:
        type = parameters[0]
        check_type(type)
        filter_type(transactions, type, history)
    elif len(parameters) == 2:
        type = parameters[0]
        check_type(type)
        amount = parameters[1]
        check_amount(amount)
        filter_type_and_amount(transactions, type, amount, history)
    else:
        raise ValueError('Invalid number of parameters for any filter command!')


def handle_undo(transactions, parameters, history):
    '''
    Handles the undo command.
    :param transactions: list of current transactions
    :param parameters: parameters for undo command
    :param history: history of changes to add to
    :return: -
    '''
    parameters = parameters.split()
    if len(history) == 0:
        raise ValueError('Cannot undo anymore!')
    else:
        if len(parameters) == 0:
            transactions.clear()
            old_transactions = history.pop()
            for transaction in old_transactions:
                transactions.append(transaction)
        else:
            raise ValueError('Invalid number of parameters for undo command!')


def test_add_to_current_day():
    transactions = []
    amount = '23'
    type = 'out'
    description = 'pizza'
    history = []
    add_to_current_day(transactions, amount, type, description, history)
    assert len(transactions) == 1
    today = date.today()
    day = str(today.strftime("%d"))
    assert transactions[0] == {'day': day, 'amount': '23', 'type': 'out', 'description': 'pizza'}
    assert len(history) == 1
    assert history[0] == []


def test_insert_to_day():
    transactions = []
    day = '1'
    amount = '23'
    type = 'out'
    description = 'pizza'
    history = []
    insert_to_day(transactions, day, amount, type, description, history)
    assert len(transactions) == 1
    assert transactions[0] == {'day': '1', 'amount': '23', 'type': 'out', 'description': 'pizza'}
    assert len(history) == 1
    assert history[0] == []


def test_remove_from_day():
    transactions = [{'day': '1', 'amount': '23', 'type': 'out', 'description': 'pizza'}]
    day = '1'
    history = []
    remove_from_day(transactions, day, history)
    assert len(transactions) == 0
    assert len(history) == 1
    assert history[0] == [{'day': '1', 'amount': '23', 'type': 'out', 'description': 'pizza'}]


def test_remove_between_start_and_end():
    transactions = [{'day': '7', 'amount': '23', 'type': 'out', 'description': 'pizza'},
                    {'day': '4', 'amount': '23', 'type': 'out', 'description': 'pizza'},
                    {'day': '1', 'amount': '23', 'type': 'out', 'description': 'pizza'}]
    start = '1'
    end = '5'
    history = []
    remove_between_start_and_end(transactions, start, end, history)
    assert len(transactions) == 1
    assert transactions[0] == {'day': '7', 'amount': '23', 'type': 'out', 'description': 'pizza'}
    assert len(history) == 1
    assert history[0] == [{'day': '7', 'amount': '23', 'type': 'out', 'description': 'pizza'},
                    {'day': '4', 'amount': '23', 'type': 'out', 'description': 'pizza'},
                    {'day': '1', 'amount': '23', 'type': 'out', 'description': 'pizza'}]


def test_remove_from_type():
    transactions = [{'day': '1', 'amount': '23', 'type': 'out', 'description': 'pizza'}]
    type = 'out'
    history = []
    remove_from_type(transactions, type, history)
    assert len(transactions) == 0
    assert len(history) == 1
    assert history[0] == [{'day': '1', 'amount': '23', 'type': 'out', 'description': 'pizza'}]


def test_replace_amount():
    transactions = [{'day': '1', 'amount': '23', 'type': 'out', 'description': 'pizza'}]
    day = '1'
    type = 'out'
    description = 'pizza'
    amount = '25'
    history = []
    replace_amount(transactions, day, type, description, amount, history)
    assert len(transactions) == 1
    assert transactions[0] == {'day': '1', 'amount': '25', 'type': 'out', 'description': 'pizza'}
    assert len(history) == 1
    assert history[0] == [{'day': '1', 'amount': '23', 'type': 'out', 'description': 'pizza'}]


def tests():
    test_add_to_current_day()
    test_insert_to_day()
    test_remove_from_day()
    test_remove_between_start_and_end()
    test_remove_from_type()
    test_replace_amount()
