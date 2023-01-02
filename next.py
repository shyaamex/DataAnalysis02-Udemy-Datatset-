from sales_analysis import main
import time as t




# The next class shows the menu from which options of user's choice
# are selected and operations related to those operations called from
# the previous files and executed



class next(main): 
    
    def menu(self):
            t.sleep(5)
            
            print("""
                        Enter your choice
                        ==================
                1.)  Get information about project
                2.)  Get information about the dataset
                3.)  Get number of courses with each subject
                4.)  Get number of courses provided by udemy with respect to the skillset level
                5.)  Get number of subscriber with respect to skillset level
                6.)  Get number of paid and free accounts 
                7.)  Get the most popular course with number of subscriber
                8.)  Get 10 most popular courses on Udemy
                9.)  Get the course with highest number of reviews
                10.) Get the most popular Python courses
                11.) Exit
                """)
            self.choice=int(input())
            
            if self.choice == 1:
                self.getinfo_project()
                self.menu()
                
                
            elif self.choice == 2:
                self.getinfo_dataset()
                self.menu()
                
                
            elif self.choice == 3:
                self.getcourses()
                self.menu()
                
                
            elif self.choice == 4:
                self.getcourses_level()
                self.menu()
                
                
            elif self.choice == 5:
                self.getsub_level()
                self.menu()
                
                
            elif self.choice == 6:
                self.paid_free_chart()
                self.menu()
                
                
            elif self.choice == 7:
                self.popular_course()
                self.menu()
                
                
            elif self.choice == 8:
                self.most_populor_10()
                self.menu()
                
                
            elif self.choice == 9:
                self.highest_review()
                self.menu()
                
                
            elif self.choice == 10:
                self.pop_py_course()
                self.menu()
                
                
            elif self.choice == 11:
                exit
                
                    
            else:
                print("Please, Enter a valid choice !!!")
                self.menu()             
instance=next()
instance.menu()