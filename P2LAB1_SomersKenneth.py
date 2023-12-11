miles_per_gallon = float(input())

dollars_per_gallon = float(input())

your_value1 = (20 / miles_per_gallon) * dollars_per_gallon
your_value2 = (75 / miles_per_gallon) * dollars_per_gallon
your_value3 = (500 / miles_per_gallon) * dollars_per_gallon
print('{:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3))
