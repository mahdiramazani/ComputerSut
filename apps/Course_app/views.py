from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, View
from apps.Course_app.models import Courses, CoursesChild, Category, Comment, Checkout,CertificatesOfCourses
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json
from apps.Teacher_app.models import TeachersIncome
from apps.Course_app.mixins import CheckCapcityMixin,CheckStudentCourseMixin,VidoChildMixin,CheckOrderShopMixin,CheckRequestToPayMixin
from django.http import JsonResponse
from apps.Course_app.forms import DocumentInquiryForm
MERCHANT = "b3b73736-7999-4b64-b2e7-f14c42ee52a7"
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 5000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional

CallbackURL = 'http://127.0.0.1:8000/courses/verify/'


class CategoryCourse(View):

    def get(self, request, id):
        category = Category.objects.get(id=id)

        course = category.Corses.all()

        paginator = Paginator(course, 6)
        page = request.GET.get("page")

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return render(request, "Course_app/course.html", {"object_list": object_list})


class CoursesView(View):
    model = Courses
    template_name = "Course_app/course.html"

    def get(self, request):

        object_list = Courses.objects.all()

        paginator = Paginator(object_list, 6)
        page = request.GET.get("page")

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return render(request, "Course_app/course.html", {"object_list": object_list})


class CourseDetailView(View):

    def get(self, request, pk):
        context = {"student": False}

        object = Courses.objects.get(id=pk)

        object.view += 1

        object.save()
        context["object"] = object
        context["last_course"] = Courses.objects.all()[0:3]

        if request.user in object.user.all():
            context["student"] = True

        return render(request, "Course_app/course-detail.html", {"object": context})

    def post(self, request, pk):

        curses = Courses.objects.get(id=pk)
        body = request.POST.get("body")



        if body is not None:
            Comment.objects.create(user=request.user, body=body, corses=curses)

            return JsonResponse({"response":"کامنت شما با موفقیت ارسال شد"})

        return redirect(reverse("Course_app:Course_detail", kwargs={"pk": pk}))


class CourseDetailVideoView(VidoChildMixin,DetailView):
    model = CoursesChild

    template_name = "Course_app/course_video_detail.html"



class AddCourseToOrderView(CheckCapcityMixin,View):

    def get(self, request, pk):

        curses = Courses.objects.get(id=pk)

        if request.user not in curses.user.all():

            user = request.user
            course = Courses.objects.get(id=pk)
            price = str(course.price)
            price = price + "0"
            price = int(price)

            tax=(9*price)//100
            tax_price=tax+price




            if not Checkout.objects.filter(user=user, course=course).exists():

                Checkout.objects.create(user=request.user, course=course, price=int(price),total_price=tax_price)



                checkout = Checkout.objects.get(Q(user=user), Q(course=course))

                return redirect(reverse("Course_app:checkout") + f"?checkout_id={checkout.id}")

            elif Checkout.objects.filter(user=user, course=course).exists():

                checkout = Checkout.objects.get(Q(user=user), Q(course=course))

                if checkout.price != price:

                    checkout.price=price
                    checkout.total_price=tax_price
                    checkout.save()

                return redirect(reverse("Course_app:checkout") + f"?checkout_id={checkout.id}")


class CheckOutClass(CheckOrderShopMixin,View):  #ok

    def get(self, request):
        checkout_id = request.GET.get("checkout_id")

        checkout = Checkout.objects.get(id=checkout_id)

        return render(request, "Course_app/checkout.html", {"checkout": checkout})



class RequestPay(CheckRequestToPayMixin,View):

    def post(self, request, pk):

        order = Checkout.objects.get(id=pk)
        request.session["order_id"] = order.id


        if order.course.price == 0:

            order.course.user.add(request.user)
            order.is_paid=True
            if order.course.how_to_hold=="حضوری":
                order.course.capacity -= 1
                order.course.save()

            order.save()

            return redirect(order.course.get_absulot_url())

        else:

            req_data = {
                "merchant_id": MERCHANT,
                "amount": order.total_price,
                "callback_url": CallbackURL,
                "description": description,
                "metadata": {"mobile": order.user.phone}
            }
            req_header = {"accept": "application/json",
                            "content-type": "application/json'"}
            req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
                req_data), headers=req_header)
            authority = req.json()['data']['authority']
            if len(req.json()['errors']) == 0:
                return redirect(ZP_API_STARTPAY.format(authority=authority))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


class VerifyView(View):

    def get(self, request):
        t_status = request.GET.get('Status')
        order_id = request.session.get("order_id")
        order = Checkout.objects.get(id=int(order_id))

        t_authority = request.GET['Authority']
        if request.GET.get('Status') == 'OK':
            req_header = {"accept": "application/json",
                          "content-type": "application/json'"}
            req_data = {
                "merchant_id": MERCHANT,
                "amount": order.total_price,
                "authority": t_authority
            }
            req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
            if len(req.json()['errors']) == 0:
                t_status = req.json()['data']['code']
                if t_status == 100:

                    # ==========================================================
                    order.is_paid = True

                    if order.course.how_to_hold == "حضوری":
                        order.course.capacity -= 1
                        order.course.save()
                    order.course.user.add(request.user)
                    if TeachersIncome.objects.filter(Q(teacher__user=order.course.teacher.user), Q(course=order.course),
                                                     Q(status=False)).exists():

                        teacher_income = TeachersIncome.objects.get(Q(teacher__user=order.course.teacher.user),
                                                                    Q(course=order.course), Q(status=False))
                        teacher_income.income += order.price
                        teacher_income.save()

                    elif TeachersIncome.objects.filter(Q(teacher__user=order.course.teacher.user), Q(course=order.course),
                                                     Q(status=True)).exists():
                        teacher_income = TeachersIncome.objects.create(teacher=order.course.teacher,
                                                                       course=order.course)
                        teacher_income.income += order.price
                        teacher_income.save()

                    else:
                        teacher_income = TeachersIncome.objects.create(teacher=order.course.teacher,
                                                                       course=order.course)
                        teacher_income.income += order.price
                        teacher_income.save()

                    order.save()

                    return redirect((order.course.get_absulot_url()))

                #=============================================================

                elif t_status == 101:

                    return redirect((order.course.get_absulot_url()))

                else:
                    return HttpResponse('Transaction failed.\nStatus: ' + str(
                        req.json()['data']['message']
                    ))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
        else:
            return redirect(order.course.get_absulot_url())


class DocumentInquiryView(View):

    def post(self,request):
        form = DocumentInquiryForm(data=request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            doucoment_number=cd.get("doucoment_number")



            return redirect(reverse("Course_app:document")+f"?document_number={doucoment_number}")


        return render(request, "Course_app/document_inquiry.html", {"form": form})

    def get(self,request):
        form=DocumentInquiryForm()


        return render(request,"Course_app/document_inquiry.html",{"form":form})


class DocumentView(View):

    def get(self,request):
        document_number=request.GET.get("document_number")
        object_list=CertificatesOfCourses.objects.get(document_number=document_number)

        return render(request,"Course_app/Document.html",{"item":object_list})