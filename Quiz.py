import pandas as pd
from Questions import qlist

obj=qlist()

qstn=obj.dict1()
qstn1=obj.dict2()

class main(qlist):
    def Main():
          
        print("Welcome to the Quiz, Please enter your Name in Capital letters:")
        name=input()
        print("Hi ",name)
        print("The following quiz contains 12 questions of True/False type. You have to enter 'True' and 'False' according to your choice")
        print("Each question carries +2 marks for the correct answer and -1 for incorrect.")
        print("Please refer to the table for more information:")
        menu=["Type this if you want to skip the question",
           "Type this if you want to navigate to some other question","Type this if u have completed"
              ,"Type this if you want to see the questions you have attempted"]
        indexes=["skip","<number of the question>","finish","attempted"]
        df=pd.DataFrame(menu,index=indexes,columns=["Details"])
        print(df)
        print("Are you ready to begin?(Enter Y for yes and N for no)")
        choice=input();
        marks=1
        if choice=='Y':
            print("Great! Lets Begin ")
            i=0;
            j=0
            l=[]
            ans1=""
               
            while(True):
                i=i%12
                
                if(j==12 or ans1=='finish'):
                    break;
                b=str('Question-'+str((i+1)))
                print(list(qstn[(i+1)])[0],":",qstn[(i+1)][b])
                if(i+1 in l):
                    print("This question has already been attempted")
                    print("Enter a new choice:")
                ans1=str(input())
                if(ans1!='True' and ans1!='False' and ans1!='skip' and ans1!="attempted" and ans1!="finish" and
                   (ans1.isdigit()==False or (int(ans1)<1 or int(ans1)>12))):
                    print("Invalid Entry")
                    continue
                
                if(ans1==(qstn[(i+1)]['answer'])):
                    marks+=2
                    j+=1
                    l.append(i+1)
                    qstn1[(i+1)]['answer']=ans1
                if(ans1=="skip"):
                    i+=1
                    continue
                if(ans1.isdigit()):
                    i=int(ans1)-1
                    continue
                if(ans1=="attempted"):
                    print("These are the questions you have attempted:")
                    for i1 in range(1,13):
                        print(qstn1[i1])            
                if(ans1!=(qstn[(i+1)]['answer'])):
                    marks-=1
                    l.append(i+1)            
                    j+=1
                    qstn1[(i+1)]['answer']=ans1
                i+=1
                    
            print("Thank you for completing the Quiz.Would you like to see your marks(Y/N)")
            ch1=input()
            if(ch1=='Y'):
                print("You have scored:",marks)
            else:
                print("Thank you for playing. Please do come back again!")
        elif choice=='N':
            exit()
        else:
            print("Invalid choice entered")
            exit()
    Main()

