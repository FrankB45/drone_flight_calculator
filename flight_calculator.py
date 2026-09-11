#Battery is rated for up to 8 hours of standby/idle operation
#Real-world Flight time is 3 hours (180 min) with no payload attached
#As Payload weight increases, active flight time decreases linearly
#T(w) = 180 - 0.1w

#returns active flight time in minutes for a given payload weight in grams
#Flight time cannot be negative, so if the calculated time is less than 0, return 0 instead
#If gram weight is negative, raise ValueError with a clear message
def calculate_flight_time(weight_grams):
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")
    
    flight_time = 180 - 0.1 * weight_grams
    return max(flight_time, 0)
    
    

#returns a list of (weight, flight_time) pairs for payload weights from 0 up to and including max_weight_grams,
#in increments of step_grams
#Function must call calculate_flight_time internally for each weight
def flight_time_table(max_weight_grams, step_grams):
    table = []
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
    return table

