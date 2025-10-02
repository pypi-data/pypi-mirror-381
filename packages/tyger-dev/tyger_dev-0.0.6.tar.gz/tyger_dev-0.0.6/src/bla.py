import pdb
import sys

def trace(frame, event, arg):
    print(f"{event} at {frame.f_code.co_name}:{frame.f_lineno}", [arg])
    return trace

sys.settrace(trace)

def foo1():
    return 1
def foo2():
    return 2
def bar(x, y):
    return x + y

def main():
    1+2
    bar(foo1(), foo2())

pdb.set_trace()
main()