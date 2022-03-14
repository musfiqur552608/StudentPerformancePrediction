from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import requests
import os
import pandas as pd
from sklearn.neural_network import MLPClassifier
import numpy as np
from requests.api import get
from .models import StudentPerformance

file = os.path.join(os.path.dirname(__file__), 'SPP.csv')


def home(request):
    return render(request, 'home.html')

#This is main function where we done everything for sentiment analysis
def studentperformance(request):
    if request.method == 'POST':
        sid = request.POST['sid']
        student_data = StudentPerformance.objects.all()
        for student_id in student_data:
            if sid == str(student_id):
                df=pd.read_csv(file)
                y = df.iloc[:,29]
                x = df.iloc[:,:29]
                model=MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
                model.fit(x,y)
                k=[student_id.sex,student_id.age,student_id.address,student_id.famsize,student_id.Pstatus,student_id.Medu,student_id.Fedu,student_id.Mjob,student_id.Fjob,student_id.reason,student_id.guardian, student_id.traveltime,student_id.studytime,student_id.failures,student_id.schoolsup,student_id.famsup,student_id.paid,student_id.activities,student_id.nursery,student_id.higher,student_id.internet,student_id.famrel,student_id.freetime,student_id.health,student_id.absences,student_id.quiz,student_id.assignment,student_id.exam1,student_id.exam2]
                kz=np.array(k).reshape(-1,29)
                print(model.predict(kz))
                k = model.predict(kz)
                perform = k[0]
                ######################################################################################
                if student_id.sex==0:
                    student_id.sex="Female"
                else:
                    student_id.sex="Male"

                if student_id.address == 0:
                    student_id.address = "Urban"
                else:
                    student_id.address = "Rural"

                if student_id.famsize == 0:
                    student_id.famsize = "LE3"
                else:
                    student_id.famsize = "GT3"
                
                if student_id.Pstatus == 0:
                    student_id.Pstatus = "Living Together"
                else:
                    student_id.Pstatus = "Apart"

                if student_id.Medu == 0:
                    student_id.Medu = "None"
                elif student_id.Medu == 1:
                    student_id.Medu = "primary education"
                elif student_id.Medu == 2:
                    student_id.Medu = "5th to 9th grade"
                elif student_id.Medu == 3:
                    student_id.Medu = "secondary education"
                else:
                    student_id.Medu = "higher education"

                if student_id.Fedu == 0:
                    student_id.Fedu = "None"
                elif student_id.Fedu == 1:
                    student_id.Fedu = "primary education"
                elif student_id.Fedu == 2:
                    student_id.Fedu = "5th to 9th grade"
                elif student_id.Fedu == 3:
                    student_id.Fedu = "secondary education"
                else:
                    student_id.Fedu = "higher education"
                
                if student_id.Mjob == 0:
                    student_id.Mjob = "Teacher"
                elif student_id.Mjob == 1:
                    student_id.Mjob = "Health"
                elif student_id.Mjob == 2:
                    student_id.Mjob = "Services"
                elif student_id.Mjob == 3:
                    student_id.Mjob = "At home"
                else:
                    student_id.Mjob = "Other"

                if student_id.Fjob == 0:
                    student_id.Fjob = "Teacher"
                elif student_id.Fjob == 1:
                    student_id.Fjob = "Health"
                elif student_id.Fjob == 2:
                    student_id.Fjob = "Services"
                elif student_id.Fjob == 3:
                    student_id.Fjob = "At home"
                else:
                    student_id.Fjob = "Other"
                
                if student_id.reason == 0:
                    student_id.reason = "Home"
                elif student_id.reason == 1:
                    student_id.reason = "Reputation"
                elif student_id.reason == 2:
                    student_id.reason = "Course"
                else:
                    student_id.reason = "Other"

                if student_id.guardian == 0:
                    student_id.guardian = "Mothee"
                elif student_id.guardian == 1:
                    student_id.guardian = "Father"
                else:
                    student_id.guardian = "Other"

                if student_id.traveltime == 1:
                    student_id.traveltime = "Less Than 15 min"
                elif student_id.traveltime == 2:
                    student_id.traveltime = "15 to 30 min"
                elif student_id.traveltime == 3:
                    student_id.traveltime = "30 min to 1h"
                else:
                    student_id.traveltime = "Greater Than 4h"

                if student_id.studytime == 1:
                    student_id.studytime = "Less Than 2h"
                elif student_id.studytime == 2:
                    student_id.studytimee = "2 to 5h"
                elif student_id.studytime == 3:
                    student_id.studytime = "5 to 10h"
                else:
                    student_id.studytime = "Greater Than 10h"
                ######################################################################################
                mydict ={
                    "mytext" : perform,
                    "sid" : sid,
                    "sex" : student_id.sex,
                    "age" : student_id.age,
                    "address" : student_id.address,
                    "famsize" : student_id.famsize,
                    "Pstatus" : student_id.Pstatus,
                    "Medu" : student_id.Medu,
                    "Fedu" : student_id.Fedu,
                    "Mjob" : student_id.Mjob,
                    "Fjob" : student_id.Fjob,
                    "reason" : student_id.reason,
                    "guardian" : student_id.guardian,
                    "traveltime" : student_id.traveltime,
                    "studytime" : student_id.studytime,
                    "failures" : student_id.failures,
                    "schoolsup" : student_id.schoolsup,
                    "famsup" : student_id.famsup,
                    "paid" : student_id.paid,
                    "activities" : student_id.activities,
                    "nursery" : student_id.nursery,
                    "higher" : student_id.higher,
                    "internet" : student_id.internet,
                    "famrel" : student_id.famrel,
                    "freetime" : student_id.freetime,
                    "health" : student_id.health,
                    "absences" : student_id.absences,
                    "quiz" : student_id.quiz,
                    "assignment" : student_id.assignment,
                    "exam1" : student_id.exam1,
                    "exam2" : student_id.exam2,
                }  
                break
              
    return render(request, 'home.html', context=mydict)

