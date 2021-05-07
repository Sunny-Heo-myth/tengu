# insertion sort

def insertion_sort(arr) :
    
    for i in range(1, len(arr)) :
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

# Example

x = [1,5,4,7,50,15,3,35,72,9]
insertion_sort(x)
print(x)
