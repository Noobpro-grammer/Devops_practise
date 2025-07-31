def divide(a, b):
    result = a / b  # this will crash on b=0
    return result

def duplicate_code():
    a = 10
    b = 5
    c = a + b
    print("Duplicate logic")

def duplicate_code2():
    a = 10
    b = 5
    c = a + b
    print("Duplicate logic")

def deeply_nested():
    if True:
        if True:
            if True:
                if True:
                    if True:
                        print("Too deep")
