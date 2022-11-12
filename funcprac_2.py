def details(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

details("Ankit", place="Bihar", mob=9999999999)