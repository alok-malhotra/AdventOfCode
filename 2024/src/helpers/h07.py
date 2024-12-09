def can_make_value_a(val: int, nums: list, curr_val: int, idx: int, n: int) -> bool:    
    if curr_val == val and idx == n: return True
    if idx == n: return False
    return can_make_value_a(val, nums, curr_val * nums[idx], idx+1, n) or can_make_value_a(val, nums, curr_val + nums[idx], idx+1, n)

def can_make_value_b(val: int, nums: list, curr_val: int, idx: int, n: int) -> bool:  
    if curr_val == val and idx == n: return True
    if idx == n: return False

    return can_make_value_b(val, nums, curr_val * nums[idx], idx+1, n) \
            or can_make_value_b(val, nums, curr_val + nums[idx], idx+1, n) \
            or can_make_value_b(val, nums, int( str(curr_val) + str(nums[idx]) ), idx+1, n)