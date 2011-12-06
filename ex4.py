# Traceback (most recent call last):
# File "ex4.py", line 8, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
# "the varible car_pool_capacity is defined wrong carpool_capacity
#  is used instead"

# 4.0 used as float, possible average?

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity =  cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

# variable
print "There are", cars, "cars available."
# variable
print "There are only", drivers, "drvers available."
# cars - drivers
print "There will be", cars_not_driven, "empty cars today."
# amount of room
print "We can transport", carpool_capacity, "people today."
# amount of passengers
print "We have", passengers, "to carpool today."
# number of people per car
print "We need to put about", average_passenger_per_car, "in each car."
