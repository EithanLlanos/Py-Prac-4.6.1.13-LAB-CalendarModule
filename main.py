# Scenario
# During this course, we looked at the Calendar class a bit. Your task is to extend its functionality with a new method called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

# Use the following tips:

# Create a class called MyCalendar that extends the Calendar class;
# create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
# in your implementation, use the monthdays2calendar method of the Calendar class.
# The following are the expected results:

# Sample arguments

# year=2019, weekday=0

# Expected output

# 52


# Sample arguments

# year=2000, weekday=6

# Expected output

# 53
####################################################################################################################################################

import calendar


class MyCalendar():
    def __init__(self):
        pass

    def count_weekday_in_year(self,year,weekday):
        self.__ct = 0
        self.__cal = calendar.Calendar()
        for i in range(1,13):
    
            for d in self.__cal.itermonthdays2(year,i):
                if d[0] == False:
                    continue
                if d[1] == weekday:
                    self.__ct +=1
        return self.__ct
        

Cal = MyCalendar()

print(Cal.count_weekday_in_year(2019,1))

