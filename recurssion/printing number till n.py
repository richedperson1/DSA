def printing(n):
    if n <= 0:
        # This print function take care if we wanted to print last test case such as 0
        print(n)
        return
    print(n)
    printing(n-1)
    return


printing(10)
