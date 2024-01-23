#--------Even or Odd----------
#Description:
# Function that takes an integer as an argument
# returning even or odd

# 1) Read the problem out loud
# 2) Making any assumptions and clarifying the problem
# 3) Pseudo-code or how you will approach the question
# 4) start writing
# 5) test at each step with print statements



# write function that takes in integer

# evaluate whether or not that int is even or odd
# --- most likely need to use if stat with %

# return the string 'even' or 'odd

def even_or_odd(num):

    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

print(even_or_odd(4))
print(even_or_odd(5))