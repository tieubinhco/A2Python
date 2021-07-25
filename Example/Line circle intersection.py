import math

# calculate using parametric subsitution to find intersections https://stackoverflow.com/questions/1073336/circle-line-segment-collision-detection-algorithm/1084899#1084899


def calculateIntersect(self, loc, start, end, radius):
    E = start
    L = end
    C = loc
    r = radius
    d = L - E
    f = E - C

    a = d.dot(d)
    b = 2 * f.dot(d)
    c = f.dot(f) - r ** 2
    discriminant = b ** 2 - 4 * a * c

    if (discriminant < 0):
        return None
    else:  # limit discriminant somehow?
        discriminant = discriminant ** 0.5
        t1 = (-b - discriminant) / (2 * a)
        t2 = (-b + discriminant) / (2 * a)

        canidates = {}
        if (t1 >= 0 and t1 <= 1.0):
            canidates[t1] = E + d * t1
        if (t2 >= 0 and t2 <= 1.0):
            canidates[t2] = E + d * t2

        if (len(canidates.keys()) > 0):
            intersect = canidates[max(canidates.keys())]
            return intersect
        else:
            return None
