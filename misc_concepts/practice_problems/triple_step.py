# O(3^n)
def triple_step(stairs):
    # Setup memoizer
    mem = [None] * (stairs + 1)
    # Run with stairs and memoizer
    return triple_step_mem(stairs, mem)


def triple_step_mem(stairs, mem):
    # If we've cached the anser already, return that
    if mem[stairs]:
        return mem[stairs]
    # 0 stairs = no stairs left
    if stairs <= 0:
        return 0
    # 1 stair = one possible way
    elif stairs == 1:
        return 1
    # 2 stairs = two possible ways => [1,1] & [2]
    elif stairs == 2:
        return 2
    # 3 stairs = 4 possible ways => [1,1,1] & [2, 1] & [1, 2] & [3]
    elif stairs == 3:
        return 4
    # Everything else is a sum of the known steps away from top
    else:
        # Cache our results and return
        mem[stairs] =  triple_step_mem(stairs-1, mem) + \
                       triple_step_mem(stairs-2, mem) + \
                       triple_step_mem(stairs-3, mem)
        return mem[stairs]
