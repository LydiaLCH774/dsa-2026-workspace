
# We import a library to draw pseudorandom numbers. 
# We'll learn more about libraries later in the module. 
import random  

def guess_the_number(min_value, max_value):
    """
    User must guess the value of a number between min_value and max_value

    Parameters:
        min_value, max_value (integers)
    """
    # YOUR CODE HERE
    random_num = random.randint(min_value, max_value)
    user_guess = input(f"Guess a number between {min_value, max_value}: ")
    
    if random_num == int(user_guess):
        return "Correct!"
    elif random_num < int(user_guess): 
        return "Too high!"
    else: 
        return "Too low!"

