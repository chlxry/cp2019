def sum_series2(i):
  i = int(input("enter 'i': "))
  n = 1
  list = []
  while n <= i:
      list.append(n / (2 * n + 1))
      n = n + 1
    
  print(sum(list))
