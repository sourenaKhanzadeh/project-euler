"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 234168
"""

def sum_multiples_3_5(n=1000):
    res = 0
    for i in range(n+1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res

if __name__ == "__main__":
    print(sum_multiples_3_5())
