score = input("Enter Score out of 1: ")
try:
    s = float(score)
except:
    print ("error, enter a numerical value")
    quit()

if s >= 0.9:
    print ("A")
elif 0.8 <= s <= 0.9:
    print ("B")
elif 0.7 <= s <=0.8:
    print("C")
elif 0.6 <= s <=0.7:
    print ("D")
else :
    print ("F")
