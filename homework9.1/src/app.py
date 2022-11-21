import argparse
import redis
import time
import random
import string

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help = "User that use system. Default: value = 1")
parser.add_argument("-k", "--key", help = "Key for get it value. Default: value = 'hsa'")
parser.add_argument("-s", "--sleep", help = "Sleep. Default: value = 5.0")
args = parser.parse_args()

user = int(args.user) if args.user else 1
key = args.key if args.key else 'hsa'
ttl = int(20)
sleep = float(args.sleep) if args.sleep else 5.0

ttl_refresh_cache = 0.1 * ttl
ttl_refresh_decision = ttl_refresh_cache / 2

r = redis.Redis(host='localhost', port=6379)

while True:
    ttl_last = r.ttl(name=key)
    print(f"User with id: {user}. TTL last: {ttl_last} seconds")
    
    if ttl_last > ttl_refresh_cache:
        print(f"User with id: {user}. Used cache. Value: '{r.get(name=key)}'")
    elif ttl_last < 0:
        print(f"User with id: {user}. Key '{key}' missed in cache.")
        print(f"User with id: {user}. Get value from db.")

        value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

        print(f"User with id: {user}. Value: '{value}'")
        
        r.set(name=key, value=value, ex=ttl)
    
    else:
        p = (random.randrange((ttl_refresh_cache - ttl_last) * 100, ttl_refresh_cache * 100, 1) / 100)   
        print(f"User with id: {user}. Probability: {p}. Decision: value > {ttl_refresh_decision}.")
        if p >= ttl_refresh_decision:        
            print(f"User with id: {user}. Used probabilistic cache.")
            print(f"User with id: {user}. Get value from db.")
            value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            print(f"User with id: {user}. Value: '{value}'")
            r.set(name=key, value=value, ex=ttl)
        else:
            print(f"User with id: {user}. Used cache. Value: '{r.get(name=key)}'")
    print('\n')
    time.sleep(sleep)