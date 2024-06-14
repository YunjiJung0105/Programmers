import math
def solution(fees, records):
    records.sort(key = lambda x: x.split(' ')[1])
    
    all = {}
    while len(records) >= 2:
        car1 = records[0].split(' ')[1]
        car2 = records[1].split(' ')[1]
        state1 = records[0].split(' ')[2]
        state2 = records[1].split(' ')[2]
        
        if car1 not in all.keys():
            all[car1] = 0
            
        if car1 == car2 and state1 == 'IN' and state2 == 'OUT':
            in_time = int(records[0].split(' ')[0].split(':')[0]) * 60 + int(records[0].split(' ')[0].split(':')[1]) 
            out_time = int(records[1].split(' ')[0].split(':')[0]) * 60 + int(records[1].split(' ')[0].split(':')[1]) 
            
            all[car1] += (out_time - in_time)
            records.pop(0)
            records.pop(0)
            
        else: # only 'IN'
            in_time = int(records[0].split(' ')[0].split(':')[0]) * 60 + int(records[0].split(' ')[0].split(':')[1]) 
            out_time = 23 * 60 + 59
            
            all[car1] += (out_time - in_time)
            records.pop(0)
        
        
    if records:
        car1 = records[0].split(' ')[1]
        if car1 not in all.keys():
            all[car1] = 0
            
        in_time = int(records[0].split(' ')[0].split(':')[0]) * 60 + int(records[0].split(' ')[0].split(':')[1]) 
        out_time = 23 * 60 + 59

        all[car1] += (out_time - in_time)
        records.pop(0)


    answer = []

    for i in all:
        if all[i] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((all[i]-fees[0])/fees[2]) * fees[3])
    
    return answer
