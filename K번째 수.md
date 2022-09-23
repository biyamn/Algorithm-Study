# K번째 수

문제url: 강의 자체 교재

푼 날짜: 2022.9.23

# 문제

<img src="강의문제Image\k번째 수.png" alt="k번째 수 문제 이미지">

# 내 풀이

```python
T = int(input())
ans = []

# 단순히 T번 반복한다는 코드라서 이름 없는 변수 `_` 사용
for _ in range(T):
	# 네 개의 숫자를 각각 N, s, e, k로 받아오기
  N, s, e, k = map(int, input().split())
	# N개의 숫자들을 numbers라는 리스트에 담기
  numbers = list(map(int, input().split()))
	# s번째부터 e번째까지의 요소를 슬라이스해서 numbers_slice 리스트에 반환
  numbers_slice = numbers[s-1:e]
	# 오름차순
  numbers_slice.sort(reverse=False)
	# numbers_slice 리스트에서 k번째 요소 뽑아서 ans 리스트에 넣기
  ans.append(numbers_slice[k-1])

# 하나씩 뽑아서 인덱스와 함께 반환
for i in range(len(ans)):
  print(f'#{i+1}', ans[i])
```

# 결과

성공했다!

![%EC%BA%A1%EC%B2%98](https://user-images.githubusercontent.com/101965666/191985137-1f8cd371-b519-452a-903e-1875cc3475cd.png)


# 다른 풀이

sort()가 오름차순인 걸 방금 알았다! 그래서 내가 한 것처럼 따로 sort(reverse=False)라고 조건을 주지 않아도 된다.

```python
T = int(input())

for t in range(T):
  n, s, e, k = map(int, input().split())
  a = list(map(int, input().split()))
  a = a[s-1:e]
  # 조건을 주지 않아도 오름차순
  a.sort()
  print("#%d %d" %(t+1, a[k-1]))
```