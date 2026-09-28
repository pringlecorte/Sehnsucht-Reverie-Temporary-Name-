def shrink(x, y, z):
    z -= 0.05 * (z/5)
    x += 0.25 * (z/5)
    y -= 1.5 * (z/5)
    

    return x, y, z

def grow(x, y, z):
    z += 0.05 * (z/5)
    x -= 0.25* (z/5)
    y += 1.5* (z/5)

    return x, y, z