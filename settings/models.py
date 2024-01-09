# from django.contrib.auth.models import User
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User






# Create your models here.
class Companies(models.Model):
    company = models.CharField(max_length=100)
    adress_1 = models.CharField(max_length=100,null=True,blank=True)
    adress_2 = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=100)
    Email  =  models.CharField(max_length=100,null=True,blank=True)
    website = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='logos/')
    is_active = models.BooleanField(default=True)  # Add the "active" field

    def __str__(self):
        return f'{self.company}, {self.adress_1}, {self.adress_2},{self.phone_number}, {self.Email},{self.website}'
    
    class Meta:
        verbose_name_plural = "a. companies" 
        

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "k . Trainer"

class Course(models.Model):
    course = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Trainer", null=True, blank=False, related_name="trainer", limit_choices_to={"is_active": True, "groups__name":'Faculty'})


    def __str__(self):
        return f'{self.course}, {self.course_code}'
    
    class Meta:
        verbose_name_plural = "j . Course"



class States(models.Model):
    state_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.state_name
    
    class Meta:
        verbose_name_plural = "b . States" 

class Districts(models.Model):
    state = models.ForeignKey(States,on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.district
    
    class Meta:
        verbose_name_plural = "c . Districts"

class Branches(models.Model):
    branch = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=100)
    adress = models.CharField(max_length=100,null=True,blank=True)
    street = models.CharField(max_length=100,null=True,blank=True)
    state = models.ForeignKey(States,on_delete=models.CASCADE)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=100,null=True,blank=True)
    mobile_num = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True,blank=True)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return f'{self.branch}, {self.branch_code}, {self.adress},{self.street}, {self.state},{self.district},{self.pincode},{self.mobile_num},{self.email}'
        
    class Meta:
        verbose_name_plural = "d . Branches"

class Enquiry_Source(models.Model):
    enquiry_source_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.enquiry_source_name

    class Meta:
        verbose_name_plural = "e . Enquiry_Source" 

class Follow_up_status(models.Model):
    follow_up_status_name = models.CharField(max_length=100)
    status = (('y','yes'),('n','no'),)
    follow_up_status = models.CharField(max_length=100,choices=status)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return f'{self.follow_up_status_name},{self.follow_up_status}'
    
    class Meta:
        verbose_name_plural = "f . Follow_up_status"

class Qualification(models.Model):
    qualification_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.qualification_name
    
    class Meta:
        verbose_name_plural = "g . Qualification"

class Batch(models.Model):
    batch = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    tutor = ChainedForeignKey(
        Trainer,
        chained_field="course",  # Field to chain with (Course)
        chained_model_field="course",  # Field on Trainer model to match with
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE
    )
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    closed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return f'{self.batch},{self.course},{self.branch},{self.tutor}'
    
    class Meta:
        verbose_name_plural = "h . Batch"

class Slot(models.Model):
    time_slot = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.time_slot
    
    class Meta:
        verbose_name_plural = "l . Slot "

class Syllabus(models.Model):
    syllabus = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.syllabus 
    
    class Meta:
        verbose_name_plural = "i . Syllabus"


