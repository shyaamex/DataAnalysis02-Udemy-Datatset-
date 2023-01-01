import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

a="""
This Data Analysis  project  is based upon the Dataset of  Udemy.
The dataset has  details about the subjects, courses, subscribers
and  all related  information. We've played  around this data and
made some basic  analytics.  We have also  use data  visualization 
for  better  understanding  of dataset  and  to  retrieve  quality 
information.
"""

class main():
    def __init__(self):
        #Reading csv file
        self.data=pd.read_csv('udemy.csv')
        
        # Removing Dupicate values from dataset
        self.data=self.data.drop_duplicates()




#       1 Information about project
    def getinfo_project(self):
        print(a)
        
        
#       2 Information about the dataset        
    def getinfo_dataset(self):
        print(self.data.info())
        
        
        
#       3 Number of courses by subject
    def getcourses(self):
        print(self.data['subject'].value_counts())
        sea.countplot(data=self.data['subject'])
        plt.xlabel("Subjects",fontsize=13)
        plt.ylabel("Number of Courses Per Subject",fontsize=13)
        plt.xticks(rotation=90)
        plt.show()
        
        
        
#       4 Number of courses with respect to the skillset level
    def getcourses_level(self):
        print(self.data['level'].value_counts())
        sea.countplot(x=self.data['level'].value_counts(), data = self.data['level'])
        plt.xlabel("Level",fontsize=13)
        plt.ylabel("Number of Courses Per Level",fontsize=13)
        plt.xticks(rotation=65)
        plt.show()
        
        
        
#       5 Number of subscriber by skillset level
    def getsub_level(self):
        sea.barplot(x="level",y="num_subscribers",data=self.data)
        plt.xticks(rotation=60)
        plt.show()
        print("So, Beginner level has highest number of subscriber ")
    
    
    
    
#       6 Number of paid and free accounts 
    def paid_free_chart(self):
        print(self.data['is_paid'].value_counts())
        sea.countplot( data=self.data['is_paid'].value_counts())
        plt.xlabel("Level",fontsize=13)
        plt.ylabel("Number of Free And Paid Courses",fontsize=13)
        plt.xticks(rotation=65)
        plt.show()
        
        
        
#       7 Most popular course by number of subscriber
    def most_populor_10(self):
        print(self.data[self.data['num_subscribers'].max()==self.data['num_subscribers']]['course_title'])
  
  
        
#       8 10 most popular courses
    def most_populor_10(self):
        self.a=self.data.sort_values(by="num_subscribers",ascending=False).head(10)
        sea.barplot(x="num_subscribers",y="course_title",data=self.a)
        
        
        
#       9 Course with highest number of reviews
    def highest_review(self):
        plt.figure(figsize=(10,4))
        sea.barplot(x="subject",y="num_reviews",data=self.data)
        
        
        
#       10 Most popular Python courses
    def pop_py_course(self):
        self.python=self.data[self.data['course_title'].str.contains('python',case=False)].sort_values(by="num_subscribers",ascending=False).head(10)
        sea.barplot(x="num_subscribers",y="course_title",data=self.python)