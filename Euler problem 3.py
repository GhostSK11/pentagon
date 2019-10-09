'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

n = 600851475143
a = 2

while a * a < n:
    while n % a == 0:
        n = n / a
    a = a + 1

print ("The largest prime factor number is:", n)