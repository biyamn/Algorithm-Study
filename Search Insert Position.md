# Search Insert Position

level: #EASY
문제url: https://leetcode.com/problems/search-insert-position/
푼 날짜: 2022.8.2

# 문제

[https://leetcode.com/problems/search-insert-position/](https://leetcode.com/problems/search-insert-position/)

# 내 코드

이진탐색을 거의 처음 접한 상태라서 **우선 이진탐색 코드를 찾아봤다.** 하지만, 이건 이분탐색을 통해 target이 어느 인덱스에 위치하는지를 구하는 코드였다. **(이미 리스트에 존재하는 target의 인덱스를 구하는 것)**

고민해봤지만 결국 문제의 의도인 어느 위치에 target이 존재해야 하는지를 구하는 코드는 작성하지 못했다. **(리스트에 target이 없는 상태에서 만약 들어간다면 어느 인덱스에 있어야 하는지를 구하는 것)**

```python
# 이진탐색은 O(log N)의 성능을 가진다
# 일반적인 이진탐색 코드

def binary_search(target, nums):
  start = 0
  end = len(nums) - 1

  while start <= end:
    mid = (start + end) // 2 # 1
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      start = mid + 1
    else:
      end = mid - 1

nums = [1,3,5,6]
target = 7

print(binary_search(target, nums))
```

# 다른 코드

엥 왜… 내가 쓴 코드랑 똑같은 거지??? 다른점이 딱하나 있는데 `return start`였다. 저건 무슨 의미일까… 

스터디에서 디버깅하며 열심히 토론한 결과, 알아냈다.

1. start와 end는 모두 인덱스이다.
2. while에서 target과 nums[mid]를 비교해 start와 end를 조정하여 움직이다가 start가 end보다 커지는 순간 while문을 빠져나오며 그때의 start값을 반환한다.
3. 이때의 start값이 최종적으로 target이 위치할 인덱스이다.

```python
def searchInsert(nums, target):
  start = 0
  end = len(nums) - 1
  
  while start <= end:
    mid = (start + end)
    if nums[mid] == target:
      return mid
    elif target > nums[mid]:
      start = mid + 1
    else:
      end = mid - 1
  
	# **이부분!!!**
  **return start**

nums = [1,3,5,6]
target = 7

print(searchInsert(nums, target))
```