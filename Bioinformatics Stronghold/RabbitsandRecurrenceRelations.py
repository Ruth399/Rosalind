#let n be the number of months 
n = 30
#let k be the number of pairs of offspring each rabbit pair produces 
k = 3

onegen = 1

twogen = 1

for months in range(1, n-1):
    nextgen = onegen + twogen * k 
    twogen = onegen
    onegen = nextgen 
print(onegen)

def rabbit_pairs(num_months, num_offspring):
    if num_months == 1:
        return 1
    elif num_months == 2:
        return num_offspring
    
    one_gen = rabbit_pairs(num_months - 1, num_offspring)
    two_gen = rabbit_pairs(num_months - 2, num_offspring)
    
    return one_gen + (two_gen * num_offspring)

# Example usage
num_months = 5
num_offspring = 3
print(rabbit_pairs(num_months, num_offspring))


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