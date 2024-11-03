def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total_sum += calculate_structure_sum(item)

    elif isinstance(data, str):
        total_sum += len(data)

    elif isinstance(data, (int, float)):
        total_sum += data

    return total_sum


data_structure = (2.0, "Nicholas", {1, 2, 3})
result = calculate_structure_sum(data_structure)
print(result)
