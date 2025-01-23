import sys

n = int(sys.stdin.readline())

status = {}

for _ in range(n) :
    name, action = sys.stdin.readline().split()
    
    if action == 'leave' :
        if name in status :
            del status[name]
    else :
        status[name] = action
        
sorted_name = sorted(status.keys(), reverse=True)

for name in sorted_name:
    print(name)