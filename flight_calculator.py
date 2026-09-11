#Battery is rated for up to 8 hours of standby/idle operation
#Real-world Flight time is 3 hours (180 min) with no payload attached
#As Payload weight increases, active flight time decreases linearly
#T(w) = 180 - 0.1w

def calculate_flight_time(weight_grams):
    """
    Calculate the active flight time for a given payload weight in grams.

    Flight time decreases linearly as payload weight increases. The result
    cannot be negative.

    Args:
        weight_grams: Payload weight in grams.

    Returns:
        Flight time in minutes, with a minimum value of 0.

    Raises:
        ValueError: If weight_grams is negative.
    """

    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")
    
    flight_time = 180 - 0.1 * weight_grams
    return max(flight_time, 0)
    
    
def flight_time_table(max_weight_grams, step_grams):
    """
    Generate flight-time estimates for a range of payload weights.

    Args:
        max_weight_grams: Maximum payload weight to include, in grams.
        step_grams: Increment between payload weights, in grams.

    Returns:
        A list of tuples containing each payload weight and its calculated
        flight time in minutes.
    """
    table = []
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
    return table

