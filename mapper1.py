import sys

_ = sys.stdin.readline().strip() # remove the header

for line in sys.stdin:
    user_id, session_id, event_type, event_page, timestamp = line.strip().split()
    print('\t'.join([user_id, session_id, timestamp, event_type, event_page]))
