# Write a program that displays the following two tables side-by-side (note that 1 mile is 1.609 kilometres):

# Miles	Kilometers	Kilometres	Miles
# 1    	1.609     	20        	12.430
# 2    	3.218     	25        	15.538

# ...
# 9    	14.481    	60        	37.290
# 10   	16.090    	65        	40.398

def milestokm(n,end):
  print("Miles" + "\t" + "Kilometres" + "\t" + "Kilometres" + "\t" + "Miles")
  for i in range(n,end):
    print(str(i) + "\t\t" + str("{0:.3f}".format(i*1.609)) + "\t\t" + str(i * 5 + 15) + "\t\t" + str("{0:.3f}".format((i * 5 + 15)/1.609)))

milestokm(1,11)
