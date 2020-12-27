# @param dayNum: Integer -> The Number of the weekday
# @return [String, String] -> List of String with Full Weekday and Weekday in short Format
def getDayString(dayNum):
    if dayNum==0:
        return ['Monday', 'Mon']
    elif dayNum==1:
        return ['Tuesday', 'Tue']
    elif dayNum==2:
        return ['Wednesday', 'Wed']
    elif dayNum==3:
        return ['Thursday', 'Thur']
    elif dayNum==4:
        return ['Friday', 'Fri']
    elif dayNum==5:
        return ['Saturday', 'Sat']
    elif dayNum==6:
        return ['Sunday', 'Sun']

# @param monthNum: Integer -> The Number of the month
# @return [String, String] -> List of String with Full Month String and Full Month in short format
def getMonthString(monthNum):
    if monthNum==0:
        return ['January', 'Jan']
    elif monthNum==1:
        return ['February', 'Feb']
    elif monthNum==2:
        return ['March', 'Mar']
    elif monthNum==3:
        return ['April', 'Apr']
    elif monthNum==4:
        return ['May', 'May']
    elif monthNum==5:
        return ['June', 'Jun']
    elif monthNum==6:
        return ['July', 'Jul']
    elif monthNum==7:
        return ['August', 'Aug']
    elif monthNum==8:
        return ['September', 'Sep']
    elif monthNum==9:
        return ['October', 'Oct']
    elif monthNum==10:
        return ['November', 'Nov']
    elif monthNum==11:
        return ['December', 'Dec']
