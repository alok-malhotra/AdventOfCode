def valid_adjacent_elements(a: int, b: int, inc: bool) -> bool:
    # print(a, b);
    if inc:
        if a >= b or abs(a-b) not in [1,2,3]:
            return False
        return True        
    # else dec
    if a <= b or abs(a-b) not in [1,2,3]:
        return False
    return True

def is_strictly_inc(arr: list[int]) -> bool:
    for i in range(1, len(arr)):
        if not valid_adjacent_elements(arr[i-1], arr[i], True):
            return False
    return True

def is_strictly_dec(arr: list[int]) -> bool:
    for i in range(1, len(arr)):
        if not valid_adjacent_elements(arr[i-1], arr[i], False):
            return False
    return True

def is_strictly_inc_one_error_allowed(arr: list[int]) -> bool:
    for i in range(1, len(arr)):
        if not valid_adjacent_elements(arr[i-1], arr[i], True):
            # Now we remove i-1 and consider the array and also remove i and consider the array.
            # If we don't have a strictly increasing array for one of these, it will not work
            return is_strictly_inc(arr[0:i] + arr[i+1: len(arr)]) or is_strictly_inc(arr[0:i-1] + arr[i: len(arr)])
    return True

def is_strictly_dec_one_error_allowed(arr: list[int]) -> bool:
    for i in range(1, len(arr)):
        if not valid_adjacent_elements(arr[i-1], arr[i], False):
            # Now we remove i-1 and consider the array and also remove i and consider the array.
            # If we don't have a strictly increasing array for one of these, it will not work
            return is_strictly_dec(arr[0:i] + arr[i+1: len(arr)]) or is_strictly_dec(arr[0:i-1] + arr[i: len(arr)])
    return True
