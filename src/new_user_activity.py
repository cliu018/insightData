from active_user_features import active_user_features
def new_user_activity (startDate, startTime, endDate, endTime, requestedNum, lastCAE):
    userRecord = active_user_features()
    userRecord.startDate = startDate
    userRecord.startTime = startTime
    userRecord.lastDate = endDate
    userRecord.lastTime = endTime
    userRecord.requestedNum = requestedNum
    userRecord.lastCAE = lastCAE
    return userRecord


