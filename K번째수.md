# K번째수

level: #1
문제url: https://programmers.co.kr/learn/courses/30/lessons/42748
완료 여부: O
푼 날짜: 2022.6.30

# 문제

[https://programmers.co.kr/learn/courses/30/lessons/42748](https://programmers.co.kr/learn/courses/30/lessons/42748)

# 내 풀이

```python
# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    ans_list = []
		# commands에서 [2, 5, 3]부터 for문으로 하나씩 빼옴
    for i in commands:
				# answer는 array의 i[0]-1번째부터 i[1]번째까지의 수임
				# [5, 2, 6, 3]
        answer = array[i[0]-1:i[1]]

				# .sort()로 정렬시킴
				# [2, 3, 5, 6]
        answer.sort()
				
				# 정렬한 리스트에서 answer[i[2]-1]번째를 구해서 빈 ans_list에 쌓음. 
				# 이걸 for문으로 끝까지 반복함
        ans_list.append(answer[i[2]-1])

		# [5, 6, 3]
    return ans_list
```

# 다른 풀이

```jsx
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```

```python
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
```