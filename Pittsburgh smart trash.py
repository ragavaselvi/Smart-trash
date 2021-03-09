from csv import DictReader
#Passing the Smart trash report from the WPRDC website
#We will use the dictreader object to iterate over the contents of the file and tabulate

#Create data tarcking container prior to interating over our csv

smarttrashsummary = {'neighborhood':{},'assignment_date':{}}
#Use the facility to manage our file object called qualityfile

with open('smart_trash.csv') as trashfile:
    #Pass our file objeact to the dictreader constructor,creating an interable reader object
    dreader = DictReader(trashfile)
   #Prints all the feild name

    #loop over each row ,showing contents

    for record in dreader:
        if record['zip'] not in smarttrashsummary['neighborhood']:
            print('Smart trash is located:', smarttrashsummary['neighborhood'])
            smarttrashsummary['neighborhood'][record['zip']] = 1
        else:
            smarttrashsummary['neighborhood'][record['zip']] +=1

        if record['last_updated_date'] not in smarttrashsummary['assignment_date']:
            print('Smart trash is placed:', record['assignment_date'])
            smarttrashsummary['assignment_date'][record['last_updated_date']] = 1
        else:
            smarttrashsummary['assignment_date'][record['last_updated_date']] +=1


        


print('summary of records:', smarttrashsummary)



    #print(record)
    #Remove routing codes from zip by slicing only the first 5 characters
    #Print (record['reporting year'])
    #Print(record['neighborhood'])


