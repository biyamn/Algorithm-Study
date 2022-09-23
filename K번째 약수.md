# K번째 약수

문제url: 강의 자체 교재

푼 날짜: 2022.9.23

# 문제

<img src="강의문제Image/k번째 약수.png" alt="k번째 약수 문제 이미지">

# 내 풀이

```python
N, K = map(int, input().split(' '))

factor = []

# 약수인지 확인
for i in range(1, N+1):
  if N % i == 0:
		# 약수라면 factor라는 리스트에 추가
    factor.append(i)

# factor 리스트의 길이(약수의 개수)가 K보다 작으면 -1 반환
if len(factor) < K:
  print(-1)

# 답 반환
else: 
  print(factor[K-1])
```

# 결과

정답!

![%EC%BA%A1%EC%B2%98](https://user-images.githubusercontent.com/101965666/191985137-1f8cd371-b519-452a-903e-1875cc3475cd.png)


# 다른 풀이

for문을 다 돌았는데도 없으면 -1을 반환한다는 깔끔한 코드이다!

리스트를 만들지 않고 cnt라는 변수를 만들어서 증가시켜가며 풀었다. 

```
N, K = map(int, input().split())

cnt = 0
for i in range(1, N+1):
  if N % i == 0:
    cnt += 1
  if cnt == K:
    print(i)
    break
else:
  print(-1)
```