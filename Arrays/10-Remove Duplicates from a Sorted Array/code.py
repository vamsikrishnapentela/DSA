def remove_duplicates_sorted(arr):
    if not arr:
        return []
    
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])
    return result

# Example
arr = [1, 1, 2, 3, 3, 4, 5, 5]
print(remove_duplicates_sorted(arr))  # [1, 2, 3, 4, 5]