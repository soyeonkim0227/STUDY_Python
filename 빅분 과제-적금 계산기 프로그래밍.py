r = 0.024
n = 12

money = int(input("월급을 입력하세요: "))

interest = 0
for i in reversed(range(1, n + 1)):
    interest += money * r * i/12
    result = interest

print("월 납입 금액: "f'{money:,}')
print("원금 합계: "f'{money*n:,}')
print("세전 이자: "f'{result:,.0f}')
all_result = result * 0.154
print("이자 과세: -"f'{all_result:,.0f}')
print("세후 수령액: "f'{money * n + result - all_result:,.0f}')