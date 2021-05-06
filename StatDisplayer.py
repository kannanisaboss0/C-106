#-------------------------------------------------------------StatDisplayer.py-------------------------------------------------------------#
'''
Importing modules:
-csv
-pandas [pd]
-numpy  [np]
-plotly.express [pe]
-os
-webbrowser
-time
-Counter (from collections)
-math
'''
import csv
import pandas as pd
import numpy as np 
import plotly.express as pe
import os
import webbrowser
import time
from collections import Counter
import math



#Definng the main function
def PerformStatistics(file_name_arg):

    #Informing the user
    print("Starting process...")
    time.sleep(2.1)

    #Opening the file for reading the data, storing the data in a list and finding the length of the list
    with open(file_name_arg) as d_1:
        reader=csv.reader(d_1)
        data_stats_list=list(reader)
        data_stats_list_length=len(data_stats_list)

        #Defining and printing the two corresponding column names/labels
        data_set_title_1=data_stats_list[0][0]
        data_set_title_2=data_stats_list[0][1]
        print("The columns are '"+str(data_set_title_1)+"' and '"+str(data_set_title_2)+"'.")
        #Removing the column names/labels to reduce the margin of error
        data_stats_list.pop(0)

        #Delcaring two empty lists to store the data from the columns
        data_set_1=[]
        data_set_2=[]

        #Stroing the data in the lists 
        for row in range(1,len(data_stats_list)):
            data_set_1.append(float(data_stats_list[row][0]))
            data_set_2.append(float(data_stats_list[row][1]))

        #Correlative Coefficient
        print("Calculating the correlative coefficient...")
        time.sleep(5.6)
        
        #Creating a dictionary object to store the data of the datasets
        dict_stat_object={"data_1":data_set_1,"data_2":data_set_2}

        #Findng and printing the correlative coefficient
        correlation=np.corrcoef(dict_stat_object["data_1"],dict_stat_object["data_2"])
        correlation_range=correlation[0,1] 
        print("The correlation coefficient is:"+str(round(correlation_range,2)))

        #Verifying wether if the correlative coefficient is inverse(-1,0) or direct(0,1)
        #Case 1
        if(float(correlation_range)<0):
            print("The two datasets are inversely proportional")
            inverse_correlation_coefficient_percentage=(correlation_range/-1)*100
            print("The correlation percentage is:"+str(round(inverse_correlation_coefficient_percentage,2))+" %")
        #Case 2    
        elif(float(correlation_range)>0):
            print("The two datasets are directly proportional")
            direct_correlation_coefficient_percentage=(correlation_range/1)*100
            print("The correlation percentage is:"+str(round(direct_correlation_coefficient_percentage,2))+" %")

        #Mean Value
        print("Calculating the mean value...")
        time.sleep(5.6)

        #First dataset
        #Declaring a variable and running a loop over the first dataset to find the sum
        data_set_sum_1=0
        for value_1 in data_set_1:
            data_set_sum_1=data_set_sum_1+int(value_1)

        #Dividing the sum by the length of the first dataset    
        data_set_mean_1=data_set_sum_1/data_stats_list_length 

        #Printng the mean value of the first dataset   
        print("The mean of the first data set is:"+str(round(data_set_mean_1,2)))
             
        #Second dataset  
        #Declaring a variable and running a loop over the second dataset to find the sum   
        data_set_sum_2=0
        for value_2 in data_set_2:
            data_set_sum_2=data_set_sum_2+int(value_2)

        #Dividing the sum by the length of the second dataset    
        data_set_mean_2=data_set_sum_2/data_stats_list_length 

        #Printng the mean value of the second dataset 
        print("The mean of the second data set is:"+str(round(data_set_mean_2,2)))

        #Findng the mean value of the mean value of the first and second datasets
        data_set_all_mean=(data_set_mean_1+data_set_mean_2)/2 

        #Printing the value of the aforementioned mean
        print("The overall mean is:"+str(round(data_set_all_mean,2)))

        #Standard Deviation
        print("Calcualting the standard deviation...")
        time.sleep(5.6)

        #Declaring a variable and running a loop over the first dataset to find the sum of the square of the difference between the each value of the first dataset and its mean
        for sd_value_1 in data_set_1:
            difference_1=int(sd_value_1)-data_set_mean_1
            difference_1=difference_1**2
            sum_1=difference_1+sum_1

        #Finding the quotient of aforementioned sum and the length of the first dataset
        quotient_1=sum_1/data_stats_list_length

        #Findng the standard deviation by findng square root of the quotient
        standard_deviation_1=math.sqrt(quotient_1)

        #Printing the standard deviation of the first dataset
        print("The standard deviation of the first data set is:"+str(round(standard_deviation_1,2)))

        #Declaring a variable and running a loop over the second dataset to find the sum of the square of the difference between the each value of the second dataset and its mean
        sum_2=0
        for sd_value_2 in data_set_2:
            difference_2=int(sd_value_2)-data_set_mean_2
            difference_2=difference_2**2
            sum_2=difference_2+sum_2

        #Finding the quotient of aforementioned sum and the length of the second dataset
        quotient_2=sum_2/data_stats_list_length

        #Findng the standard deviation by findng square root of the quotient
        standard_deviation_2=math.sqrt(quotient_2)

        #Printing the standard deviation of the first dataset
        print("The standard deviation of the second data set is:"+str(round(standard_deviation_2,2)))

        #Finding and printing the mean of both the standard deivstions of the first and second dataset
        standard_deviation_mean=(standard_deviation_1+standard_deviation_2)/2
        print("The overall standard deviation is:"+str(round(standard_deviation_mean,2)))



        #Median Value
        print("Calculating the median value...")
        time.sleep(5.6)

        #Sorting the elements of the first dataset
        data_set_1.sort()

        #Finding the length of the first dataset
        data_set_1_length=len(data_set_1)

        #Setting a variable for the median of the first dataset
        data_set_median_1=0

        #Checking wether the length of the first dataset is even  or odd
        #Case 1
        if(data_set_1_length%2==0):
            data_set_1_median_1=data_set_1[int(data_set_1_length/2)]
            data_set_1_median_2=data_set_1[int((data_set_1_length/2)-1)]
            data_set_1_median=(data_set_1_median_1+data_set_1_median_2)/2 
            print("The number of entries for the first dataset is odd") 
            print("The median of the first dataset is:"+str(round(data_set_1_median,2)))   
        #Case 2    
        elif(int(data_set_1_length%2!=0)):
            data_set_1_median=data_set_1[int(data_set_1_length/2)]
            print("The number of entries for the first dataset is even") 
            print("The median of the first dataset is:"+str(round(data_set_1_median,2))) 

        #Sorting the elements of the second dataset
        data_set_2.sort()

        #Finding the length of the second dataset
        data_set_2_length=len(data_set_2)

        #Setting a variable for the median of the second dataset
        data_set_2_median=0

        #Checking wether the length of the second dataset is even  or odd
        #Case 1
        if(data_set_2_length%2==0):
            data_set_2_median_1=data_set_1[int(data_set_2_length/2)]
            data_set_2_median_2=data_set_1[int((data_set_2_length/2)-1)]
            data_set_2_median=(data_set_1_median_1+data_set_1_median_2)/2 
            print("The number of entries for the second dataset is odd") 
            print("The median of the second dataset is:"+str(round(data_set_2_median,2))) 
        #Case 2       
        elif(int(data_set_2_length%2!=0)):
            data_set_2_median=data_set_2[int(data_set_2_length/2)] 
            print("The number of entries for the second dataset is even") 
            print("The median of the second dataset is:"+str(round(data_set_2_median,2))) 

        #Finding and printing the mean of both the medians of the first and second datasets
        data_set_all_median_mean=(data_set_1_median+data_set_2_median)/2 
        print("The overall median is:"+str(round(data_set_all_median_mean,2)))

        #Closing the file momentarily
        d_1.close()

        #Mode Value
        print("Calculating the mode value...")
        time.sleep(5.6)

        #Opening the file for calculating the mode
        with open(file_name_arg) as d_2:
            reader_mode=csv.reader(d_2)
            data_stat_mode_list=list(reader_mode)

            #Declaring two empty lists for calculating mode
            data_set_1_mode=[]
            data_set_2_mode=[]

            #Storing the data in the lists 
            for row_purpose_mode in range(1,len(data_stat_mode_list)):
                data_set_1_mode.append(data_stat_mode_list[int(row_purpose_mode)][0])
                data_set_2_mode.append(data_stat_mode_list[int(row_purpose_mode)][1])
            
            #Setting a counter for the first dataset and extracting values from it
            data_set_1_mode_counter=Counter(data_set_1_mode)
            data_set_1_mode_counter_values=data_set_1_mode_counter.values()
            data_set_1_mode_counter_items=data_set_1_mode_counter.items()

            #Running a for loop over the first dataset to find the most frequently occuring value
            for name_mode_1,value_mode_1 in data_set_1_mode_counter_items:

                #Verifying wether the most frequently occuring element repeates itself more than one time
                #Case 1
                if(int(max(data_set_1_mode_counter_values))==1):
                    print("There are no values which are repetitive in the first dataset")
                    break
                #Case 2    
                else:
                    if(value_mode_1==max(data_set_1_mode_counter_values)):
                        print("The mode for the second dataset is:"+str(name_mode_1)+" at "+str(value_mode_1)+" times")
                        break

            #Setting a counter for the second dataset and extracting values from it
            data_set_2_mode_counter=Counter(data_set_2_mode)
            data_set_2_mode_counter_values=data_set_2_mode_counter.values()
            data_set_2_mode_counter_items=data_set_2_mode_counter.items()

            #Running a for loop over the second dataset to find the most frequently occuring value
            for name_mode_2,value_mode_2 in data_set_2_mode_counter_items:

                #Verifying wether the most frequently occuring element repeates itself more than one time
                #Case 1
                if(int(max(data_set_2_mode_counter_values))==1):
                    print("There are no values which are repetitive in the second dataset")
                    break
                #Case 2    
                else:
                    if(value_mode_2==max(data_set_2_mode_counter_values)):
                        print("The mode for the second dataset is:"+str(name_mode_2)+" at "+str(value_mode_2)+" times")
                        break

        #Notifying the user about the sicces in completion
        print("All statistics have been generated")

        #Printing the ending message
        print("Thank You for using StatDisplayer.py")



#Writing the main code
#Printing the introductory messages,adding a delay to each message and providing guidelines
print("Welcome to StatDisplayer.py, we provide statistical data of files with the extension '.csv'. ")
time.sleep(2.2)
print("Below mentioned are some guidelines we recommend to abide by for the best experience:")
time.sleep(2.2)
print("1. The program is compatible with files of type 'coma seperated values' or '.csv' only")
time.sleep(2.2)
print("2. While writing or pasting or uploading the data, we recommend only two columns as the program only accounts for the first two columns of the data provided.")
time.sleep(2.2)
print("3. We recommend to provide the columns with names/labels as the program can use it as identification.")
time.sleep(2.2)
print("That is all which is required for a smooth performance.")
time.sleep(0.5)
print("Have A Good Day.")
time.sleep(1.0)

#Declaring an list to display the choices available
primary_choice=["Uniterable_Protective_Element","Create A File","Upload A File"]

#Declaring a variable to represent the index
primary_choice_count=0

#Running a for loop over the list
for choice in primary_choice[1:]:
    #Increasing the count by one
    primary_choice_count+=1
    #Printing all the elements, except the first
    print(str(primary_choice_count)+":"+choice)

#Declaring an input for the users
user_choice=int(input("Please enter the index of the method through which the files should be uploaded:"))

#Analysing the input provided by the user
#Case 1
if(user_choice==1): 
    #Displaying the user's choice
    print("Create A File")

    #Declaring an input which holds the name of the file and splitting it into the root name and the extension name
    file_name=input("Please enter the name of the file to create:")
    print("Creating "+file_name+"...")
    file_root,file_ext=os.path.splitext(file_name)

    #Verifying whether the file has the correct extension name
    #Case 1
    if(file_ext==".csv"):

        #Creating the file using write mode
        with open(file_name,'w') as w_1:

            #Notifying the user that the file has been generated and asking them to paste the data in the file created
            print(file_name+" has been generated.")
            print("Please paste the required data in the file.")

            #Notifying the user about the circumstances and closing the file
            print("The application only supports two columns of data as most of the calculations conducted are eligible for two seprate sets of data, in this case, columns.")
            w_1.write("Please paste the data here(delete this line as well)")
            w_1.close()

        #Asking the user wether they have pasted the data and to continue to the program    
        continue_execution=input("Once the data has been pasted, please press 'Enter' to continue")

        #Calling the main function and passing the parameter
        PerformStatistics(file_name)

    #Case 2
    else:
        #Declaring a variable containing the file root and desireable extension
        concantenated_file_name=file_root+".csv"

        #Notifying the user of their error
        print("Invalid file extension.")

        #Describing the error conducted by the user
        print("The program only supports files with the extension '.csv'")

        #Providing them and executing the corrective measures
        print("Changing file extension to '.csv'...")
        print("Tansferal complete.")

        #Creating the file using write mode
        with open(concantenated_file_name,'w') as w_2:

            #Notifying the user that the file has been generated and asking them to paste the data in the file created
            print(concantenated_file_name+" has been generated.")
            print("Please paste the required data in the file.")

            #Notifying the user about the circumstances and closing the file
            print("The application only supports two columns of data as most of the calculations conducted are eligible for two seprate sets of data, in this case, columns.")
            w_2.write("Please paste the data here(delete this line as well)")
            w_2.close()
         

        #Asking the user wether they have pasted the data and to continue to the program    
        continue_execution=input("Once the data has been pasted, please press 'Enter' to continue")

        #Calling the main function and passing the parameter
        PerformStatistics(concantenated_file_name)
    
        
#Case 2      
elif(user_choice==2):

    #Displaying the user's choice
    print("Upload A File")

    #Notifying them about opening a web browser to "Kaggle.com"
    print("Opening Kaggle in Browser...")
    print("Kaggle.com is an amazing website where countless datasets, including csv datasets, can be accessed and downloaded mostly for free!")
    time.sleep(3.6)

    #Opening the web-browser to "Kaggle.com"
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s ' ).open("https://www.kaggle.com/")

    #Verifying with the user about the name of the file
    file_name=input("Please enter the name of the file uploaded:") 

    #Getting the current path
    current_path=os.getcwd()

    #Verifying wehter the path(file) exists or not

    #Case 1
    if(os.path.exists(current_path+'/'+file_name)):

        #Notifying the user about the success 
        print("The file has been found.")
        print("Accessing "+str(file_name)+"...")
        print("Acces attained.")

        #Calling the main function and passing the parameter
        PerformStatistics(file_name)

    #Case 2    
    else:
        #Denying the user's request
        print("Request Terminated.")

        #Metioning the reason of denial
        print("The file mentioned does not exist.")

        #Printing the ending message
        print("Thank You for using StatDsiplayer.py.") 

#Case 3           
else:
    #Denying the user's request
    print("Request Terminated.")

    #Metioning the reason of denial
    print("Invalid Input.") 

    #Printing the ending message
    print("Thank You for using StatDsiplayer.py.")        
#-------------------------------------------------------------StatDisplayer.py-------------------------------------------------------------#
