from django.contrib import admin

from apps.Course_app.models import Courses,CoursesChild,Category,Comment,CertificatesOfCourses,Checkout


admin.site.register(Checkout)

admin.site.register(Courses)
admin.site.register(CoursesChild)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(CertificatesOfCourses)