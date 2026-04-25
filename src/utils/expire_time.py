from datetime import timedelta, datetime

def expire_time():

    _expire_time = datetime.now() + timedelta(minutes=5)
    return _expire_time