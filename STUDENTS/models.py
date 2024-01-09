from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from settings.models import *
# Create your models here.
# laptop_choice = (('y','yes'),('n','no'),)

class Students(models.Model):
    enquiry_source = models.ForeignKey(Enquiry_Source, on_delete=models.CASCADE)


    phone_num = models.CharField(max_length=100,default='')


    student = models.CharField(max_length=100,default='')
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),('O', 'Other'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Email = models.CharField(max_length=100,default='')
    alternative_email = models.EmailField(help_text="not compulsory.",blank=True, null=True)
    Adress = models.CharField(max_length=100,default='')
    Alternative_adress = models.CharField(max_length=100,help_text="not compulsory.",blank=True, null=True)
    DOB =  models.DateField(default='')
    mobile = models.CharField(max_length=100,default='')
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    district = models.ForeignKey(Districts,on_delete=models.CASCADE)
    pincode = models.CharField(max_length=100,default='',blank=True, null=True)
    whatsapp_num = models.CharField(max_length=100,default='',blank=True, null=True)


    collage_name = models.CharField(max_length=100,default='')
    year_of_pass_out = models.PositiveIntegerField(choices=[(year, year) for year in range(2000, 2024)])
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    roll_num = models.CharField(max_length=100,default='')
    reg_num = models.CharField(max_length=100,default='')


    course = models.ForeignKey(Course,on_delete=models.CASCADE)


    photo = models.ImageField(upload_to='photo/',default='')


    STUDENT_CALL_STATUS_CHOICES = (('Hot', 'Hot'),('Cold', 'Cold'),)
    student_call_status = models.CharField(max_length=4,choices=STUDENT_CALL_STATUS_CHOICES)
    next_follow_up_date = models.DateField(default='')
    to_staff =  ChainedForeignKey(
        Trainer,
        chained_field="course",  # Field to chain with (Course)
        chained_model_field="course",  # Field on Trainer model to match with
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE
    )
    comments = models.TextField(blank=True, null=True,default='')
    
    def __str__(self):
        return self.student , self.gender , self.Email , self.Adress , self.DOB , self.mobile , self.state , self.district , self.pincode

class Student_info(models.Model):
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    phone = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    laptop_choice = (('y','yes'),('n','no'),)
    does_this_student_have_laptop = models.CharField(max_length=3,choices=laptop_choice)
    is_active = models.BooleanField(default=True) 

