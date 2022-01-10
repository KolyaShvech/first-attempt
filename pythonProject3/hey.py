# import account
# rate = int(input('Введите процентную ставку: '))
# period = int(input('Введите количетсво месяцев: '))
# money = int(input('Введите сумму: '))
#
# result = account.calculate_income(rate, period, money)
# print('Параметры счета: \n', 'Сумма', money, '\n', 'ставка:', rate, '\n', 'Период: ', period, '\n', 'Сумма на счете в конце периода: ', result)

# import account as acc
# rate = int(input('Введите процентную ставку: '))
# period = int(input('Введите количетсво месяцев: '))
# money = int(input('Введите сумму: '))
# result = acc.calculate_income(rate, money, period)
# print('Параметры счета: \n', 'Сумма', money, '\n', 'ставка:', rate, '\n', 'Период: ', period, '\n', 'Сумма на счете в конце периода: ', result)

#
# from account import calculate_income
#
# rate = int(input('Введите процентную ставку: '))
# period = int(input('Введите количетсво месяцев: '))
# money = int(input('Введите сумму: '))
# result = calculate_income(rate, money, period)
# print('Параметры счета: \n', 'Сумма', money, '\n', 'ставка:', rate, '\n', 'Период: ', period, '\n', 'Сумма на счете в конце периода: ', result)
#
# def calculate_income(rate, money, month):
#     if money <= 0:
#         return 0
#
#     for i in range(1, month + 1):
#         money = round(money + money * rate/ 100/ 12, 2)
#     return money
# def main():
#     rate = 10
#     money = 100000
#     period = 12
#     result = calculate_income(rate, money, period)
#     print('Параметры счета: \n', 'Сумма', money, '\n', 'ставка:', rate, '\n', 'Период: ', period, '\n', 'Сумма на счете в конце периода: ', result)
# if __name__ == '__main__':
#     main()
