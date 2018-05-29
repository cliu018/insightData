import os
from time_diff import time_diff
from output_oneline import output_oneline
from new_user_activity import new_user_activity
from copy import deepcopy

# Set up path
dir1 = '.'
inactFile = os.path.join(dir1, 'input', 'inactivity_period.txt')
logFile = os.path.join(dir1, 'input', 'log.csv')
outputFile = os.path.join(dir1, 'output', 'sessionization.txt')

if os.path.exists(outputFile):
    os.remove(outputFile)

# Read csv data
f = open(inactFile, "r")
inactPeriod = int(f.read())
f = open(logFile, "r")

tableHead = f.readline().split(",")
index_ip = tableHead.index("ip")
index_date = tableHead.index("date")
index_time = tableHead.index("time")
index_cik = tableHead.index("cik")
index_accession = tableHead.index("accession")
index_extention = tableHead.index("extention")

activeUserSet = dict()
activeUserOrder = list()

for oneRecord in f:
    recordList = oneRecord.split(",")
    ip = recordList[index_ip]
    date = recordList[index_date]
    time = recordList[index_time]
    cik = recordList[index_cik]
    accession = recordList[index_accession]
    extention = recordList[index_extention]

    # check if the active users passed the inactive period
    tempUserOrder = deepcopy(activeUserOrder)
    for user in activeUserOrder:
        curLastDate = activeUserSet[user].lastDate
        curLastTime = activeUserSet[user].lastTime
        inactDue = time_diff(curLastDate, curLastTime, date, time)
        if inactDue > inactPeriod:
            output_oneline(user, activeUserSet[user].startDate, activeUserSet[user].startTime, activeUserSet[user].lastDate,
                          activeUserSet[user].lastTime, activeUserSet[user].requestedNum, outputFile)
            del (activeUserSet[user])
            tempUserOrder.remove(user)
    activeUserOrder = deepcopy(tempUserOrder)

    # check if IP address existing
    if ip in activeUserSet:
        # Update the last request date, update the requested document number by checking the CAE
        activeUserSet[ip].lastDate = date
        activeUserSet[ip].lastTime = time
        activeUserSet[ip].requestedNum = activeUserSet[ip].requestedNum + 1
    else:
        # Create an active user
        activeUserSet[ip] = new_user_activity(date, time, date, time, 1, cik+"+"+accession+"+"+extention)
        activeUserOrder.append(ip)

# Finalize all of existing users
for userFinal in activeUserOrder:
    output_oneline(userFinal, activeUserSet[userFinal].startDate, activeUserSet[userFinal].startTime,
                  activeUserSet[userFinal].lastDate, activeUserSet[userFinal].lastTime, activeUserSet[userFinal].requestedNum, outputFile)



