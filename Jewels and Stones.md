# 보석과 돌

level: #EASY

문제url: https://leetcode.com/problems/jewels-and-stones

완료 여부: O

푼 날짜: 2022.4.30

# 문제

[https://leetcode.com/problems/jewels-and-stones](https://leetcode.com/problems/jewels-and-stones)

# 내 풀이

### 풀이1. 일반 풀이

jewels에 있는 글자와 stones에 있는 글자를 하나하나 비교하여(이중 for문) 비교하고, 같으면 cnt++하여 cnt를 정답으로 리턴했다. 

```python
class Solution:
    def numJewelsInStones(self, jewels, stones):
        cnt = 0
        for i in jewels:
          for j in stones:
            if i == j:
              cnt += 1
        return cnt
```

### 풀이2. 딕셔너리를 사용한 풀이

딕셔너리를 사용해서 풀어보려고 했는데, 딕셔너리끼리 비교하는 부분에서 막혀서 못풀었다. 

**<미완성된 내 풀이>**

```python
class Solution:
    def numJewelsInStones(self, jewels, stones):
        stones_dict = {}
        jewels_dict = {}

        for stone in stones:
          # {'a': 1, 'A': 2, 'b': 4}
          stones_dict[stone] = stones.count(stone)
          
        # {'a': 1, 'A': 1}
        for jewel in jewels:
          jewels_dict[jewel] = jewels.count(jewel)
```

**<완성된 내 풀이>**

1. stones에서는 stone만 세는건줄 알았고, stones에서 jewels를 세는 발상은 하지 못했다.
2. 어떤딕셔너리.values()를 쓸 생각을 못했다. 그리고 이를 sum()으로 합할 수 있는지도 몰랐다.
    - print(jewels_dict.values())라고 하면 dict_values([1, 2])이렇게 출력되어서, sum()을 하면 3이 출력됨

```python
class Solution:
  def numJewelsInStones(self, jewels, stones):
    stones_dict = {}
    jewels_dict = {}
    have_dict = {}

    for stone in stones:
      stones_dict[stone] = stones.count(stone)

    for jewel in jewels:
      jewels_dict[jewel] = jewels.count(jewel)

    for jewel in jewels:
      have_dict[jewel] = stones.count(jewel)

    return sum(have_dict.values())
```

# 다른 풀이

[https://deep-learning-study.tistory.com/356](https://deep-learning-study.tistory.com/356)

```python
class Solution:
    def numJewelsInStones(self, jewels, stones: str) -> int:
        return sum(s in jewels for s in stones)
```
