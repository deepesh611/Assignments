def median(data):
    data.sort()
    if len(data) % 2 == 0:
        return (data[len(data)//2] + data[len(data)//2 - 1]) / 2
    else:
        return data[len(data)//2]
    

def Q1(data):
    if len(data) % 2 == 0:
        return median(data[:len(data)//2])
    else:
        return median(data[:len(data)//2])


def Q3(data):
    if len(data) % 2 == 0:
        return median(data[len(data)//2:])
    else:
        return median(data[len(data)//2+1:])


def IQR(data):
    return Q3(data) - Q1(data)


def LL(data):
    return Q1(data) - 1.5 * IQR(data)


def UL(data):
    return Q3(data) + 1.5 * IQR(data)


def Outliers(data):
    return [x for x in data if x < LL(data) or x > UL(data)]


def main():
    data = [12, 10, 11, 14, 76, 103, 13,15,12,16,17,11,16,25, 110, 20, 23, 27,19, 18,10,13,78, 15,14,20,28,32,87, 23,25,19,22,28,17,27,80,15, 18, 22, 20,25,82,27,21,12,15,18,90,108,28,150]
    
    data.sort()
    
    print(f"Min: {min(data)}")
    print(f"Max: {max(data)}")
    print(f"Median: {median(data)}")
    print(f"Q1: {Q1(data)}")
    print(f"Q3: {Q3(data)}")
    print(f"IQR: {IQR(data)}")
    print(f"LL: {LL(data)}")
    print(f"UL: {UL(data)}")
    print(f"Outliers: {Outliers(data)}")
    


if __name__ == '__main__':
    main()