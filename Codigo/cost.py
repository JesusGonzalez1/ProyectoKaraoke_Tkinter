def calculate_cost(people, hours):
    rate_per_half_hour = 5000  
    total_cost = (hours * 2) * rate_per_half_hour * people
    return total_cost
