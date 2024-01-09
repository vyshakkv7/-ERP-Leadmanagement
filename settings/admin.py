from django.contrib import admin
from settings import models
from .models import Companies, Course, Trainer, States, Districts, Branches, Enquiry_Source, Follow_up_status, Qualification, Batch, Syllabus,Slot


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'adress_1', 'adress_2', 'phone_number', 'Email', 'website', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('company', 'phone_number', 'Email', 'website')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   
    list_display = ('course', 'course_code', 'trainer')
    search_fields = ('course', 'course_code')
    # list_filter = ('tutor',)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(States)
class StatesAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('state_name',)

@admin.register(Districts)
class DistrictsAdmin(admin.ModelAdmin):
    list_display = ('state', 'district', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('state__state_name', 'district')

@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    list_display = ('branch', 'branch_code', 'adress', 'street', 'state', 'district', 'pincode', 'mobile_num', 'email', 'is_active')
    list_filter = ('is_active', 'state', 'district')
    search_fields = ('branch', 'branch_code', 'adress', 'street', 'state__state_name', 'district__district', 'pincode', 'mobile_num', 'email')

@admin.register(Enquiry_Source)
class EnquirySourceAdmin(admin.ModelAdmin):
    list_display = ('enquiry_source_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('enquiry_source_name',)

@admin.register(Follow_up_status)
class FollowUpStatusAdmin(admin.ModelAdmin):
    list_display = ('follow_up_status_name', 'follow_up_status', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('follow_up_status_name', 'follow_up_status')

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('qualification_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('qualification_name',)
    
@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch', 'course','tutor', 'branch', 'start_date', 'end_date', 'closed', 'is_active')
    list_filter = ('closed', 'is_active', 'branch__state', 'branch__district')
    search_fields = ('batch', 'course__course', 'branch__branch')

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('syllabus', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('syllabus',)

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('time_slot','is_active')
    list_filter = ('is_active',)
    search_fields = ('time_slot',)
