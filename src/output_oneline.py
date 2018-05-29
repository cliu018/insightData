from time_diff import time_diff
def output_oneline (ip, startDate, startTime, endDate, endTime, requestedNum, outputFile):
    inactDue = time_diff(startDate, startTime, endDate, endTime)
    oneline = ip+","+startDate+" "+startTime+","+endDate+" "+ endTime+","+str(inactDue+1)+","+str(requestedNum)+"\n"
    f = open(outputFile, "a")
    # print ("write to file: "+oneline)
    # print (outputFile)
    # print(os.path.abspath(outputFile))
    f.write(oneline)

