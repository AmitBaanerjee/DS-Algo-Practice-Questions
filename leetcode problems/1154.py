1154. Day of the Year

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61

class Solution:
    def dayOfYear(self, date: str) -> int:
        dic={
            '01':31,
            '02':31+28,
            '03':31+28+31,
            '04':31+28+31+30,
            '05':31+28+31+30+31,
            '06':31+28+31+30+31+30,
            '07':31+28+31+30+31+30+31,
            '08':31+28+31+30+31+30+31+31,
            '09':31+28+31+30+31+30+31+31+30,
            '10':31+28+31+30+31+30+31+31+30+31,
            '11':31+28+31+30+31+30+31+31+30+31+30,
            '12':31+28+31+30+31+30+31+31+30+31+30+31

        }
        comp=date.split('-')
        result=0+int(comp[2])
        if int(comp[1])==1:
            return result
        elif int(comp[1])>1 and int(comp[1])<=10:

            result+=dic['0'+str(int(comp[1])-1)]
            if int(comp[0])%4==0 and int(comp[0])%100 !=0 and int(comp[1])>=3:
                return result+1
            else:
                return result
        elif int(comp[1])>1 and int(comp[1])>10:
            result+=dic[str(int(comp[1])-1)]
            if int(comp[0])%4==0 and int(comp[0])%100 !=0:
                return result+1
            else:
                return result
