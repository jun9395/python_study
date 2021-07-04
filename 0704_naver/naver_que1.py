# 주문할 제품의 가격 prices
# 쿠폰별 할인율 discounts가 주어진다
# 모든 물건을 구입한다고 할 때, 가장 싸게 구매하는 값

def solution(prices, discounts):
    prices.sort(reverse=True)
    discounts.sort(reverse=True)

    sumvalue = 0
    for i in range(len(prices)):
        if i < len(discounts):
            sumvalue += round(prices[i] * (1 - 0.01 * discounts[i]))
        else:
            sumvalue += prices[i]
    return sumvalue


prices = [13000, 88000, 10000]
discounts = [30, 20]

print(solution(prices, discounts))