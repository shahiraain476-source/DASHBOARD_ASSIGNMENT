#IMPORT LIBRARY
import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="STUDENTS PERFORMANCE DASHBOARD",
    page_icon="📊",
    layout="wide") #more wide than before

#LOADING DATA
data= pd.read_csv("clean_data.csv")
#BACKGROUND COLOR
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg,
                                #0a001f,
                                #160033,
                                #240046);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #120028;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* KPI Cards */
div[data-testid="metric-container"] {
    background: linear-gradient(135deg, #5a189a, #ff4dd2);
    border: none;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(255,77,210,0.3);
}

/* Metric Labels */
div[data-testid="metric-container"] label {
    color: white !important;
}

/* Metric Values */
div[data-testid="metric-container"] div {
    color: white !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 15px;
}

/* Subheader */
h3 {
    color: #ff80df !important;
}

</style>
""", unsafe_allow_html=True)

#SIDEBAR TITLE
st.sidebar.markdown("""
<h3 style='text-align:left; color:white;'>
🎓 STUDENTS PERFORMANCE DASHBOARD
</h3>
""", unsafe_allow_html=True)

#NAVIGATION
page = st.sidebar.radio("Go To",
                        ["🏠 HOME",
                         "🎯 OBJECTIVE 1",
                         "🎯 OBJECTIVE 2",
                         "🎯 OBJECTIVE 3",
                         "📄 RAW DATA"])

#SIDEBAR FILTERS
st.sidebar.header("FILTERS")
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
#start filter, identify range
filtered_data=data[
    (data['Hours Studied'] >= hours_range[0]) &
    (data['Hours Studied'] <= hours_range[1]) &
    (data['Attendance'] >= attendance_range[0]) &
    (data['Attendance'] <= attendance_range[1])]

#HOME PAGE
if page == "🏠 HOME":
    #PAGE TITLE
    st.title("WELCOME TO STUDENTS PERFORMANCE DASHBOARD")
    st.write("ANALYSIS OF FACTORS AFFECTING STUDENT EXAM PERFORMANCE")
    st.write("DESIGN BY NOR AIN SHAHIRA AND SYAMEEM ZUHAIRA")
    #KPI CARDS
    st.subheader("OVERVIEW")
    col1, col2, col3, col4 = st.columns(4) # to create 4 column next to each other
    #column first
    with col1: #anything inside this will display in the first column
        with st.container(border=True):
            st.metric("👨‍🎓 TOTAL STUDENTS",
                      len(filtered_data) #counts the number of students in filtered data. we use filter
                     )
    #column second
    with col2:
        with st.container(border=True):
            st.metric("📈 AVERAGE EXAM SCORE",
                      round(filtered_data["Exam Score"].mean(),2) #Calculate the average and display
                     )
    #column third
    with col3:
        with st.container(border=True):
            st.metric("📅 AVERAGE ATTENDANCE",
                      round(filtered_data["Attendance"].mean(),2) #round to 2 decimal places
                     )
    #column fourth
    with col4:
        with st.container(border=True):
            st.metric("📚 AVERAGE STUDY HOURS",
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
        fig.update_layout(plot_bgcolor="#1a0033",
                          paper_bgcolor="#1a0033",
                          font_color="white")
        st.plotly_chart(fig)  #because use panda.express not matplotlib.pyplot
    
    # PIE CHART
    with col2:
        st.subheader("SCHOOL TYPE DISTRIBUTION")
        fig = px.pie(data,
                     names="School Type",
                     color_discrete_sequence=['purple','violet'])
        fig.update_layout(plot_bgcolor="#1a0033",
                          paper_bgcolor="#1a0033",
                          font_color="white")
        st.plotly_chart(fig)
    
    #CORRELATION CHART 
    st.subheader("CORRELATION HEATMAP") #correlation to know about the reationship
    corr_cols = ['Hours Studied',
                 'Attendance',
                 'Sleep Hours',
                 'Tutoring Sessions',
                 'Physical Activity',
                 'Exam Score']
    corr_matrix = filtered_data[corr_cols].corr() #use filter
    fig = px.imshow(corr_matrix,
                    text_auto=True,
                    color_continuous_scale="viridis")
    fig.update_layout(plot_bgcolor="#1a0033",
                      paper_bgcolor="#1a0033",
                      font_color="white")
    st.plotly_chart(fig,
                    use_container_width=True)

# OBJECTIVE 1
elif page == "🎯 OBJECTIVE 1":
    st.title("OBJECTIVE 1")
    st.write("To investigate the relationship between study hours, attendance rates and final exam scores to identify key drivers of student success.")
    col1, col2 = st.columns(2)
    # HOURS STUDIED VS EXAM SCORE
    with col1:
        st.subheader("RELATIONSHIP BETWEEN STUDY HOURS AND EXAM SCORE")
        fig = px.scatter(data,
                         x="Hours Studied", 
                         y="Exam Score", 
                         color_discrete_sequence=["purple"])
        fig.update_layout(plot_bgcolor="#1a0033",
                          paper_bgcolor="#1a0033",
                          font_color="white")
        st.plotly_chart(fig)

    #ATTENDANCE VS EXAM SCORE
    with col2:
        st.subheader("RELATIONSHIP BETWEEN ATTENDANCE AND EXAM SCORE")
        fig= px.scatter(data,
                        x="Attendance", 
                        y="Exam Score", 
                        color_discrete_sequence = ["pink"])
        fig.update_layout(plot_bgcolor="#1a0033",
                          paper_bgcolor="#1a0033",
                          font_color="white")
        st.plotly_chart(fig)

#OBJECTIVE 2
elif page == "🎯 OBJECTIVE 2":
    st.title("OBJECTIVE 2")
    st.write("To analyze the patterns of sleep hours and physical activity levels across different exam score groups among students.")
    col1, col2 = st.columns(2)
    #SLEEP HOURS
    with col1:
        st.subheader("AVERAGE STUDENTS SLEEP HOURS BY EXAM SCORE")
        sleep_score = data.groupby('Exam Score')['Sleep Hours'].mean().reset_index()
        fig=px.line(sleep_score,
                    x="Exam Score",
                    y="Sleep Hours",
                    markers=True, 
                    color_discrete_sequence=['purple'])
        fig.update_layout(plot_bgcolor="#1a0033",
                      paper_bgcolor="#1a0033",
                      font_color="white")
        st.plotly_chart(fig)

    #PHYSICAL ACTIVITY
    with col2:
        st.subheader("AVERAGE PHYSICAL ACTIVITY BY EXAM SCORE")
        activity_score = data.groupby('Exam Score')['Physical Activity'].mean().reset_index() #if there is no reset index, the exam score not a column anymore 
        fig=px.line(activity_score,
                    x="Exam Score",
                    y="Physical Activity",
                    markers=True, 
                    color_discrete_sequence=['magenta'])
        fig.update_layout(plot_bgcolor="#1a0033",
                          paper_bgcolor="#1a0033",
                          font_color="white")
        st.plotly_chart(fig)

#OBJECTIVE 3
elif page == "🎯 OBJECTIVE 3":
    st.title("OBJECTIVE 3")
    st.write("To assess the effectiveness of external support systems, such as tutoring sessions and internet access, in improving the exam scores of students with different learning needs.")
    col1, col2 = st.columns(2)
    #TUTORING SESSIONS
    with col1:
        st.subheader("AVERAGE EXAM SCORE BY TUTORING SESSIONS")
        tutoring_score = data.groupby('Tutoring Sessions')['Exam Score'].mean().reset_index() #if there is no reset index, the exam score not a column anymore
        fig=px.line(tutoring_score,
                    x="Tutoring Sessions",
                    y="Exam Score",
                    markers= True, 
                    color_discrete_sequence=['maroon'])
        fig.update_layout(plot_bgcolor="#1a0033",
                          paper_bgcolor="#1a0033",
                          font_color="white")
        st.plotly_chart(fig)

    #INTERNET ACCESS
    with col2:
        st.subheader("AVERAGE EXAM SCORE BY INTERNET ACCESS")
        internet_score = data.groupby('Internet Access')['Exam Score'].mean().reset_index() #if there is no reset index, might get error or empty plot
        fig=px.bar(internet_score, 
                    x="Internet Access",
                    y="Exam Score",
                    color_discrete_sequence=['violet'])
        fig.update_layout(plot_bgcolor="#1a0033",
                          paper_bgcolor="#1a0033",
                          font_color="white")
        st.plotly_chart(fig) #because use panda.express not matplotlib.pyplot

#DISPLAY RAW DATA
elif page == "📄 RAW DATA":
    st.subheader("RAW DATA")
    st.dataframe(data)
