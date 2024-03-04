import sys


prev_session = (None, None)
prev_page = None
err = False
route = []

for line in sys.stdin:
    user_id, session_id, timestamp, event_type, event_page = line.strip().split()
    
    if prev_session != (user_id, session_id):
        prev_page = None
        err = False
        if len(route) > 0:
            print('-'.join(route))
        route = []
    prev_session = (user_id, session_id)
    
    if not err and 'error' in event_type:
        err = True
    
    if not err:
        if prev_page is None or prev_page != event_page:
            route.append(event_page)
        prev_page = event_page

if len(route) > 0:
    print('-'.join(route))
