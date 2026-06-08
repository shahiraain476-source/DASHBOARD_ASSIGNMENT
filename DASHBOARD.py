#IMPORT LIBRARY
import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="STUDENTS PERFORMANCE DASHBOARD",
    page_icon="📊",
    layout="wide") # to make layout more wider

#LOADING DATA
data= pd.read_csv("clean_data.csv") #use data that had been clean

#PAGE TITLE
st.title("🎓STUDENTS PERFORMANCE DASHBOARD")
st.write("ANALYSIS OF FACTORS AFFECTING STUDENT EXAM PERFORMANCE")
st.write("DESIGN BY NOR AIN SHAHIRA AND SYAMEEM ZUHAIRA")

#SIDEBAR FILTERS
st.sidebar.header("Filters")
#Indentify maximum and minimum value for Study hours and Attendance
hours_min, hours_max = int(data["Hours Studied"].min()), int(data["Hours Studied"].max())
att_min, att_max = int(data["Attendance"].min()), int(data["Attendance"].max())
#Filter slider for Study Hours
hours_range=st.sidebar.slider('Hours Studied',
                              hours_min,
                              hours_max,
                              (hours_min, hours_max))
#Filter slider for Attendance
attendance_range=st.sidebar.slider('Attendance',
                                   att_min,
                                   att_max,
                                   (att_min,att_max))
#start filter indentify range
filtered_data=data[
    (data['Hours Studied'] >= hours_range[0]) &
    (data['Hours Studied'] <= hours_range[1]) &
    (data['Attendance'] >= attendance_range[0]) &
    (data['Attendance'] <= attendance_range[1])]

#KPI CARDS
st.subheader("OVERVIEW")
col1, col2, col3, col4 = st.columns(4) # to create 4 column next to each other
#column first
with col1: #anything inside this will display in the first column
    st.metric("TOTAL STUDENTS",
              len(filtered_data) #counts the number of students in filtered data. we use filter
             )
#column second
with col2:
    st.metric("AVERAGE EXAM SCORE",
              round(filtered_data["Exam Score"].mean(),2) #Calculate the average and display
             )
#column third
with col3:
    st.metric("AVERAGE ATTENDANCE",
              round(filtered_data["Attendance"].mean(),2) #round to 2 decimal places
             )
#column fourth
with col4:
    st.metric("AVERAGE STUDY HOURS",
              round(filtered_data["Hours Studied"].mean(),2)
             )

#BASIC INFORMATION
col1, col2 = st.columns(2)
#HISTOGRAM
with col1:
    st.subheader("EXAM SCORE DISTRIBUTION")
    fig = px.histogram(data, 
                       x="Exam Score",
                       color_discrete_sequence=["fuchsia"])
    st.plotly_chart(fig) #because use panda.express not matplotlib.pyplot
    
#PIE CHART
with col2:
    st.subheader("SCHOOL TYPE DISTRIBUTION")
    fig = px.pie(data,
                 names="School Type",
                 color_discrete_sequence=['purple','violet'])
    st.plotly_chart(fig)

# OBJECTIVE 1
col1, col2 = st.columns(2)
# HOURS STUDIED VS EXAM SCORE
with col1:
    st.subheader("Relationship between Study Hours and Exam Score")
    fig = px.scatter(data,
                     x="Hours Studied", 
                     y="Exam Score", 
                     color_discrete_sequence=["purple"])
    st.plotly_chart(fig)

#ATTENDANCE VS EXAM SCORE
with col2:
    st.subheader("Relationship between Attendance and Exam Score")
    fig= px.scatter(data,
                    x="Attendance", 
                    y="Exam Score", 
              color_discrete_sequence = ["pink"])
    st.plotly_chart(fig)

#OBJECTIVE 2
col1, col2 = st.columns(2)
#SLEEP HOURS
with col1:
    st.subheader("Average Students Sleep Hours by Exam Score")
    sleep_score = data.groupby('Exam Score')['Sleep Hours'].mean().reset_index()
    fig=px.line(sleep_score,
                x="Exam Score",
                y="Sleep Hours",
                markers=True, 
                color_discrete_sequence=['purple'])
    st.plotly_chart(fig)

#PHYSICAL ACTIVITY
with col2:
    st.subheader("Average Physical Activity by Exam Score")
    activity_score = data.groupby('Exam Score')['Physical Activity'].mean().reset_index()
    fig=px.line(activity_score,
                x="Exam Score",
                y="Physical Activity",
                markers=True, 
                color_discrete_sequence=['magenta'])
    st.plotly_chart(fig)

#OBJECTIVE 3
col1, col2 = st.columns(2)
#TUTORING SESSIONS
with col1:
    st.subheader("Average Exam Score by Tutoring Sessions")
    tutoring_score = data.groupby('Tutoring Sessions')['Exam Score'].mean().reset_index() #if there is no reset index, the exam score not a column anymore
    fig=px.line(tutoring_score,
                x="Tutoring Sessions",
                y="Exam Score",
                markers= True, 
                color_discrete_sequence=['maroon'])
    st.plotly_chart(fig)

#INTERNET ACCESS
with col2:
    st.subheader("Average Exam Score by Internet Access")
    internet_score = data.groupby('Internet Access')['Exam Score'].mean().reset_index() #if there is no reset index, might get error or empty plot
    fig=px.bar(internet_score,
                x="Internet Access",
                y="Exam Score",
                color_discrete_sequence=['violet'])
    st.plotly_chart(fig)

#DISPLAY RAW DATA
st.subheader("RAW DATA")
st.dataframe(data)
