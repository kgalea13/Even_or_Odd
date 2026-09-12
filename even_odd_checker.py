
# 16. Even or Odd

# Gernerate 100 random numbers
# Keep count of how many of those random numbers are even and how many are odd

# Use random module

import random

# Helper function: Checks the numbers created by generate_randoms from the main().
# If they are even then function returns True, if odd, then returns False.
def odd_even_check(generate_randoms):
    check_odd_even = generate_randoms % 2

    if check_odd_even == 0:
        return True

    else:
        return False 
  
# Main function
def main():
    even_total = 0
    odd_total = 0

    for rand_num in range(0,100):
        generate_randoms = random.randint(1,100)
        numbers = odd_even_check(generate_randoms)
        if numbers == True:
            even_total = even_total + 1    
        else:
            odd_total = odd_total + 1


    print(f'*** There are {even_total} even numbers ***')
    print(f'*** There are {odd_total} odd numbers ***')
            
    

again = 'Y'

while again == 'Y':
    print(' ')
    main()
    print(' ')
    again = input('Do you want to play again? Y/N: ').upper() 
 
