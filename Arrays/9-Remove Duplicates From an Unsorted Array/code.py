def remove_duplicates_unsorted(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Example
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(remove_duplicates_unsorted(arr))  # [3, 1, 4, 5, 9, 2, 6]