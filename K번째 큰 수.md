# K번째 큰 수

문제url: 강의 자체 교재

푼 날짜: 2022.9.26

# 문제

![%EC%BA%A1%EC%B2%98](https://user-images.githubusercontent.com/101965666/192219072-5176f61a-37a3-4bba-8ae9-17b17c8dd92f.png)

# 내 풀이

도대체 왜 틀렸는지 모르겠다. 중복을 포함한 값 N개에서 3개를 뽑아 그 합을 구한 후 내림차순으로 정렬하여 K번째 값을 출력하는 것이 아닌가??? 왜 답이랑 다르지?? 강의를 들어보기로 했다. 

```python
# 틀린 풀이

# itertools 라이브러리에서 combinations(조합) 임포트
from itertools import combinations

# 입력으로부터 N, K 받아오기
N, K = map(int, input().split())
# 입력된 숫자들 가져와서 numbers 리스트에 입력하기
numbers = list(map(int, input().split()))
# numbers 리스트에서 순서 상관없이 3개씩 뽑아서 numbers_combinations 리스트에 넣기
numbers_combinations = list(combinations(numbers, 3))
# 빈 리스트 lst 선언
lst = []
# for문을 돌며 (*, *, *) 형태로 3개씩 뽑인 수들을 더하여 lst 리스트에 각각 넣기
for i in numbers_combinations:
  lst.append(sum(i))
# 내림차순으로 정렬하기(큰 수부터 작은 수까지)
lst.sort(reverse=True)
# lst 리스트에서 K번째 수 출력하기(인덱스는 0부터 시작하므로 인덱스 K-1을 구해야 함)
print(lst[K-1])
```

→ ㅋㅋㅋㅋ문제를…제대로 안봤구나… 직접적으로 중복 값은 하나만 카운팅한다는 말은 없지만 25 25 23 23 22…에서 K가 3이면 `22` 라고 했는데… 그럼 중복인 25와 23은 한 번씩만 센다는 뜻이다. 이제 다시 풀어보자. 

이제는 성공했다!

```python
# 맞은 풀이

# itertools 라이브러리에서 combinations(조합) 임포트
from itertools import combinations
# 입력으로부터 N, K 받아오기
N, K = map(int, input().split())
# 입력된 숫자들 가져와서 numbers 리스트에 입력하기
numbers = list(map(int, input().split()))
# numbers 리스트에서 순서 상관없이 3개씩 뽑아서 numbers_combinations 리스트에 넣기
numbers_combinations = list(combinations(numbers, 3))
# 빈 리스트 lst 선언
lst = []
# for문을 돌며 (*, *, *) 형태로 뽑힌 튜플들(i)을 더하여(* + * + *) lst 리스트에 각각 넣기
for i in numbers_combinations:
  lst.append(sum(i))
# lst에서 중복을 제거하여 lst_set 리스트에 넣기
lst_set = list(set(lst))
# 내림차순으로 정렬하기(큰 수부터 작은 수까지)
lst_set.sort(reverse=True)
# lst 리스트에서 K번째 수 출력하기(인덱스는 0부터 시작하므로 인덱스 K-1을 구해야 함)
print(lst_set[K-1])
```

# 결과

![%EC%BA%A1%EC%B2%98](https://user-images.githubusercontent.com/101965666/191985137-1f8cd371-b519-452a-903e-1875cc3475cd.png)

# 다른 풀이

combinations 모듈을 사용하지 않고 직접 구현해서 풀었다. 

```python
N, K = map(int, input().split())
a = list(map(int, input().split()))
res = set()
# 각기 다른 수 3개를 뽑는 경우의 수
for i in range(N):
  for j in range(i+1, N):
    for m in range(j+1, N):
      res.add(a[i]+a[j]+a[m])
      
res = list(res)
res.sort(reverse=True)
print(res[K-1])
```

삼중 for문을 돌며 순서에 상관없이 3개의 값을 뽑는데, i가 인덱스 0에 있으면 j는 이와 위치가 겹치면 안되므로 i+1번째부터 뽑는다. m도 마찬가지로 i, j와 뽑는 위치가 겹치면 안되므로 j+1부터 뽑는다. 이를 코드로 구현한 것이 위의 삼중 for문이다. 

![%EC%A0%9C%EB%AA%A9_%EC%97%86%EC%9D%8C](https://user-images.githubusercontent.com/101965666/192219077-b99d8ad2-c9a0-4f55-8caf-7087bc148ca8.png)
