# Top K Frequent Elements

level: #Medium

문제url: https://leetcode.com/problems/top-k-frequent-elements/

완료 여부: O

푼 날짜: 2022.5.10

# 문제

[https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

# 내 풀이

내 풀이는 시간 초과가 떠서 실패했다. 

```python
# 시간 초과!
# nums = [1,1,1,2,2,3]
# k = 2
def TopKElement(nums, k):

	# {1: 3, 2: 2, 3: 1}
	nums_dict = {}
  for num in nums:
	  nums_dict[num] = nums.count(num)
     
  # [1, 2, 3]
  nums_sorted = sorted(nums_dict, key=lambda x : nums_dict[x], reverse=True)
    
	# [1, 2]
	return nums_sorted[:k]
    
# 시간초과를 어떻게 해결할 수 있을까... count나 sorted에서 시간초과가 난 것 같은데..
```

1. count함수로 각 숫자가 몇 번 있는지 세어 딕셔너리에 저장했다.
2. sorted함수로 각 value순서대로 정렬하여 가장 많이 등장한 순서대로 정렬하였다.
3. 리스트 슬라이싱으로 k개의 문자를 리턴하였다.

→ 데이터의 양이 적은 input은 잘 처리되었지만, **데이터의 양이 너무 많으면 시간초과가 뜨며** 처리되지 않았다. 결국 시간초과로 실패했는데, count함수와 sorted함수를 쓰지 않고 숫자를 세고 정렬할 방법이 도무지 떠오르지 않아 다른 풀이를 보게 되었다.

---

# 다른 풀이

파이썬의 Counter를 써서 해결할 수 있었다! 처음 봤는데, 정말로.. 유용한 모듈이었다. 

일단 Counter(nums)로 객체를 만들고, .most_common(k)로  k개만큼 많은 순서대로 가져와 리턴했다. 위의 내 코드에 비하면 짧고 간결한 코드였다. (심지어 시간초과도 나지 않는!!)

```python
def topKFrequent(nums, k):
	# Counter({1: 3, 2: 2, 3: 1})
  cnt = Counter(nums)

	# [(1, 3), (2, 2)] cnt에서 k개만큼 많은 순서대로 가져온다
  most_common_k = cnt.most_common(k)

	# for문으로, for num in most_common_k: return i[0]과 같은 의미
  return [num[0] for num in most_common_k]
```

그런데 위의 코드를 아래처럼 아주아주 간단한 버전으로 만들 수도 있었다. 와우..파이썬 최고...

```python
# 위의 코드를 이렇게도 만들 수 있다!!!!!
def topKFrequent(nums, k):
	return [x[0] for x in Counter(nums).most_common(k)]
```

---

# 파이썬 Counter란? 한번 알아보자.

파이썬 collections 모듈의 Counter 클래스는 데이터의 개수를 셀 때 쓰기 좋다고 한다.

예를 들면 “Hello World” 알파벳의 개수를 세어보자.

Counter를 사용하지 않으면 이렇게 긴 코드를 써야 하지만,

```python
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

countLetters('hello world'))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

Counter를 사용하면 이렇게 한줄로 만들 수 있다.

```python
from collections import Counter
Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

그리고 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 most_common이라는 유용한 메서드를 제공한다.(Top K Frequent Elements도 사용함)

```python
from collections import Counter

Counter('hello world').most_common(k) # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
Counter('hello world').most_common(1) # [('l', 3)] 1을 넘기면 가장 개수가 많은 k개의 데이터를 얻는다.
```

참고: [https://www.daleseo.com/python-collections-counter/](https://www.daleseo.com/python-collections-counter/)
