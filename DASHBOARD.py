#IMPORT LIBRARY
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# PAGE TITLE
st.title("STUDENTS PERFORMANCE DASHBOARD")
st.write("ANANLYSIS OF FACTORS AFFECTING STUDENT EXAM PERFORMANCE")

#LOADING DATA
data= pd.read_csv("clean_data.csv")

#DISPLAY RAW DATA
st.subheader("RAW DATA")
st.dataframe(data)

# OBJECTIVE 1
# HOURS STUDIED VS EXAM SCORE
st.subheader("Relationship between Study Hours and Exam Score")
fig, ax = plt.subplots(figsize = (8, 6))
#Scatter plot
data.plot(
        kind='scatter',
        x='Hours Studied', 
        y='Exam Score', 
        color = 'purple',
        ax=ax
)
st.pyplot(fig)

#ATTENDANCE VS EXAM SCORE
st.subheader("Relationship between Attendance and Exam Score")
fig, ax = plt.subplots(figsize = (8, 6))
data.plot(
        kind='scatter',
        x='Attendance', 
        y='Exam Score', 
        color = 'pink',
        ax=ax
)
st.pyplot(fig)

#OBJECTIVE 2
#SLEEP HOURS
st.subheader("Average Sleep Hours by Exam Score")
sleep_score = data.groupby('Exam Score')['Sleep Hours'].mean()
fig, ax = plt.subplots(figsize = (10, 6))
sleep_score.plot(kind='line',
                 x='Exam Score',
                 y='Average Sleep Hours',
                 marker='o', 
                 color='purple',
                 linewidth= 2,
                 figsize=(8,5),
                 ax =ax)
st.pyplot(fig)

#PHYSICAL ACTIVITY
st.subheader("Average Physical Activity by Exam Score")
activity_score = data.groupby('Exam Score')['Physical Activity'].mean()
fig, ax = plt.subplots(figsize = (10, 6))
sleep_score.plot(kind='line',
                 x='Exam Score',
                 y='Average Physical Activity',
                 marker='o', 
                 color='magenta',
                 linewidth= 2, 
                 figsize=(8,5),
                 ax =ax)
st.pyplot(fig)

#OBJECTIVE 3
#TUTORING SESSIONS
st.subheader("Average Exam Score by Tutoring Sessions")
tutoring_score = data.groupby('Tutoring Sessions')['Exam Score'].mean()
fig, ax = plt.subplots(figsize = (10, 6))
tutoring_score.plot(kind='line',
                    x='Tutoring Sessions',
                    y='Exam Score',
                    marker= 'o', 
                    color='maroon',
                    linewidth= 2,
                    figsize=(8,5),
                    ax =ax)
st.pyplot(fig)

#INTERNET ACCESS
st.subheader("Average Exam Score by Internet Access")
internet_score = data.groupby('Internet Access')['Exam Score'].mean()
fig, ax = plt.subplots(figsize = (10, 6))
internet_score.plot(kind='barh',
                   x='Internet Access',
                   y='Exam Score', 
                   color='violet',
                   edgecolor='black',
                   ax =ax)
st.pyplot(fig)