def third_largest(numbers):
    distinct = sorted(set(numbers), reverse=True)

    if len(distinct) < 3:
        raise ValueError("List needs at least three distinct numbers")

    return distinct[2]


values = [10, 20, 4, 45, 99]
print(third_largest(values))