# A stack has two operations: push and pop
# All function calls go onto the call stack
# the call stack can get very large, which takes up a lot of memory

def greet2(name):
    print("how are you, ", name, "?")

def bye():
    print("ok bye!")

def greet(name):
    print("hello, ", name, "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

greet("adit")