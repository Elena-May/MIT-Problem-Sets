#ProblemSet1c
## for a given savings rate how many does it take to save it function for the given saving rate bisection search with the function in it 

semi_annual_raise = 0.07
invest_return = 0.04
down_payment = 0.25
house_cost = 1000000
num_of_months = 0
 
amount_to_save = house_cost * down_payment 

annual_salary = int(input('Enter your wage: ')

low = 0
high = 1

current_savings = 0 

# find the starting midpoint
ans = (high + low)/2.0

# a function that calculates based on a saving rate how many months it will take to save a certain amount 
def months_taken_func(saving_rate):
   
   while current_savings =! amount_to_save: 
        num_of_months += 1

        if num_of_months%6 == 0:
            annual_salary = annual_salary + (semi_annual_raise * annual_salary)
        
        portion_saved_monthly = (annual_salary/12) * saving_rate

        investment = current_savings*r/12

        current_savings = current_savings + (portion_ saved_monthly + investment)
return num_of_months


if months_taken_func(ans) > 36:
    low = ans
    ans = ((high + low)/2.0
    print (numGuesses)

elif months_taken_func(ans) < 36:
    high = ans
    ans = ((high + low)/2.0
    print (numGuesses)





            

   

