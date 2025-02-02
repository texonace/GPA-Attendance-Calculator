import streamlit as gui
import pandas
import math

#How-To-Use Text Variable
how_to_use_data = "1. Enter the number of subjects you have for the semester.\n2. Enter the number of classes you have for each subject\
    for each day.\n3. Enter the number of weeks you have college.\n4. :red[Note:] A 'week' is considered from Monday to Saturday\
    and a 'working week' is any week that has one or more classes classes scheduled in any of the days.\
    \n5. For a given 'work week' any day that does not have any classes scheduled is considered as a non-working\
    day/Holiday.\n6. You will count the the total number of non-working days' for Monday's, Tuesday's, Wednesday's, Thursday's,\
    Friday's, and Saturday's.\n7. You will add the number of non working days' for each day of the week in the table below\
    \n".title()+"8. :red[Note:]"+"If your Classes start and/or end in the middle of the week, then even that week is considered as\
    a full working weeks, and those days that the college has not started and/or the days left in the week after college\
    ended as non working days and add it to the tally of non-working days. Similarly if your exams conclude and/or begin in the middle\
    of the week(weeks) then consider the days of the exam as non-working days(Not required if your exam is an entire\
    working-week or occurs after completion of all classes. Do not consider the week which has all the days as\
    working-weeks in your tally of working weeks).\n9. Entering Subject Name is Optional, Calculate Lab Attendance by\
    considering labs as different subjects.".title()

user_warning = ':red[WARNING:] THIS IS JUST AN ESTIMATE TO CALCULATE THE NUMBER OF CLASSES YOU MAY HAVE FOR THE SEMESTER. YOUR CLASSES CAN VARY\
    AND DEVIATE FROM THE TIME-TABLE, DUE TO CIRCUMSTANCES YOUR ACTUAL NUMBER OF CLASSES MAY INCREASE OR DECRESASE\
    PLEASE ENSURE THAT YOU ARE MONITORING YOUR ACTUAL ATTENDANCE IN YOUR INSTITUTION\'S PORTAL.\
    THIS WEBSITE MAY ONLY BE USED AS A REFERENCE TO GET AN ESTIMATE OF THE NUMBER OF CLASSES YOU MAY IN AN IDEAL\
    SEMESTER. ACTUAL CLASSES WILL ALWAYS VARY.'

open_sourece_plee = "Thank you for visiting this site. Please take some of your time to read and contribute to Open Source Foundations\
    and organisations who are the White Knights of Computer Programming. GCC, LLVM, Python, Rust, Linux Kernel, FreeBSD, OpenBSD,\
    NetBSD, Android, VS Code, Git, Eclipse,Node.js, TensorFlow, PyTorch, Scikit-learn, Pandas, Kubernetes, Docker,Blender, GIMP,\
    FFmpeg, OpenCV, Redis, Apache Kafka, are just some of the examples of what great people have created,\
    who were at one point were just like you sitting at their computer, Overflowing with passion and determinance, Who made\
    the world of computers as great as it is today!".title()


#Header Display
gui.title("Total Classes Calculator")
gui.write("A Web Application to estimate the Number of classes for each subject in the semester".title())
gui.divider()


#Explaining What to do
gui.header("How To Use It?")
gui.write(how_to_use_data)
gui.divider()


#Data Input
gui.subheader("Enter Subject Details".title())
no_of_subjects = gui.number_input("Enter the number of subjects you have you have for the semester.", min_value=1, max_value=15)
data_table_list = []
for i in range(no_of_subjects):
    data_table_list.append({
    "Subject Name":f"{i+1}",
    "Monday":10, 
    "Tuesday":10, 
    "Wednesday":10, 
    "Thursday":10,
    "Friday":10,
    "Saturday":10})
pandas_data_frame = pandas.DataFrame(data_table_list)
gui.caption("Enter the no. of classes you have for each subject for each day.")
data_frame = gui.data_editor(pandas_data_frame,hide_index=True)
gui.divider()


#Week Details
gui.subheader("Enter Working-Week details".title())
no_of_weeks = gui.number_input(label="Entet the no. of full working weeks you have", min_value=1, max_value= 50, value=5)
minimum_percentage = gui.number_input(label="Enter the Minimum Percentage required for the subjects.", min_value=60, max_value=100, step=5, value=75)

gui.caption(':red[Note:] Even if you have only one day or one class in that entire week then you must\
             consider that week, only leave those weeks in which all the days are exhausted by exams or\
             holidays or combination of both')

gui.subheader("For each day of the week enter the number of days that you have Holidays/No classes".title())
data_table_list = [{
    "Monday":2, 
    "Tuesday":2, 
    "Wednesday":2, 
    "Thursday":2,
    "Friday":2,
    "Saturday":2}]
pandas_data_table_list = pandas.DataFrame(data_table_list)
gui_data_table_list = gui.data_editor(pandas_data_table_list, hide_index=True)


#Calculating No. of Working Days
actual_working_days = []
i = 0
for subject in data_frame["Subject Name"].tolist():
    actual_working_days.append({
        "Subject Name": f"{subject}",
        "Monday":       data_frame["Monday"].tolist()[i]*no_of_weeks - gui_data_table_list["Monday"][0],
        "Tuesday":      data_frame["Tuesday"].tolist()[i]*no_of_weeks - gui_data_table_list["Tuesday"][0],
        "Wednesday":    data_frame["Wednesday"].tolist()[i]*no_of_weeks - gui_data_table_list["Wednesday"][0],
        "Thursday":     data_frame["Thursday"].tolist()[i]*no_of_weeks - gui_data_table_list["Thursday"][0],
        "Friday":       data_frame["Friday"].tolist()[i]*no_of_weeks - gui_data_table_list["Friday"][0],
        "Saturday":     data_frame["Saturday"].tolist()[i]*no_of_weeks - gui_data_table_list["Saturday"][0]
    })
    i += 1

gui.write("Total number Of Actual Working Days:")
pandas_data_frame = pandas.DataFrame(actual_working_days)
working_days_frame = gui.data_editor(pandas_data_frame, hide_index=True)
gui.divider()

total_days_per_subject ={}

i = 0
for subject in actual_working_days:
    total_days_per_subject[subject["Subject Name"]] = (subject['Monday'] + subject['Tuesday'] + 
    subject['Wednesday'] + subject['Thursday'] + subject['Friday']+subject['Saturday'])


#Displaying Final Data
gui.header("Below are the number of working days for the semester!".title())
bunk_data = []
for subject, days in total_days_per_subject.items():
    bunk_data.append({
        "Subject Name": f"{subject}",
        "Total number of classes":days,
        "Number Of Classes Required to Attend": math.floor(days * (minimum_percentage / 100)),
        "Number of classes that may be left": days - math.floor(days * (minimum_percentage / 100))
    })

panda_bunk_data = pandas.DataFrame(bunk_data)
gui.dataframe(panda_bunk_data, hide_index=True)
gui.divider()

#Warnings and sign off
gui.write(user_warning)
gui.write(open_sourece_plee)
gui.markdown("<p style='text-align: center; color: grey; margin-bottom: 5px'>Developed By Neeraj R Rugi</p>", unsafe_allow_html=True)
gui.markdown("<p style='text-align: center; color:grey; margin-top:1px'>Under MIT License</p>", unsafe_allow_html=True)

