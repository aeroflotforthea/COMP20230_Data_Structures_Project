

# RECURSIVE APPROACH

def count_sets(arr, total):
    return rec(arr, total, len(arr) - 1)

def rec(arr, total, i):
    if total == 0:
        # if the total is 0, then we just want an empty set, so return 1
        return 1
    elif total < 0: 
        return 0
        # if the total is smaller than 0, there are no subsets, so return 0
    elif i < 0:
        return 0
        # if the index is past the beginning of the array, there are no subsets, so return 0
    elif total < arr[i]:
        return rec(arr, total, i-1)
        # now we want to start recursively moving towards those base cases. If the total is smaller than the number at the index, this means there are no subsets here, so we run the same process at the earlier index
    else: 
        return rec(arr, total - arr[i], i-1) + rec(arr, total, i-1)
        # but otherwise, e.g if the total is either bigger than the number there or the same, we want to add all of the possibilities from a smaller total at an earlier index to all of the possibilities from the same total at an earlier index

# print(count_sets([2,4,6,10], 16))



# DYNAMIC PROGRAMMING APPROACH


def count_sets_dp(arr, total):
    mem = {}
    # mem is a dictionary
    return dp(arr, total, len(arr) -1, mem)
    

def dp(arr, total, i, mem):
    print(mem)
    # in this situation, we want to store the results of the computations in mem, which is a dictionary
    key = str(total) + ":" + str(i) # we create a unique key for each computation
    if key in mem:
        return mem[key]
        # if the computation has already been done, do that
    if total == 0:
        return 1
    # this is our single subset
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    # there are by definition no subsets beyond the last index
    elif total < arr[i]:
        to_return = dp(arr, total, i-1, mem)
    else: 
        to_return = (dp(arr, total - arr[i], i-1, mem) + dp(arr, total, i-1, mem))
        mem[key] = to_return
    return to_return
        

print(count_sets_dp([2,4,6,10], 16))
    

