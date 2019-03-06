# Write a function m_series(i) to compute the following series:

# Write a test program that displays the following table:

# i         m(i)     
# 1         0.5000   
# 2         1.1667   
# ... 
# 19        16.4023  
# 20        17.3546  

def m_series(i, end):
    print("i" + "\t" + "m(i)") # heading
    sum = 0
    for i in range(1, 21):       
        sum = sum + i/(i+1)
        print(str(i) + "\t" + str("{0:.4f}".format(sum)))

m_series(1,21)
