import math
def shrink(y, z):
    #print(f"Before {x}")
    z -= 0.05 * (z/5)
    y -= 1 * (z/5)

    #print(y)
    #print(f"dist from center {x}")
    return y, z

def grow(y, z):
    #print(f"Before {x}")
    z += 0.05 * (z/5)
    y += 1 * (z/5)
    
    #print(y)

    #print(f"dist from center {x}")
    return y, z

def grow_thresholds(min_val, max_val, current_z):
    #45 degrees right triangle
    delta = abs(1 - current_z)
    min_val -= delta
    max_val += delta

    
    return min_val, max_val

def shrink_thresholds(min_val, max_val, current_z):
    #45 degrees right triangle
    delta = abs(1 - current_z)
    min_val += delta
    max_val -= delta


    return min_val, max_val
