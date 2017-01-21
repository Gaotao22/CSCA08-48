from e2a import *


def reporter(f, x):
    '''(function, obj) -> str
    This function receives a function and a str. The received function will
    take the str as parameter. If the received function raises errors, matched
    result will be returned.
    Example:
    >>>reporter(raiser, '2')
    'no problem'
    >>>reporter(raiser, ['1', '2'])
    'generic'
    >>>reporter(raiser, '3')
    'E2OddException'
    '''
    try:
        # call the function
        f(x)
    # let the programs react to matched conditions
    except ValueError:
        return 'Value'
    except E2OddException:
        return 'E2OddException'
    except E2Exception:
        return 'E2'
    except TypeError:
        return 'generic'
    else:
        return 'no problem'
