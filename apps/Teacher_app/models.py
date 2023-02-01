from django.db import models
from apps.Acount_app.models import Teacher
from apps.Course_app.models import Courses


def STR_TO_LIST(string):

    new_list=[]

    for item in string:

        new_list.append(item)

    return new_list

def LIST_TO_STR(LIST):

    new_str=""

    for item in LIST:

        new_str += item

    return new_str

class TeachersIncome(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="teacher_income")
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,related_name="teacher_income")
    income=models.IntegerField(default=0)
    status=models.BooleanField(default=False)



    def get_income(self):


        if self.income >= 11000 and self.income <= 99999 :

            new_price=""

            new_price += str(self.income)


            new_price=STR_TO_LIST(new_price)

            new_price[-4] += ","

            new_price=LIST_TO_STR(new_price)

            return new_price



        elif self.income >= 100000 and self.income <= 999999 :

            new_price=""

            new_price += str(self.income)


            new_price=STR_TO_LIST(new_price)

            new_price[2] += ","

            new_price=LIST_TO_STR(new_price)

            return new_price

        elif self.income >= 1000000 and self.income <= 9999999:

            new_price = ""

            new_price += str(self.income)


            new_price = STR_TO_LIST(new_price)

            new_price[-4] += ","
            new_price[-7] += ","

            new_price = LIST_TO_STR(new_price)

            return new_price


        elif self.income >= 10000000:

            new_price = ""

            new_price += str(self.income)


            new_price = STR_TO_LIST(new_price)

            new_price[-4] += ","
            new_price[-7] += ","


            new_price = LIST_TO_STR(new_price)

            return new_price

        else:

            return self.income


    def __str__(self):

        return self.teacher.user.full_name
