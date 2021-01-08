import analyzeReport
from analyzeReport import Reporter

fileName="SampleReport.csv"
r=Reporter(fileName)

#fetch and print tickets with status "new"
newTics=r.newTickets(r.csv)
r.printDataFrame(newTics)
print("##################################")

#fetch and print tickets with status "closed"
closedTics=r.closedTickets(r.csv)
r.printDataFrame(closedTics)
print("##################################")

#fetch and print tickets with status "merged"
mergedTics=r.mergedTickets(r.csv)
r.printDataFrame(mergedTics)
print("##################################")

#fetch and print tickets with status "waiting for customer"
customerTics=r.customerTickets(r.csv)
r.printDataFrame(customerTics)
print("##################################")

#fetch and print tickets with status "in porgress"
progressTics=r.progressTickets(r.csv)
r.printDataFrame(progressTics)
print("##################################")

#fetch and print tickets with status "action required"
actionTics=r.actionTickets(r.csv)
r.printDataFrame(actionTics)
print("##################################")

queueTics=r.ticsByQueue(r.csv, r.queues)


