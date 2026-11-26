# Lab 01 Exercise 1: Road Trip Budgeter

def calculate(one_way_km,budget): 
    fuel_cost_total = one_way_km * 0.25 * 2
    if budget < fuel_cost_total:
        return True
    else:
        return False
round_trip = calculate(100, 39)
print(round_trip)  # Output: True
