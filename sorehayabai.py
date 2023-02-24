def sorehasosu(x):
    count = 0
    for i in range(2,x,2):
        if x%i == 0:
            count = 1
            break

    
    if count == 0:
        print("それは素数")
    else:
        print("それはやばい")

sorehasosu(11)