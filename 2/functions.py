from decimal import Decimal

def processing(input):
    input_lst = []
    count = 0
    for i in range(len(input)):
        if input[i] == '(':
            input_lst.append(input[i])
            count = 0
        elif input[i] == ')':
            input_lst.append(input[i])
            count = 0
        elif input[i] == '/':
            input_lst.append(input[i])
            count = 0
        elif input[i] == '*':
            input_lst.append(input[i])
            count = 0
        elif input[i] == '+':
            input_lst.append(input[i])
            count = 0
        elif input[i] == '-':
            input_lst.append(input[i])
            count = 0
        elif count == 0:
            input_lst.append(input[i])
            count += 1
        elif count > 0:
            temp = input_lst[len(input_lst)-1] + input[i]
            input_lst.pop()
            input_lst.append(temp)
            count += 1
    return input_lst

def preparation(str):
    for i in range(len(str)):
        if '/' in str:
            str = calculation(str, '/')
        elif '*' in str:
            str = calculation(str, '*')
        else:
            for i in str:
                if i == '+':
                    str = calculation(str, '+')
                    break
                elif i == '-':
                    str = calculation(str, '-')
                    break
    return str

def calculation(input_str, symbol):
    if symbol in input_str:
            temp = input_str.index(symbol)
            num1 = Decimal(input_str[temp - 1])
            num2 = Decimal(input_str[temp + 1])
            if symbol == '/':
                result = num1 / num2
            elif symbol == '*':
                result = num1 * num2
            elif symbol == '+':
                result = num1 + num2
            elif symbol == '-':
                result = num1 - num2
            input_str[temp - 1] = str(result)
            input_str.pop(temp)
            input_str.pop(temp)
    return input_str

def calc(tmp):
    input = str(tmp)
    input_lst = processing(input)

    count_brackets = 0
    index_in_brackets = ['']
    data_in_brackets = []
    data_collection = []
    count = 0

    for i in input_lst:
        if i == '(':
            count_brackets += 1
    if count_brackets > 0:
        for i in range(count_brackets):
            for i in input_lst:
                if input_lst[count] == '(':
                    index_in_brackets.pop()
                    index_in_brackets.append(count)
                elif input_lst[count] == ')':
                    index_in_brackets.append(count)
                    break
                count += 1
            for i in range(index_in_brackets[0]+1, index_in_brackets[1]):
                data_in_brackets.append(input_lst[i])
            result_in_brackets = list(preparation(data_in_brackets))
            for i in range(index_in_brackets[0]):
                data_collection.append(input_lst[i])
            data_collection.append(result_in_brackets[0])
            for i in range(index_in_brackets[1]+1, len(input_lst)):
                data_collection.append(input_lst[i])
            input_lst = data_collection
            index_in_brackets = ['']
            data_in_brackets = []
            data_collection = []
            count = 0

        result_lst = list(preparation(input_lst))
        result_for_return = Decimal(result_lst[0])

    else:
        preparation(input_lst)
        result_for_return = Decimal(input_lst[0])
    
    return result_for_return