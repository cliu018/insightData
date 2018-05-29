from datetime import datetime
def time_diff(date1, time1, date2, time2):
    date1Array = date1.split("-")
    date2Array = date2.split("-")
    time1Array = time1.split(":")
    time2Array = time2.split(":")
    datetime1 = datetime(int(date1Array[0]), int(date1Array[1]), int(date1Array[2]), int(time1Array[0]),
                         int(time1Array[1]), int(time1Array[2]))
    datetime2 = datetime(int(date2Array[0]), int(date2Array[1]), int(date2Array[2]), int(time2Array[0]),
                         int(time2Array[1]), int(time2Array[2]))

    timedifference = datetime2 - datetime1
    diffT = timedifference.days*24*3600 + timedifference.seconds

    return int(diffT)