"""
A gui program to calculate your GPA.
"""
import streamlit as gui
import pandas
import math

open_sourece_plee = "Thank you for visiting this site. Please take some of your time to read and contribute to Open Source Foundations\
    and organisations who are the White Knights of Computer Programming. GCC, LLVM, Python, Rust, Linux Kernel, FreeBSD, OpenBSD,\
    NetBSD, Android, VS Code, Git, Eclipse,Node.js, TensorFlow, PyTorch, Scikit-learn, Pandas, Kubernetes, Docker,Blender, GIMP,\
    FFmpeg, OpenCV, Redis, Apache Kafka, are just some of the examples of what great people have created,\
    who were at one point were just like you sitting at their computer, Overflowing with passion and determinance, Who made\
    the world of computers as great as it is today!"

try:
    def round_up_half(value):
        # If the decimal part is exactly 0.5, round up
        if value % 1 == 0.5:
            return math.ceil(value)
        else:
            return round(value)

    def calculate(no_of_subjects, data_frame):
        #Grade data Processing
        gpa_per_subject = []
        data_per_subject = zip(
            data_frame["Subject Name"].tolist(),
            data_frame["Maximum Theory Marks"].tolist(),
            data_frame["Theory Marks Obtained"].tolist(),
            data_frame["Maximum Lab Marks (if any)"].tolist(),
            data_frame["Lab Marks Obtained (if any)"].tolist(),
            data_frame["Number of Attainable Credits"].tolist(),
            data_frame["Passing marks out of 100"].tolist())

        for subject in data_per_subject:
            marks_attained = round_up_half(((subject[2] + subject[4])/(subject[1] + subject[3]))*100)
            grade_point_of_subject = ((marks_attained//10 +1) if marks_attained / 10 != 10 else 10) if marks_attained >= subject[6] else 0
            credit_hour  = subject[5] * grade_point_of_subject
            gpa_per_subject.append(credit_hour)

        #Displaying Data
        gui.subheader("Grade-Point per subject:")
        for grade in range(no_of_subjects):
            gui.write(f'Grade point for subject {data_frame["Subject Name"].tolist()[grade]} is: {gpa_per_subject[grade]}')

        #Final Output:
        col1, col2  = gui.columns(2)
        final_gpa = 0
        final_gpa = sum(gpa_per_subject) / sum(data_frame["Number of Attainable Credits"].tolist())
        gui.header("Your Finale Grade Is")
        col1.metric("Grade Point Average in 10 point scale: ", round(final_gpa, 2))
        col2.metric("Grade Point Average ina a 4 point scale:", (round(final_gpa, 2)/ 10) * 4)
        
        
        if final_gpa >= 7:
            gui.subheader("Congrats! You Did Well :grinning:")
        elif final_gpa >=5:
            gui.subheader("You Did Fair But Try Harder Next Time You Got This!")
        else:
            gui.subheader("Bruh You Cooked LMAO")  
        gui.write(':red[Note:] The 4 point GPA is an estimate based on the 10 point scale and will vary slightly with your actual 4 point GPA.')
        gui.write(open_sourece_plee)
        gui.markdown("<p style='text-align: center; color: grey; margin-bottom: 5px'>Developed By Neeraj R Rugi</p>", unsafe_allow_html=True)
        gui.markdown("<p style='text-align: center; color:grey; margin-top:1px'>Under MIT License</p>", unsafe_allow_html=True)

    #Gui Display and Subject Input
    gui.title('GPA Calculator', anchor=False)
    gui.write('A tool to calculate your GPA for 10 point system')
    gui.divider()
    gui.write('\n\n')
    gui.subheader('How Many Subjects Do You Have This Semester?', anchor= False)
    no_of_subjects = gui.number_input(label="Enter the number of subjects", min_value=1, max_value=15)
    gui.divider()


    #Editable Subject Data 
    gui.caption("Enter the data for each Subject:")
    gui.caption(":red[_Note:_]\n1. If the subject does not have a lab component then just just set the both lab releated coloumns to 0\n2. You Need not enter the names of the subject")
    data_table_list = []
    for i in range(no_of_subjects):
        data_table_list.append({
        "Subject Name":f"{i+1}",
        "Maximum Theory Marks":100, 
        "Theory Marks Obtained":55, 
        "Maximum Lab Marks (if any)":20, 
        "Lab Marks Obtained (if any)":15,
        "Number of Attainable Credits":5,
        "Passing marks out of 100":40})
    pandas_data_frame = pandas.DataFrame(data_table_list)
    data_frame = gui.data_editor(pandas_data_frame, hide_index=True)
    go_button = gui.button("Go!")
    gui.divider()
    if go_button:
        calculate(no_of_subjects, data_frame)
except ZeroDivisionError:
    gui.warning("Error: Please Ensure Total attainable Marks are not 0")
except ValueError:
    gui.warning("Please Enter an appropriate Value")
except:
    gui.warning('Some Error Occured')