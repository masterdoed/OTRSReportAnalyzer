#OTRS Sample Report FORMAT
##TICKET NUMMER as datetime
##TICKET TITLE as text
##TICKET QUEUE as text
##TICKET STATUS as text
	### new
	### closed
	### in progress
	### merged
	### waiting for customer
	### action required


#initailize function variables for report generation
ticketID=1000000000
ticketTitle="Ticket title "
ticketQueue=["Queue 1", "Queue 2", "Queue 3", "Queue 4"]
ticketStatus=["new", "closed", "merged", "in progress", "waiting for customer", "action required"]
fileName="SampleReport.csv"

#open file for writing
f=open(fileName, "a")

#write file header
f.write("TicketID"+","+"Title"+","+"Queue"+","+"Status"+"\n")

#create a sample report with random tickets
for i in range(1, 100):
	tID=str(ticketID+i)
	tTitle=ticketTitle + " " + str(i)
	tq=i%4
	ts=i%6
	line=tID+','+tTitle+','+ticketQueue[tq]+','+ticketStatus[ts]
	f.write(line + "\n")

#close file
f.close()