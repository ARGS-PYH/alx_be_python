try: 
    n = 30
    d = 2
    c = n/d
except Exception as a:
    print(a)
else:
    print(c)
finally:
    print("Execute somthing regardless")