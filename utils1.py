# Importing required modules 
import csv 
from datetime import datetime 
filename ='result.csv'


# function to write in csv file 
def write_in_csv(rows): 

	# Opening the CSV file in read and 
	# write mode using the open() module 
	with open(filename, 'a', newline='') as file: 

		# creating the csv writer 
		file_write = csv.writer(file) 

		# Iterating over all the data in the rows 
		# variable 
		for val in rows: 
			
			# writing the data in csv file 
			file_write.writerow(val) 

def saving_result2(data,mode='Real Time'):
    # list to store the values of the rows 
    rows = [] 

    # while loop to take 
    # inputs from the user 
    run = '' 
    while run != 'no':

        # lists to store the user data 
        val = [] 
        
        val1= data
        val2=mode

        # storing current date and time 
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %I:%M %p' )
		

        # Appending the inputs in a list 
        val.append(formatted_time)
        val.append(val2) 
        val.append(val1)

        # Taking input to add one more row 
        # If user enters 'no' then the will loop will break 

        # Adding the stored data in rows list 
        rows.append(val)
        run = 'no'
    write_in_csv(rows) 


saving_result2("sad")