# 모든 아나그램 찾기(JS)

날짜: 2022년 10월 20일

문제url: 강의 자체 교재

# 문제

<img src="강의문제Image\모든 아나그램 찾기.png" alt="모든 아나그램 찾기 이미지">

# 내 코드

```python
# input1
bacaAacba
abc 
# output1: 3

# input2
abcabca
abc 
# output2: 5

# input3
bbacabcAbaabc
abc
# output3: 4
```

처음에는 아래와 같이 풀었다. 그런데 이렇게 하면 input1은 통과하는데 input2(내가 만듦)은 통과하지 않았다. 디버깅하면서 살펴보니, 만약에 abc가 문자열에 n번 들어가 있더라도 for i in S로는 하나만 잡고 끝나기 때문에 실제 output보다 적은 숫자가 나오는 것이었다. 수정해보기로 했다. 

```python
import itertools
import itertools
S = input()
T = list(input())

lst = list(map(''.join, itertools.permutations(T)))

cnt = 0
for i in lst:
  if i in S:
    cnt += 1

print(cnt)
```

오 아래와 같이 count() 내장함수를 썼더니 input2를 통과했다! 혹시 모르니까 input3를 만들어서 넣어보기로 했다. 

```python
import itertools
import itertools

S = input()
T = list(input())

# 입력받은 문자열 T를 섞어서 만들 수 있는 문자열 모두 구해서 lst에 담기
lst = list(map(''.join, itertools.permutations(T)))

# S라는 문자열에서 lst의 원소가 몇 개 들어있는지 count 함수로 세서 cnt에 담는다
cnt = 0
for i in lst:
  cnt += S.count(i)

print(cnt)

# input1
bacaAacba
abc 
# output1: 3

# input2
abcabca
abc 
# output2: 5

# input3
bbacabcAbaabc
abc
# output3: 4
```

→ input4도 통과! 맞는 것 같다!~