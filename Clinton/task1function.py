def volume_of_cylinder(radius, length):
    pi = 3.14
    area =(pi * radius) **2
    volume = area * length
    return area, volume
print(volume_of_cylinder(3, 8))
