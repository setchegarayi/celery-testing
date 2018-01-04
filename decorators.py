from functools import wraps
import memcache
from hashlib import md5

class LoginError(Exception):
    """Base class for exceptions in this module."""
    pass

cache = memcache.Client([('127.0.0.1', 11211)])

def lock_on_task_error(timeout):
    def task_exc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            payload = (func.__name__ + str(args)).encode('utf-8')
            lock_id = md5(payload).hexdigest()
            acquire_lock = lambda: cache.add(lock_id, "true", timeout)
            release_lock = lambda: cache.delete(lock_id)
            if acquire_lock():
                try:
                    func(*args, **kwargs)
                except LoginError:
                    print("Login error")
                else:
                    release_lock()
                finally:
                    pass
            else:
                print("Locked")
        return wrapper
    return task_exc
