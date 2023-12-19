from datetime import timedelta, datetime

check = 1
while check != 0:

    curr = datetime.now()
    end = datetime(curr.year, 11, 28)
    if end <= curr: end = datetime(curr.year + 1, 11, 28)
    
    print("\n{}".format(end - curr))

    check = int(input("\nCheck Again ? 1 : 0 = "))