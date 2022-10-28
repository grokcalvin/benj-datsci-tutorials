def foo1(bar: str) -> str:
    return bar

def foo2(bar: str) -> list:
    return list(bar)

def foo3(bar: str) -> tuple:
    out = list(bar)
    length = len(out)
    return out, length


def foo4(bar: str) -> tuple:
    out = list(bar)
    length = len(out)

    return out, length, length+1


def complex(arg1: str, arg2: float, arg3: int) -> str:
    output = f"{arg1} is {arg2} for {arg3}"
    return output


def main():

    val1, val2, val3 = "val1", "val2", ("val3", "val4")
    out1, out2 = foo3(bar='testing')
    print(out1)
    print(out2)
    output = foo4(bar='testing')
    for o in output:
        print(o)

    # # unpacking lists
    args = ['bread', 9.99, 2] # order matters
    output1 = complex(*args)
    output2 = complex(args[0], args[1], args[2])
    print(output1)
    print(output2)

    # # unpacking dictionaries
    kwargs = {
        'arg3': 2, # order does not matter 
        'arg1': 'bread',
        'arg2': 9.99,

    }
    output3 = complex(**kwargs)
    print(output3)

if __name__ == '__main__':
    main()
