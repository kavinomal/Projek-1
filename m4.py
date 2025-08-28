for i in range(0,3):
    print("jeruk", i)
    for j in range(0,3):
        print("pisang", j)
        for h in range(0,3):
            print("jeruk", h)

            #materilanjut
for i in range(0,10):
    print("hai", i)
    if i > 5:
        print("apel", i)
        break

    #lanjutan ke 2
    for i in range(0,10):
        print("hai", i)
        if i > 5:
            print("apel", i)
            break
    
    #LANJUTAN
    for i in range(0,10):
        print("t", i)
        if i >= 5:
            continue
            print("apel", i)
            print("pisang")
        print("hai", i)

        #while
        while 1 == 1:
            print("a")
            break