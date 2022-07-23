arr = [1]*5
arr = []


n = len(arr)


def search_transition_points(arr, n):
    low = 0
    high = n-1
    point = False
    one_only = True
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == 1:
            point = True
            high = mid-1
        else:
            one_only = False
            low = mid+1

    if point == True and one_only == False:
        return high+1
    elif one_only:
        return 0
    else:
        return -1


print(search_transition_points(arr, n))
