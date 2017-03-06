# What Would Python Print
def whoami(r):
    while next(iter(r)):
        print("before")
        yield next(r)
        print("after")

def mysterious(m):
    while m > 0:
        yield m
        m -= 1

for x in whoami(mysterious(4)):
    print(x)