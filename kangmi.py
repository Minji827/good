def withdraw(balance, amount):
    if amount > balance:
        print("잔액보다 많이 출금할 수 없습니다")
    return balance
    balance = balance - amount
    return balance