"""
Python Algorithms: Searching & Sorting
Comprehensive implementations of fundamental data structures concepts.
"""

# --- UNIT 1: SEARCHING ALGORITHMS ---

def linear_search(arr, target):
    """Checks every element one by one. O(n)"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Repeatedly halves the search interval. O(log n)
    Note: Input array MUST be sorted.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# --- UNIT 2: SIMPLE SORTING (O(n^2)) ---

def bubble_sort(arr):
    """Swaps adjacent elements if they are in wrong order."""
    n = len(arr)
    temp_arr = arr.copy() # Avoid modifying original list
    for i in range(n):
        for j in range(0, n - i - 1):
            if temp_arr[j] > temp_arr[j + 1]:
                temp_arr[j], temp_arr[j + 1] = temp_arr[j + 1], temp_arr[j]
    return temp_arr

def selection_sort(arr):
    """Finds the minimum and moves it to the front."""
    temp_arr = arr.copy()
    for i in range(len(temp_arr)):
        min_idx = i
        for j in range(i + 1, len(temp_arr)):
            if temp_arr[j] < temp_arr[min_idx]:
                min_idx = j
        temp_arr[i], temp_arr[min_idx] = temp_arr[min_idx], temp_arr[i]
    return temp_arr


# --- UNIT 3: ADVANCED SORTING (O(n log n)) ---

def merge_sort(arr):
    """Recursively splits and merges lists in sorted order."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    """Partitions array around a pivot."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# --- UNIT 4: EXECUTION & TESTING ---

if __name__ == "__main__":
    # Sample Data
    unordered_data = [64, 34, 25, 12, 22, 11, 90]
    target_val = 22

    print("--- Sorting Demonstration ---")
    print(f"Original Data:  {unordered_data}")
    print(f"Bubble Sort:    {bubble_sort(unordered_data)}")
    print(f"Selection Sort: {selection_sort(unordered_data)}")
    print(f"Merge Sort:     {merge_sort(unordered_data)}")
    print(f"Quick Sort:     {quick_sort(unordered_data)}")
    
    # Pythonic Way (Timsort)
    print(f"Python Built-in:{sorted(unordered_data)}")

    print("\n--- Searching Demonstration ---")
    # Linear search can work on unsorted data
    lin_idx = linear_search(unordered_data, target_val)
    print(f"Linear Search: Finding {target_val} -> Index: {lin_idx}")

    # Binary search REQUIRES sorted data
    sorted_data = sorted(unordered_data)
    bin_idx = binary_search(sorted_data, target_val)
    print(f"Binary Search: Finding {target_val} in {sorted_data} -> Index: {bin_idx}")
