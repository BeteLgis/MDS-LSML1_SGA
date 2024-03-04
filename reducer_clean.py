import sys


prev_session = (None, None)
prev_page = None
err = False

for line in sys.stdin:
    user_id, session_id, timestamp, event_type, event_page = line.strip().split()
    
    if prev_session != (user_id, session_id):
        prev_page = None
        err = False
    prev_session = (user_id, session_id)
    
    if not err and 'error' in event_type:
        err = True
    
    if not err:
        if prev_page is None or prev_page != event_page:
            print('\t'.join([user_id, session_id, timestamp, event_page]))
        prev_page = event_page
