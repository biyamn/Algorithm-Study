# 학급 회장(JS)

날짜: 2022년 10월 19일

문제url: 강의 자체 교재

# 문제

<img src="강의문제Image\학급 회장.png" alt="학급 회장 문제 이미지">

# 내 코드

```python
N = int(input())
score = input()

candidate = ['A', 'B', 'C', 'D', 'E']
res = []

# res에 A, B, C, D, E가 각각 몇번 들어가있는지 저장
for i in candidate:
  res.append(score.count(i))

# 가장 큰 수를 찾아 그걸 candidate의 인덱스로 넣어서 최빈값을 찾기
print(candidate[res.index(max(res))])
```