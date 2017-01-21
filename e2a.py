class E2Exception(Exception):
    '''The exception inherits the Exception class. It will be thrown when
    'CSCA48' is received.
    '''


class E2OddException(E2Exception):
    '''This exception is a subclass of E2Exception. It will be thrown when
    an odd number or a value that can be converted to an odd number is in
    the function.
    '''


def raiser(x):
    '''(obj) -> (Nonetype)
    This function will receives a parameter of any possible types. Then it will
    throws exceptions according to the condition the parameter may match. The
    only situation that the function will not return exception is when the
    input is an even number or a value that can be converted to an even number.
    RAISE: E2OddException if input value is an odd integer or it can be
    converted to an odd integer
           E2Exception if input is string 'CSCA48'
           ValueError if input is a string that cannot be converted to integer
           TypeError if input is any other types
    '''
    if (type(x) == int):
        if(x % 2 != 0):
            raise E2OddException
        else:
            pass
    elif (type(x) == str):
        if (x == "CSCA48"):
            raise E2Exception("Hi Brian")
        elif (not x.isnumeric()):
            raise ValueError
        else:
            if(int(x) % 2 != 0):
                raise E2OddException
            else:
                pass
    elif (type(x) == bool):
        if(x):
            raise E2OddException
        else:
            pass
    else:
        raise TypeError
