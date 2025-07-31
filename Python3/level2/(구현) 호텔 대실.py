def solution(book_time):
    new_book_time = []
    for time in book_time:
        a = int(time[0].split(':')[0]) * 60 + int(time[0].split(':')[1])
        b = int(time[1].split(':')[0]) * 60 + int(time[1].split(':')[1]) + 10
        new_book_time.append([a,b])
    new_book_time.sort()
        
    rooms = [new_book_time[0]]
    for i in range(1, len(new_book_time)):
        count = 0
        for r in rooms:
            if new_book_time[i][0] >= r[-1]:
                r += new_book_time[i]
                count += 1
                break
        
        if count==0:
            rooms.append(new_book_time[i])
 
    return len(rooms)
