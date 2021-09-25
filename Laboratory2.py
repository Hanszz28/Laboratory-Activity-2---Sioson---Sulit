print("This program will compute the student average")
print(" ")
pre = float(input("Enter your Prelims Score   : "))
mid = float(input("Enter your Midterms Score  : "))
sem = float(input("Enter your Semis Score     : "))
finals = float(input("Enter your Finals Score : "))

avg = (pre + mid + sem + finals) / 4
print("Your average is {}!".format(avg))