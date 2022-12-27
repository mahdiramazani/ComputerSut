from apps.Acount_app.models import User
from apps.Course_app.models import Courses

def count_course(request):


    if request.user.is_authenticated:

        user=request.user
        courses=Courses.objects.filter(user=user)

        if courses.exists():

            return{"c_count":courses.all().count()}
        else:

            return {"c_count":0}


    return None

