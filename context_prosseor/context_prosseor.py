from apps.Acount_app.models import User
from apps.Course_app.models import Courses,Category
from apps.Course_app.models import Checkout


def get_order_shop(request):
    if request.user.is_authenticated:
        user=request.user

        if Checkout.objects.filter(user=user):

            checkout=Checkout.objects.filter(user=user,is_paid=False)
            count=checkout.all().count()


            return {"checkout":checkout,"count_ch":count}

        else:

            return {"checkout": None, "count_ch": 0}

    else:

        return None

def count_course(request):


    if request.user.is_authenticated:

        user=request.user
        courses=Courses.objects.filter(user=user)

        if courses.exists():

            return{"c_count":courses.all().count()}
        else:

            return {"c_count":0}


    return {"c_count":0}

def category_list(request):


    try:
        cat = Category.objects.all()

        return {"category": cat}

    except TypeError:

        return None




