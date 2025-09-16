def binary_search(arr, target):
    """
    Performs binary search on a sorted array to find the target element.
    Returns the index of target if found, otherwise returns -1.
    """
    # Initialize left and right pointers
    left = 0
    right = len(arr) - 1
    
    # Continue searching while search space is valid
    while left <= right:
        # Calculate middle index to avoid overflow
        mid = left + (right - left) // 2
        
        # Check if target is found at middle
        if arr[mid] == target:
            return mid
        # If target is smaller, search left half
        elif arr[mid] > target:
            right = mid - 1
        # If target is larger, search right half
        else:
            left = mid + 1
    
    # Target not found
    return -1



# Example usage:
if __name__ == "__main__":
    # Test array (must be sorted for binary search)
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    # Test iterative version
    result = binary_search(arr, target)
    if result != -1:
        print(f"Iterative: Element {target} found at index {result}")
    else:
        print(f"Iterative: Element {target} not found")
    
    # Test recursive version
    result_recursive = binary_search_recursive(arr, target)
    if result_recursive != -1:
        print(f"Recursive: Element {target} found at index {result_recursive}")
    else:
        print(f"Recursive: Element {target} not found")


"""
PSEUDOCODE FOR BINARY SEARCH (ITERATIVE):

ALGORITHM BinarySearch(array, target)
BEGIN
    SET left = 0
    SET right = length of array - 1
    
    WHILE left <= right DO
        SET mid = left + (right - left) / 2
        
        IF array[mid] = target THEN
            RETURN mid
        ELSE IF array[mid] > target THEN
            SET right = mid - 1
        ELSE
            SET left = mid + 1
        END IF
    END WHILE
    
    RETURN -1  // Element not found
END

PSEUDOCODE FOR BINARY SEARCH (RECURSIVE):

ALGORITHM BinarySearchRecursive(array, target, left, right)
BEGIN
    // Base case
    IF left > right THEN
        RETURN -1
    END IF
    
    SET mid = left + (right - left) / 2
    
    IF array[mid] = target THEN
        RETURN mid
    ELSE IF array[mid] > target THEN
        RETURN BinarySearchRecursive(array, target, left, mid - 1)
    ELSE
        RETURN BinarySearchRecursive(array, target, mid + 1, right)
    END IF
END

TIME COMPLEXITY: O(log n)
SPACE COMPLEXITY: O(1) for iterative, O(log n) for recursive
PREREQUISITE: Array must be sorted
"""