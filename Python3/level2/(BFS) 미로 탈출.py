from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    for r in range(n):
        for c in range(m):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                end = (r, c)

    def bfs(start_pos, end_pos):
        q = deque([(start_pos[0], start_pos[1], 0)])
        visited = set()   # 문제에서 같은 곳을 여러번 반복해도 된다고 해도 최단거리를 구해야하기 때문에 반복 허용 X!
        
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        while q:
            x, y, cost = q.popleft()

            if (x,y) in visited:
                continue
            visited.add((x,y))
            
            if (x, y) == end_pos:
                return cost

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visited and maps[nx][ny] != 'X':
                    q.append((nx, ny, cost + 1))
        
        return -1

    # 1단계: S -> L
    time_to_lever = bfs(start, lever)
    if time_to_lever == -1:
        return -1

    # 2단계: L -> E
    time_to_end = bfs(lever, end)
    if time_to_end == -1:
        return -1

    return time_to_lever + time_to_end
