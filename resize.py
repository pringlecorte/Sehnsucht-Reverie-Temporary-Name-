def shrink(y, z, base_y):

    z -= 0.05 * (z/5)
    y -= 1 * (z/5)
    base_y -= 1 * (z/5)

    return y, z, base_y

def grow(y, z, base_y):

    z += 0.05 * (z/5)
    y += 1 * (z/5)
    base_y += 1 * (z/5)

    return y, z, base_y

def grow_thresholds(min_val, max_val, current_z):
    #45 degrees right triangle
    delta = current_z - 1
    min_val -= delta
    max_val += delta

    
    return min_val, max_val

def shrink_thresholds(min_val, max_val, current_z):
    #45 degrees right triangle
    delta = current_z - 1
    min_val += delta
    max_val -= delta

    return min_val, max_val
