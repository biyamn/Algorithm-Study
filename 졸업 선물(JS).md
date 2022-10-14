# 졸업 선물(JS)

날짜: 2022년 10월 14일

문제url: 강의 자체 교재

# 문제
스터디에서 JS 알고리즘 강의를 듣는 분의 문제이다. 그분이 문제를 해설할 차례이기 때문에 그분이 푸는 문제를 스터디원 모두 같이 풀어보아야 한다.

<img src="강의문제Image\졸업 선물.png" alt="졸업 선물 문제 이미지">

# 내 풀이

```python
N, M = map(int, input().split())

# 선생님이 내야 하는 금액을 구하기(가격/2 + 배송비)
arr = []
for i in range(N):
  price, delivery_fee = map(int, input().split())
  sum = price//2 + delivery_fee
  arr.append(sum)
arr.sort()

# 예산 M에서 작은 값부터 하나씩 빼가며 몇 번 뺄 수 있는지 구하지
cnt = 0
for i in arr:
  M -= i
  if M >= 0:
    cnt += 1
  else:
    break

print(cnt)
```

# 다른 풀이

```python
def solution(M, products):
    answer = 0
    N = len(products)
		# 가격과 배송비를 더해서 나온 총 금액별로 정렬함(오름차순)
    products.sort(key = lambda p : p[0] + p[1])
    for i in range(N):
				# 남은 돈 = 총 예산 - 할인된 가격 + 배송비
        left_money = M - (products[i][0] / 2 + products[i][1])
				# 할인된 상품은 이미 삼! 카운트를 해줌!
        cnt = 1
        for j in range(N):
            total = products[j][0] + products[j][1]
            if j != i and total > left_money:
                break
						# 남은 예산이 총 금액보다 크거나 같으면(돈이 남아서 사줄 수 있으면)
            if j != i and total <= left_money:
								# 사줌
                left_money -= total
								# 사줬다고 표시함
                cnt += 1
				# cnt가 answer보다 커지면(사줄 수 있는 인간의 최고 기록 경신!) answer를 새로 갱신
        answer = max(answer,cnt)

    return answer

param = {
    "m": 28,
    "arr": [
      [6, 6], # 이 상품이 할인받는다 해보고
      [2, 2], # 이 상품이 할인받는다 해보고
      [4, 3], # ... 다해보고
      [4, 5],
      [10, 3],
    ],
}
param1 = {
    "m": 41,
    "arr": [[8, 6],[2, 2],[4, 3],[4, 5],[12, 1]]
}
param2 = {
    "m": 596,
    "arr": [[6, 331],[4, 251],[8, 675],[5, 214],[10, 735],[5, 996],[9, 609],[9, 371],[8, 377],
      [5, 707],[7, 907],[6, 433],[9, 737],[8, 796],[4, 265],[3, 484],[8, 488],[8, 191],[9, 232],[4, 195]
    ],
}
param3 = {
    "m": 41,
    "arr": [[8, 6],[2, 2],[4, 3],[4, 5],[12, 1]],
}

print(solution(param["m"], param["arr"]))
print(solution(param1["m"], param1["arr"]))
print(solution(param2["m"], param2["arr"]))
print(solution(param3["m"], param3["arr"]))
```