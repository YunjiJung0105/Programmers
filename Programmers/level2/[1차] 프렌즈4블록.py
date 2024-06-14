def solution(m, n, board):
    board = [list(b) for b in board]
    visited = []
    
    while True:
        curr_vis = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1] and board[i][j] != '':
                    possible = [[i,j], [i,j+1], [i+1,j], [i+1,j+1]]
                    for p in possible:
                        if p not in curr_vis:
                            curr_vis.append(p)

        if curr_vis == []:
            break
            
        visited += curr_vis
        for v in curr_vis:
            board[v[0]][v[1]] = ''


        board = [list(x) for x in zip(*board)]   # transpose
        for i in range(n):
            cnt = board[i].count('')
            board[i] = [''] * cnt + list(''.join(board[i]))
        board = [list(x) for x in zip(*board)]


    return len(visited)
