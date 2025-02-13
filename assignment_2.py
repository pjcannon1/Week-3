#%% Intro

'''
Please The following code SHOULD run and FINISH...but doesn't

This is an example of an infinite loop.  This is NOT a good thing to 
have in your code.  It will cause your code to run forever and never
finish.  This is a problem because it will cause your code to use up
all of the resources on your computer and cause it to crash.

Please fix the code so that it runs and finishes.

You should only need to change two lines of code to fix this problem!

This loop should count to 10 and then stop. PC
'''

# Fix: Move `i = 0` outside the loop
finished_program = False
i = 0  # Initialize i before the loop

# Count to 10 Program
while not finished_program:  
    print(f'Testing i = {i}')

    if i == 10:
        finished_program = True  # Exit condition

    i += 1  # Fix: Increment i properly

