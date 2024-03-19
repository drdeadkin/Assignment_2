from playsound import playsound

def merge_sort(array1):
    final = []
    left_2 = 0
    right_2 = 0
    file = 'C:\Users\justi\PycharmProjects\pythonProject\Sound Effect 1.wav' #intialize file for play sound
    if len(array1) <= 1:
        return array1
    half = len(array1) // 2  # divide intial array into 2
    left = array1[:half]
    right = array1[half:]  # split divided array into left and right array

    left_1 = merge_sort(left)
    right_1 = merge_sort(right)  # recursively divide both halves

    while left_2 < len(left_1) and right_2 < len(right_1):  # while the index counter of the length of the array of either left or right then sory
        if left_1[left_2] < right_1[right_2]:  # if left half of array is less the right, then append that element to final array
            final.append(left_1[left_2])
            left_2 += 1
            playsound(file) #play sound at swaps
        else:
            final.append(right_1[right_2])
            right_2 += 1
            playsound(file)

    final.extend(left_1[left_2:])  # use extend instead of append to add list of elements to final.
    final.extend(right_1[right_2:])

    return final  # Return the sorted array


def main():
    array1 = input("input how many numbers you want to be sorted, separated by a space: ")
    if len(array1) <= 1:
        print("Array already sorted(1 or less)")
        return array1
    sorted_array = merge_sort(array1.split(" "))
    print("Sorted using merge sort:", sorted_array)


if __name__ == '__main__':
    main()