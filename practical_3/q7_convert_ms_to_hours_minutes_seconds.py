# Write a method convert_ms(n) that converts milliseconds to hours, minutes, and seconds. 
# The method returns a string as hours:minutes:seconds. 
# For example, convert_ms(5500) returns a string 0:0:5, 
# convert_ms(100000) returns a string 0:1:40, 
# and convert_ms(555550000) returns a string 154:19:10.

def convert_ms(n):
    ms = int(input("enter number of milliseconds: "))
    hours = int(ms / 3600000)
    mins = int((ms % 3600000) / 60000)
    seconds = int(((ms % 3600000) % 60000) / 1000)
    print(str(hours) + ":" + str(mins) + ":" + str(seconds))
