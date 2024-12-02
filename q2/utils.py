def is_safe_sequence(values):
    is_increasing_and_valid = all(values[i] < values[i+1] and 1 <= values[i+1] - values[i] <= 3 for i in range(len(values) - 1))
    is_decreasing_and_valid = all(values[i] > values[i+1] and 1 <= values[i] - values[i+1] <= 3 for i in range(len(values) - 1))
    return is_increasing_and_valid or is_decreasing_and_valid