#how many months will it take to save for your dream house
portion_down_payment = 0.25
current_savings = 0
r = 0.04 
num_of_months = 0

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of you salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))



#Find the amount you need to save
total_to_save = total_cost * portion_down_payment
print ('Total to save: ', total_to_save)


#use a while loop for iteration of a boolean statement when there isnt a list to loop through
while current_savings < total_to_save:
        #Find the amount you save each month
        #this needs to come into the loop so that it changes relative to annual salary
        monthly_saving = portion_saved * (annual_salary/12)
        print ('Monthly Saving: ', monthly_saving)
        
        #need to put the investment in the while loop otherwise it remains at 0 like the current_savings coutner outside of the loop
        investment = current_savings*r/12
        
        #count for current savings as each month passes
        current_savings = current_savings + (monthly_saving + investment)
        
        #count for months 
        num_of_months = num_of_months + 1 
        print (num_of_months)
        
        # nest an if statement inside a for loop?
        if num_of_months%6 == 0:
            annual_salary = annual_salary + (semi_annual_raise * annual_salary)
            print('ANNUAL SALARY:', annual_salary)
            

#if the while loop comes false then execute the if statement  
if current_savings >= total_to_save:
    print ('Number of months: ', num_of_months)