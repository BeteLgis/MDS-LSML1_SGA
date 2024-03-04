import sys


prev_route = None
count = 0

for line in sys.stdin:
    route = line.strip()
    
    if prev_route is not None and prev_route != route:
        print('\t'.join([prev_route, str(count)]))
        count = 0
    
    count += 1
    prev_route = route

print('\t'.join([route, str(count)]))
