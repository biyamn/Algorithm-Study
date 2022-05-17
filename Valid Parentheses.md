# Valid Parentheses

level: #EASY
문제url: https://leetcode.com/problems/valid-parentheses/
완료 여부: O
푼 날짜: 2022.5.14

# 문제

[https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

# 내 풀이

→ 틀렸다. 스택 개념을 모르고 풀었는데, 어려웠다. 맞게 푼 것 같은데 왜 틀렸는지는 추후 디버깅을 통해 알아보려고 한다.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        list_s = list(s)
        
        arr = [('(', ')'), ('[', ']'), ('{', '}')]
        trueOrFalse = []
        
        for k in range(len(list_s)//2):
            # ( [ {
            v = list_s[2*k]
            for i in arr:
                if v in i:
                    if list_s[2*k+1] == i[1]:
                        trueOrFalse.append('true')
                else:
                    trueOrFalse.append('false')
        
        if set(trueOrFalse) == {'true'}:
            return True
        else:
            return False
```

# 다른 풀이

스택의 개념을 몰라서 풀지 못했던 문제 같다.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # 홀수개면 짝이 맞지 않기 때문에 False를 반환
        if len(s) % 2 != 0:
            return False
        # dict에 열고 닫는 쌍들을 저장
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        # 받은 s값들에서 for문을 돌림
        for i in s:
            # i가 dict의 keys에 있으면? (keys = 여는 것들 - (, [, {))
            if i in dict.keys():
                # stack이라는 리스트에 i를 넣음
                stack.append(i)
            # i가 dict의 keys에 없으면?
            else:
                # 만약 스택이 빈 상태이면?
                if stack == []:
                    # False를 반환한다
                    return False
                # 스택에서 하나를 뺀다!
                a = stack.pop()
                # 만약에 dict[a](하나 뺀거)가 i와 다르면(닫는 것들이 다르면)
                # 예) if ')' != dict['(']
                if i!= dict[a]:
                    # False를 반환한다
                    return False
        # 다 빼고 났는데 빈 스택 리스트가 아니면 False를 반환하고 아니면 True를 반환한다
        return stack == []

k = Solution()
print(k.isValid('()[}'))
```