#not currently working 
# runs infinitely
semi_annual_raise = 0.07
invest_return = 0.04
down_payment = 0.25
house_cost = 1000000

currentsalary = int(input('Enter the starting salary: '))
monthlysalary = currentsalary/12

#Find the amount you need to save
total_to_save = dream_house * down_payment
print ('Total to save: ', total_to_save)

numGuesses = 0 
close_enough_high = total_to_save + 100
close_enough_low = total_to_save - 100

low = 1
high = 10000

# find the starting midpoint
ans = (high + low)/2.0

calc = ((ans/10000) * currentsalary) * 36

#trying to work out best savings rate

while calc > close_enough_high or calc < close_enough_low:
        if calc < close_enough_low: 
                numGuesses += 1
                print (numGuesses)
# if calc is lower than close enough, then the mid point becomes the lowest
                low = ans
                ans = ((high + low)/10000)/2.0
                calc =((ans/10000) * currentsalary) * 36

        elif calc > close_enough_high:
                numGuesses += 1
                print (numGuesses)
#
                high = ans
                ans = ((high + low)/10000)/2.0
                calc =((ans/10000) * currentsalary) * 36

if close_enough_low <= calc <= close_enough_high:
        print ('Best savings rate: ', ans)
        print ('Steps in bisection search: ', numGuesses)


