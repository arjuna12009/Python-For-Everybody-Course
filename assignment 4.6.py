

hrs = input("Enter Hours:")
rate = input("Enter the rate per hour: ")
h = float(hrs)
r = float(rate)
def computepay (a,b):
    if a > 40.0:
        reg = a * b
        ot = (a - 40.0) * (b * 0.5)
        xp = reg + ot
        return xp
    else:
        xp = a * b
        return xp
p = computepay(h,r)
print(p)