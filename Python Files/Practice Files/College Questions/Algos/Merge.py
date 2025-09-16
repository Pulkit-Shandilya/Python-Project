def merge_sort(arr):
    # Base case: if the array has only one element, it's already sorted
    if len(arr) <= 1:
        return arr
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])      # Recursive call to sort left half
    right_half = merge_sort(arr[mid:])     # Recursive call to sort right half
    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i , j = 0 , 0
    # Merge elements from left and right in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements if any
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage:
if __name__ == "__main__":
    arr = [4, 1, 3, 2]
    sorted_arr = merge_sort(arr)
    print("Sorted Array:", sorted_arr)


"""
PSEUDOCODE FOR MERGE SORT:

ALGORITHM MergeSort(array)
BEGIN
    // Base case
    IF length of array <= 1 THEN
        RETURN array
    END IF
    
    // Divide
    SET mid = length of array / 2
    SET left_half = MergeSort(array[0 to mid-1])
    SET right_half = MergeSort(array[mid to end])
    
    // Conquer (merge)
    RETURN Merge(left_half, right_half)
END

ALGORITHM Merge(left, right)
BEGIN
    CREATE empty list result
    SET i = 0, j = 0
    
    // Compare and merge elements in sorted order
    WHILE i < length of left AND j < length of right DO
        IF left[i] <= right[j] THEN
            ADD left[i] to result
            INCREMENT i
        ELSE
            ADD right[j] to result
            INCREMENT j
        END IF
    END WHILE
    
    // Add remaining elements from left array
    WHILE i < length of left DO
        ADD left[i] to result
        INCREMENT i
    END WHILE
    
    // Add remaining elements from right array
    WHILE j < length of right DO
        ADD right[j] to result
        INCREMENT j
    END WHILE
    
    RETURN result
END
"""
