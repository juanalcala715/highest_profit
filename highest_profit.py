### Juan Alcala ###
### highest_profit.py ###
### SADA ###
### 4/20/2021 ###
# PART 1
# This program opens a file (data.csv) and counts the 
# the amount of rows in the data.
# The data the deletes unnecessary rows of data and then
# counts the new rows and writes into the file.
# To make it friendlier i created a new file and wrote 
# into that keeping the old data intact and storing the new data in a new file.
import csv

# Open the file and read from the file
with open('data.csv', 'r') as csv_file:
    # name the open file
    csv_reader = csv.reader(csv_file)
    # open the file to write into the new file
    with open('new_data.csv', 'w',newline="") as new_file:
        # name the newley written file
        csv_writer = csv.writer(new_file)

        # use for loop to read through the data.csv file and use a condition statement
        for line in csv_reader:
            # use the condition statement if to get the profit data that was non-negative
            # by using the profit column
            if line[4] > '0':
                # if true then it will write the data in the new file
                csv_writer.writerow(line)
        
        # There are multipule ways to go about this I chose to
        # equal the line counters to the length of the rows of the file while I am still in the file 
        # and then printed them. Anthoer way is opening each file individually and 
        # getting the length basically as the same code.    
        line_counter = len(list(csv.reader(open('data.csv'))))
        line_counter_new_data = len(list(csv.reader(open("new_data.csv"))))
        print("First printed answer: " + str((line_counter)))
        print("Second answer non-numeric profit: " + str(line_counter_new_data))       
        #print(line_counter)
        #print(line_counter_new_data)
    csv_file.close()
    new_file.close()