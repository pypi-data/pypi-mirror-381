import collections

HELPERS = collections.defaultdict(list)
PREPROCESSORS = collections.defaultdict(list)

def helper(*domains):
    def decorator(func):
        for d in domains:
            HELPERS[d].append(func)
        return func
    return decorator

def preprocessor(*domains):
    def decorator(func):
        for d in domains:
            PREPROCESSORS[d].append(func)
        return func
    return decorator
