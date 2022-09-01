from collections import deque

n, m = map(int, input().split())

# graph = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

'''
4 6
101111
101010
101011
111011
'''

def bfs(x, y):
  # 이동할 네 가지 방향 정의(상, 하, 좌, 우)
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]
  # 큐 구현을 위해 deque 라이브러리 사용
  # 처음에 queue는 deque([(0, 0)])이 된다
  queue = deque()
  queue.append((x, y))
  # 큐가 빌 때까지 반복하기
  while queue: 
    # x = 0, y = 0
    x, y = queue.popleft()
    # 현재 위치에서 4가지 방향으로의 위치 확인(range(4)를 통해)
    # nx, ny는 new x, new y를 뜻함
    # i=0일 때 nx=0, ny=1 / graph[nx][ny]=1
    # i=1일 때 nx=0, ny=-1 / graph[nx][ny]=x
    # i=2일 때 nx=-1, ny=0 / graph[nx][ny]=x
    # i=3일 때 nx=1, ny=0 / graph[nx][ny]=0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 미로찾기 공간을 벗어난 경우 무시
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      # 벽인 경우 무시(0이 벽이고 1이 지나갈 수 있는 길)
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      # 지나간 거리를 누적하여 더함
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

# print(bfs(시작 위치))
print(bfs(0, 0))