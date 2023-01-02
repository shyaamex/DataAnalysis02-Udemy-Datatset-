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
        #Reading csv file, Now csv file is readed as pandas dataframe 
        # and it will be used in whole project.
        self.data=pd.read_csv('udemy.csv')
        
        # Removing Dupicate values from pandas dataframe(readed csv file) 
        # This is the basic cleaning of data
        self.data=self.data.drop_duplicates()




#       1 This method contains introduction to what this project is all about
    def getinfo_project(self):
        print(a)
        
        
#       2 This method contains information about the dataframe, 
#         All about the columns and their data types       
    def getinfo_dataset(self):
        print(self.data.info())
        
        
        
#       3 This method tells us about the number of courses each subject contains
#         and it is also consist of visual representations of data
    def getcourses(self):
        print(self.data['subject'].value_counts())
        sea.countplot(data=self.data['subject'])
        plt.xlabel("Subjects",fontsize=13)
        plt.ylabel("Number of Courses Per Subject",fontsize=13)
        plt.xticks(rotation=90)
        plt.show()
        
        
        
#       4 This method will return number of courses with respect to the skillset 
#         level and also contains visual representation of the data
    def getcourses_level(self):
        print(self.data['level'].value_counts())
        sea.countplot(x=self.data['level'].value_counts(), data = self.data['level'])
        plt.xlabel("Level",fontsize=13)
        plt.ylabel("Number of Courses Per Level",fontsize=13)
        plt.xticks(rotation=65)
        plt.show()
        
        
        
#       5 This method will evaluate number of subscriber by skillset 
#         level with Bar graph
    def getsub_level(self):
        sea.barplot(x="level",y="num_subscribers",data=self.data)
        plt.xticks(rotation=60)
        plt.show()
        print("So, Beginner level has highest number of subscriber ")
    
    
    
    
#       6 This method returns dumber of paid and free accounts 
    def paid_free_chart(self):
        print(self.data['is_paid'].value_counts())
        
        
        
        
#       7 this method returns most popular course by number of subscriber
    def popular_course(self):
        print("\nSubs        Course name\n")
        print(self.data[self.data['num_subscribers'].max()==self.data['num_subscribers']]['course_title'])
  
  
        
#       8 This method shows 10 most popular courses on bar graph
    def most_populor_10(self):
        self.a=self.data.sort_values(by="num_subscribers",ascending=False).head(10)
        sea.barplot(x="num_subscribers",y="course_title",data=self.a)
        plt.show()
        
        
        
#       9 This method tells about the dourse with highest number of reviews with the help of bar graph
    def highest_review(self):
        plt.figure(figsize=(10,4))
        sea.barplot(x="subject",y="num_reviews",data=self.data)
        plt.show()
        
        
        
#       10 this method returns most popular Python courses
    def pop_py_course(self):
        self.python=self.data[self.data['course_title'].str.contains('python',case=False)].sort_values(by="num_subscribers",ascending=False).head(10)
        sea.barplot(x="num_subscribers",y="course_title",data=self.python)
        plt.show()