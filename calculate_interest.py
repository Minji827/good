def calculate_interest(balance, rate):
    interest = balance * rate
    
    # 계산된 이자를 바로 화면에 출력해줍니다!
    print("이자 금액은:", interest, "원이에요!")
    
    # 혹시 나중에 쓸 수도 있으니까 리턴도 그냥 남겨둘게요
    return interest

# 함수 써보기 (예시)
calculate_interest(1000000, 0.05)
