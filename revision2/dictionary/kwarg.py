dist = {"name":"Rutvik",'lastName':"Jaiswal","number":9673062604}


def func(**kwar):
    print(kwar)
    return kwar


print(func(**dist))