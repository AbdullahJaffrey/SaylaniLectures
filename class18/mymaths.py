def addition(*num):
    '''
    It can take arbitrary arguments.
    Takes multiple inputs in one shot and 
    Returns their sum.
    
    '''
    if len(num) == 0:
        return 'atleast two parameters required'
    else:
        return sum(num)

def exponent(num,exp):
    '''
    Takes two inputs(either integer or float). One as number and second as its exponent and later
    Returns the result generated from this function.
    
    '''
    return num**exp
