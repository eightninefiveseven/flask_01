from redis import *

if __name__ == '__main__':
    try:
        sr = StrictRedis()
        r1 = sr.set('name','zhang')
        r2 = sr.set('name1','wang')
        result = sr.get('name')
        print(result)
    except Exception as e:
        print(e)