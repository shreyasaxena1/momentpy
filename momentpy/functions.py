# @param dayNum: Integer -> The Number of the weekday
# @return [String, String] -> List of String with Full Weekday and Weekday in short Format
def getDayString(dayNum):
     dayDict = {  
        1: ['Monday' ,'Jan'],
        2: ['Tuesday','Feb'],
        3: ['Wednesday','Mar'],
        4: ['Thursday','Apr'],
        5: ['Friday','May'],
        6: ['Saturday', 'Jun'],
        7: ['Sunday', 'Jul'],
     }
    return dayDict.get(dayNum,['Invalid'])

# @param monthNum: Integer -> The Number of the month
# @return [String, String] -> List of String with Full Month String and Full Month in short format
def getMonthString(monNum):
    monthDict = {
        1: ['January' ,'Jan'],
        2: ['February','Feb'],
        3: ['March','Mar'],
        4: ['April','Apr'],
        5: ['May','May'],
        6: ['June', 'Jun'],
        7: ['July', 'Jul'],
        8: ['August', 'Aug'],
        9: ['September', 'Sep'],
        10: ['October', 'Oct'],
        11: ['November', 'Nov'],
        12: ['December', 'Dec']
    }
    return monthDict.get(monNum,['Invalid'])

# @param monthNum: Integer -> Current Year
# @return nextLeap: Integer -> Next Leap Year
def IsLeapYear(year):
 if (year % 4) == 0:
     if (year % 100) == 0:
         if (year % 400) == 0:
           return True
         else:
           return False
     else:
         return True
 else:
     return False     

def GetNextLeapYear(CurrYear):
    nextLeap = CurrYear
    while(IsLeapYear(nextLeap)==False):
        nextLeap =  nextLeap +1
    return nextLeap
    
