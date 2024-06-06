#let n be the number of months 
n = 5
#let k be the number of pairs of offspring each rabbit pair produces 
k = 3

onegen = 1

twogen = 1

for months in range(1, n-1):
    nextgen = onegen + twogen * k 
    twogen = onegen
    onegen = nextgen 
print(onegen)


#def months():

#def offspring():



#def rabbitpairs(int(months), int(offspring)):
 ##  # if months == 1:
      #  return 1
       # return offspring
   ## elif months == 2:
    
#onegen = rabbitpairs(months - 1, offspring)
#twogen = rabbitpairs(months - 2, offspring)


#int (rabbitpairs(int months, int offspring)
#if months == 1:
#else if months == 2:
 #   return 1
 #   return offspring
# long and int were unified