print("This program will compute the student average")
print(" ")
pre = float(input("Enter your Prelims Score   : "))
mid = float(input("Enter your Midterms Score  : "))
sem = float(input("Enter your Semis Score     : "))
finals = float(input("Enter your Finals Score : "))

avg = (pre + mid + sem + finals) / 4
print("Your average is {}!".format(avg))

if avg>=75:
    print("PASSED")
elif avg<75:
    print("FAILED")
else:
    print("Invalid")

    if avg>=99 and avg<=100:
    print("A")
elif avg>=90 and avg<=98:
    print("B")
elif avg>=80 and avg<=89:
    print("C")
elif avg>=71 and avg<=79:
    print("D")
elif avg>=61 and avg<=70:
    print("E")
elif avg<=60:
    print("F")
else:
    print("Invalid Input!")