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

class Reporter:
	fn=""
	csv=pd.DataFrame()
	queues=[]
	

	def __init__(self, fileName):
		#initialize variables for report analysis
		#read fileName into dataframe
		self.fn=fileName
		self.csv=pd.read_csv(fileName)
		self.queues=["Queue 1", "Queue 2", "Queue 3", "Queue 4"]
	
	# function to print an ticket DataFrame object
	def printDataFrame(self, df):
		for row in df.itertuples():
			ID=str(row.TicketID)
			title=str(row.Title)
			queue=str(row.Queue)
			status=str(row.Status)
			result=ID+","+title+","+queue+","+status
			print(result)

	# function to create a new ticket DataFrame object
	def newTickets(self, csv):
		#print all new tickets
		df_mask=csv["Status"]=="new"
		df_filtered=csv[df_mask]
		
		return df_filtered

	# function to create a new close DataFrame object
	def closedTickets(self, csv):
		#print all new tickets
		df_mask=csv["Status"]=="closed"
		df_filtered=csv[df_mask]
		
		return df_filtered

	# function to create a merged ticket DataFrame object
	def mergedTickets(self, csv):
		#print all new tickets
		df_mask=csv["Status"]=="merged"
		df_filtered=csv[df_mask]
		
		return df_filtered

	# function to create a waiting for customer ticket DataFrame object
	def customerTickets(self, csv):
		#print all new tickets
		df_mask=csv["Status"]=="waiting for customer"
		df_filtered=csv[df_mask]
		
		return df_filtered

	# function to create a in progress ticket DataFrame object
	def progressTickets(self, csv):
		#print all new tickets
		df_mask=csv["Status"]=="in progress"
		df_filtered=csv[df_mask]
		
		return df_filtered

	# function to create a action required ticket DataFrame object
	def actionTickets(self, csv):
		#print all new tickets
		df_mask=csv["Status"]=="action required"
		df_filtered=csv[df_mask]
		
		return df_filtered

	# function to create a DataFrame to print tickets by queue
	def ticsByQueue(self, csv, queues):
		for i in range(0,len(queues)):
			df_mask=csv["Queue"]==queues[i]
			df_filtered=csv[df_mask]
			print(queues[i])
			for row in df_filtered.itertuples():
				print(row)
			print("##################################")







