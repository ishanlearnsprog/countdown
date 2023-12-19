from datetime import timedelta, datetime

check = 1
while check != 0:

    curr = datetime.now()
    end = datetime(curr.year, 11, 28)
    if end <= curr: end = datetime(curr.year + 1, 11, 28)
    
    days, timestamp = str((end - curr)).split(",")
    hours, mins, _ = timestamp.split(":")
    print("\n{}\n{} hours\n{} minutes".format(days, hours, mins))

    check = int(input("\nCheck Again ? 1 : 0 = "))