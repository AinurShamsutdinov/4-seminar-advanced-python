import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

# Введите ваше решение ниже


# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
# Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
def deposit(amount):
    dep_op: str
    if check_multiplicity(amount):
        global bank_account
        bank_account = bank_account + decimal.Decimal(amount)
        amount_str = remove_trailing_zeros(amount)
        bank_account_str = remove_trailing_zeros(bank_account)
        dep_op = f'Пополнение карты на {amount_str} у.е. Итого {bank_account_str} у.е.'
        operations.append(dep_op)
        global count
        count += 1


# Функция withdraw(amount) позволяет клиенту снимать средства со счета.
# Сумма снятия также должна быть кратной MULTIPLICITY. При снятии средств начисляется комиссия в процентах
# от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

# 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.',
# 'Недостаточно средств. Сумма с комиссией 3045.000 у.е. На карте 940 у.е.',
# 'Возьмите карту на которой 0 у.е.'
def withdraw(amount):
    draw_op: str
    amount = decimal.Decimal(amount)
    global bank_account
    check = check_multiplicity(amount)
    comission = decimal.Decimal(amount) * decimal.Decimal(PERCENT_REMOVAL)
    if comission < MIN_REMOVAL:
        comission = MIN_REMOVAL
    elif comission > MAX_REMOVAL:
        comission = MAX_REMOVAL
    remove = decimal.Decimal(amount + comission)
    if check and remove < bank_account:
        bank_account = bank_account - remove
        amount_str = remove_trailing_zeros(amount)
        comission_str = remove_trailing_zeros(comission)
        bank_account_str = remove_trailing_zeros(bank_account)
        draw_op = f'Снятие с карты {amount_str} у.е. Процент за снятие {comission_str} у.е.. Итого {bank_account_str} у.е.'
        operations.append(draw_op)
    elif remove > bank_account:
        remove_str = remove_trailing_zeros(remove)
        bank_account_str = remove_trailing_zeros(bank_account)
        draw_op = f'Недостаточно средств. Сумма с комиссией {remove_str} у.е. На карте {bank_account_str} у.е.'
        operations.append(draw_op)


# Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM,
# начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
def exit():
    global bank_account
    if bank_account > RICHNESS_SUM:
        rich_comission = decimal.Decimal(bank_account * RICHNESS_PERCENT)
        bank_account -= rich_comission
        rich_comission_str = remove_trailing_zeros(rich_comission)
        bank_account_str = remove_trailing_zeros(bank_account)
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {rich_comission_str} у.е. Итого {bank_account_str} у.е.')
    bank_account_str = remove_trailing_zeros(bank_account)
    operations.append(f'Возьмите карту на которой {bank_account_str} у.е.')


# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
# Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
def check_multiplicity(amount):
    if decimal.Decimal(amount) % decimal.Decimal(MULTIPLICITY) == 0:
        return True
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False


def remove_trailing_zeros(number):
    number_str = str(number)
    number_str = number_str.rstrip('0').rstrip('.') if '.' in number_str else number_str
    return decimal.Decimal(number) if '.' in number_str else int(number_str)




deposit(173)
withdraw(21)
exit()

print(operations)


# deposit(1000000000000000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()
#
# print(operations)


#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#deposit(1000)
#withdraw(200)
#exit()

#print(operations)


['Пополнение карты на 1000000000000000 у.е. Итого 1000000000000000 у.е.',
 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 999999999999770 у.е.',
 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 999999999999440 у.е.',
 'Пополнение карты на 500 у.е. Итого 999999999999940 у.е.',
 'Снятие с карты 3000 у.е. Процент за снятие 45.000 у.е.. Итого 999999999996895.000 у.е.',
 'Вычтен налог на богатство 0.1% в сумме 99999999999689.5000 у.е. Итого 899999999997205.5000 у.е.',
 'Возьмите карту на которой 899999999997205.5000 у.е.']
