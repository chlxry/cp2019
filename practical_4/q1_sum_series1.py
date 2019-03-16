def sum_series1(i):
  i = int(input("enter 'i': "))
  n = 1

  list = []
  while n <= i:
      list.append(1 / n)
      n = n + 1
    
  print(sum(list))
