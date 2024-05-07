names = ['Alice', 'Bob', 'Charley']
for name in names:
  print ('Hello, ' + name)

#print(list(range(5, 12)))
print(range(5, 12))
#notice the difference between the outputs of line 5 and 6 -> in 5, the list function effectively converses the range into a list, which is then printed

numbers = list(range(4489,9038,2))
total = 0 
for i in numbers:
  total += i
print(total)
  
#while a < 200:
  #print((a + 1))
  #a = a + 2
#b = 200
#print(list(range((a+1), b, 2)))

