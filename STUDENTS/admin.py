from django.contrib import admin
from .models import Students,Student_info

class StudentInfoInline(admin.TabularInline):
    model = Student_info
    # extra = 2

class StudentsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('GENERAL', {'fields': ['enquiry_source']}),
        ('PHONE VERIFICATION',{'fields':['phone_num']}),
        ('PERSONAL INFO',{'fields':['student','gender', 'Email', 'alternative_email', 'Adress', 'Alternative_adress', 'DOB', 'mobile', 'state', 'district', 'pincode', 'whatsapp_num']}),


        ('ACADAMIC INFO',{'fields':['collage_name', 'year_of_pass_out', 'qualification', 'roll_num', 'reg_num']}),
        ('COURSE INFO',{'fields':['course']}),
        ('PHOTO',{'fields':['photo']}),
        ('STUDENT CALL STATUS',{'fields':['student_call_status', 'next_follow_up_date','to_staff', 'comments']}),   
    ]
    # inlines = [StudentInfoInline]


class Student_infoAdmin(admin.ModelAdmin):
    list_display = ['student', 'phone', 'email', 'batch', 'does_this_student_have_laptop', 'is_active']
    list_filter = ['batch', 'does_this_student_have_laptop', 'is_active']
    search_fields = ['student', 'phone', 'email']


admin.site.register(Students, StudentsAdmin)
admin.site.register(Student_info, Student_infoAdmin)



