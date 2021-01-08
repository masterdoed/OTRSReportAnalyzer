import pandas as pd 
import os

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

#initialize variables for report analysis
fileName="SampleReport.csv"

#read CSV into dataframe
csv=pd.read_csv(fileName)

#print all new tickets
for row in csv.itertuples():
	if row.Status=="new":
		ID=str(row.TicketID)
		title=str(row.Title)
		queue=str(row.Queue)
		status=str(row.Status)
		print(ID+","+title+","+queue+","+status)

#print all closed tickets
for row in csv.itertuples():
	if row.Status=="closed":
		ID=str(row.TicketID)
		title=str(row.Title)
		queue=str(row.Queue)
		status=str(row.Status)
		print(ID+","+title+","+queue+","+status)

#print all merged tickets
for row in csv.itertuples():
	if row.Status=="merged":
		ID=str(row.TicketID)
		title=str(row.Title)
		queue=str(row.Queue)
		status=str(row.Status)
		print(ID+","+title+","+queue+","+status)

#print all waiting for customer tickets
for row in csv.itertuples():
	if row.Status=="waiting for custiomer":
		ID=str(row.TicketID)
		title=str(row.Title)
		queue=str(row.Queue)
		status=str(row.Status)
		print(ID+","+title+","+queue+","+status)

#print all action required tickets
for row in csv.itertuples():
	if row.Status=="action required":
		ID=str(row.TicketID)
		title=str(row.Title)
		queue=str(row.Queue)
		status=str(row.Status)
		print(ID+","+title+","+queue+","+status)

#print tickets by queue
queues=["Queue 1", "Queue 2", "Queue 3", "Queue 4"]
#print(len(queues))
for i in range(0,len(queues)):
	df_mask=csv["Queue"]==queues[i]
	df_filtered=csv[df_mask]
	for row in df_filtered.itertuples():
		print(row)





