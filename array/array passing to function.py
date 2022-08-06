arr = [2, 3, 4]

# Python will pass address of the list to the function rather than copy of list
# which mean any change happen in function to the list also be reflected to the main list


def change(arr):
    arr[0] = 5


print("\nBefore changing list : ", arr)
change(arr)

print("After changeing list : ", arr, "\n")


brr = [2, 4, 6]
print("Before changing : ", brr)
change(brr)
print("List with different name : ", brr, "\n")
