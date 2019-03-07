PRIME_NO_LIMIT=10 #set the limit here
i = 2
while(i < PRIME_NO_LIMIT):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1
