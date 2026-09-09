import math
radius = 4.75
# diameter - srednnica
# circumference - obwod
# area - pole
# radius - promien

area = math.pi * radius**2
circum = 2 * math.pi * radius
diameter = 2 * radius

print(round(diameter,2), round(circum,2), round(area,2))