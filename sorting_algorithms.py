class Sort:

    # MERGE SORT
    @staticmethod
    def merge(array):
        comparisons = 0

        # Split the list in 2 recursively 
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]

            # Recursely split & sort each half
            left_comparisons = Sort.merge(left)
            right_comparisons = Sort.merge(right)

            comparisons += left_comparisons + right_comparisons

            # Two iterators for left and right
            i = 0
            j = 0
            
            # Iterator for the main list
            k = 0
            
            while i < len(left) and j < len(right):
                
                comparisons += 1

                # Swap unsorted elements in subarrays
                if left[i] <= right[j]:
                    array[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
                comparisons += 1

            while j < len(right):
                array[k]=right[j]
                j += 1
                k += 1
                comparisons += 1
        
        return comparisons

        
    # SHELL SORT
    @staticmethod
    def shell(array):
        comparisons = 0

        n = len(array)

        h = n // 2

        while h > 0:

            for i in range(h, n):
                t = array[i]
                j = i

                while j >= h and array[j - h] > t:
                    array[j] = array[j - h]
                    j -= h
                    comparisons += 1
    
                array[j] = t
                comparisons += 1

            h = h // 2
    
        return comparisons

    # INSERTION SORT
    @staticmethod
    def insertion(array):
        comparisons = 0
        # Iterate through array starting from the first index
        for i in range(1, len(array)):
    
            num = array[i]
            j = i-1

            comparisons += 1

            # While element not in it's place, move it back
            while j >=0 and num < array[j] :
                    array[j+1] = array[j]
                    j -= 1

                    comparisons += 1

            array[j+1] = num
        
        return comparisons
  
    # SELECTION SORT
    @staticmethod
    def selection(array):
        comparisons = 0

        # Iterate through all array elements
        for i in range(len(array)):
            
            # Find the minimum element in remaining
            # unsorted array
            min_i = i

            comparisons += 1

            for j in range(i+1, len(array)):
                comparisons += 1
                if array[min_i] > array[j]:
                    min_i = j
                    
            # Swap the found minimum element with
            # the first element       
            array[i], array[min_i] = array[min_i], array[i]
        
        return comparisons
