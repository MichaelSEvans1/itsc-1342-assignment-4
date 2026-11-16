# Michael Evans - Assignment 4

def check_session(idle_minutes, max_idle=30):
    # Evaluate idle time against max_idle threshold
    if idle_minutes >= max_idle:
        return "SESSION_EXPIRED"
    return "SESSION_ACTIVE"
