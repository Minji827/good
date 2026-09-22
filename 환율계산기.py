def exchange_money(amount, exchange_rate):
    result = amount * exchange_rate
    return result

amount = float(input("환전할 금액을 입력하세요: "))
exchange_rate = float(input("환율을 입력하세요: "))

result = exchange_money(amount, exchange_rate)

print("환전 결과: ", result)
