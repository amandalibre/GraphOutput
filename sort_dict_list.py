def sort_dict_list(dict):
    values = []
    sorted = []
    for entry in dict:
        for key, value in entry.items():
            values.append(value)
        values.sort(key=lambda x: x, reverse=True)
    for number in range(len(values)):
        for entry in dict:
            for key, value in entry.items():
                if value == values[number]:
                    sorted.append(entry)
                    break
    return sorted