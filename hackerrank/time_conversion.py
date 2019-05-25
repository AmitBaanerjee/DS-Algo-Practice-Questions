# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
#
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
#
# Function Description
#
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
#
# timeConversion has the following parameter(s):
#
# s: a string representing time in  hour format
def timeConversion(s):
    data=s.split(":")
    index=0
    if "PM" in s:
        if data[0]=="12":
            pass
        else:
            data[0]=str(int(data[0])+12)
        for i in range(len(data[-1])):
            if "P" ==data[-1][i]:
                index=i
                data[-1]=data[-1][:index]
                break
        return ":".join(data)
    if "AM" in s:
        if data[0]=="12":
            data[0]="00"
        for i in range(len(data[-1])):
            if "A" ==data[-1][i]:
                index=i
                data[-1]=data[-1][:index]
                break
        return ":".join(data)

print(timeConversion("07:05:35PM"))
