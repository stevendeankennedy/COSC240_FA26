'''
    Exceptions!
    Special Thanks:
'''

class COSC240Error(Exception):
    def __init__(self, value):
        self.value = value

def example():
    word = input("Word? >")

    try:
        result = word - 5
        print(result)

    except TypeError:
        print("What happen??")
    except:
        print("Something happened I don't know what")
    finally: # CLEAN UP HERE
        print("FINALLY")
    print("after")

def example_bad():
    word = input("Word? >")

    result = word - 5
    print(result)

# This is a better way to raise exceptions
def raise_example(num):
    print("hey", num)

    if num > 5:
        raise ValueError("I made a value error")

def raise_ex2(num):
    try:
        print("1")
        if num < 5:
            raise ValueError("weird it broke")
        elif num == 67:
            raise COSC240Error("Six... Seven...")
    except ValueError:
        print("huh")
    except COSC240Error:
        print("67!")

#example()
try:
    #example()
    #raise_example(10)
    #raise_ex2(10)
    raise_ex2(67)
    #pass
except ValueError:
    print("woops")
