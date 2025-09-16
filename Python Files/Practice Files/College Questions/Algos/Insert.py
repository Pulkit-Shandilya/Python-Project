def insertion_sort(arr):
    # Start from the second element (index 1) because first element is considered sorted
    for i in range(1, len(arr)):
        # Store the current element to be inserted into the sorted portion
        key = arr[i]
        
        # Start comparing with the element just before the current element
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            # Shift the larger element one position to the right
            arr[j + 1] = arr[j]
            # Move to the previous element for comparison
            j -= 1

        # Insert the key at its correct position in the sorted portion
        # j+1 is the correct position because j was decremented in the loop
        arr[j + 1] = key

    return arr


# Example usage:
if __name__ == "__main__":
    # Test array with unsorted elements
    arr = [5, 2, 9, 1, 5, 6]
    print("Original Array:", arr)
    
    # Call insertion sort function
    sorted_arr = insertion_sort(arr)
    
    # Display the sorted result
    print("Sorted Array (Insertion Sort):", sorted_arr)
    
    # Time Complexity: O(n²) in worst case, O(n) in best case (already sorted)
    # Space Complexity: O(1) - sorts in place

    '''
    INSERTION SORT PSEUDOCODE:
    
    ALGORITHM InsertionSort(arr)
    INPUT: Array arr of n elements
    OUTPUT: Sorted array in ascending order
    
    BEGIN
        FOR i = 1 TO n-1 DO
            key = arr[i]
            j = i - 1
            
            WHILE j >= 0 AND arr[j] > key DO
                arr[j + 1] = arr[j]
                j = j - 1
            END WHILE
            
            arr[j + 1] = key
        END FOR
        
        RETURN arr
    END
    
    Time Complexity: O(n²) worst case, O(n) best case
    Space Complexity: O(1)
    '''