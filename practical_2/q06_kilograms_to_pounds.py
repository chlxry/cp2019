# Write a program that displays the following table (1 kilogram = 2.2 pounds):

# Kilograms Pounds
# 1         2.2
# 2         4.4
# 3         6.6
# ...
# 9         19.8
# 10        22.0

def kilotopounds(n,end):
  print("Kilograms" + "\t" + "Pounds")
  for i in range(n,end):
    print(str(i) + "\t\t" + str("{0:.1f}".format(i*2.2)))

kilotopounds(1,11)
