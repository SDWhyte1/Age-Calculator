import datetime

x = datetime.datetime.now()
#print(x)
usDateY = x.strftime("%Y")
usDateM = x.strftime("%m")
usDateD = x.strftime("%d")
#print(usDateY)
#print(usDateY[-4:])
#usDate = int(usDate)
#print()
userBirth = input("Please enter your birth date in US format: ")


def age(nowDate,birthDate):
    nowYear = int(usDateY)
    birthYear = int(userBirth[-4:])
    nowMonth = int(usDateM)
    birthMonth = int(userBirth[0:2])
    nowDays = int(usDateD)
    birthDays = int(userBirth[3:5])

    if nowMonth < birthMonth:
        ages = (nowYear - birthYear)
    elif nowMonth == birthMonth:
        if nowDays >= birthDays:
            ages = (nowYear - birthYear)
        else:
            ages = ((nowYear - birthYear) - 1)
    else:
        ages = ((nowYear - birthYear) - 1)

    #print(nowMonth)
    #print(birthMonth)
    #print(birthDays)
    print("You are "+str(ages)+ " Years old")

age(usDateY,userBirth)
