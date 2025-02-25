from django.db import models

import uuid

# Create your models here. 

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True


class DistrictChoices(models.TextChoices):

    THIRUVANANTHAPURAM = 'THIRUVANANTHAPURAM','THIRUVANANTHAPURAM'

    KOLLAM ='KOLLAM','KOLLAM'

    PATHANAMTHITTA = 'PATHANAMTHITTA','PATHANAMTHITTA'

    ALAPPUZHA = 'ALAPPUZHA','ALAPPUZHA'

    KOTTAYAM = 'KOTTAYAM','KOTTAYAM'

    IDUKKI = 'IDUKKI','IDUKKI'

    ERNAKULAM = 'ERNAKULAM','ERNAKULAM'

    THRISSUR = 'THRISSUR','THRISSUR'

    PALAKKAD = 'PALAKKAD','PALAKKADU'

    MALAPPUARM = 'MALPPURAM','MALAPPURAM'

    KOZHIKODE = 'KOZHIKODE','KOZHIKODE'

    WAYANAD = 'WAYANAD','WAYANADU'

    KANNUR = 'KANNUR','KANNUR'

    KASARGOD = 'KASARGOD','KASARGOD'



class CourseChoices(models.TextChoices):

    PYTHON_DJANGO = 'PYTHON-DJANGO','PYTHON-DJANGO'

    MEARN = 'MEARN','MEARN'

    DATA_SCIENCE = 'DATA-SCIENCE','DATA-SCIENCE',

    SOFTWARE_TESTING = 'SOFTWARE-TESTING','SOFTWARE-TESTING'

class BatchChoices(models.TextChoices):
    
    PYTHON_P1 = 'PY-NOV-2024','PY-NOV-2024'

    PYTHON_p2 = 'PY-JAN-2025','PY-JAN-2025'

    MEARN_M1 = 'MEARN-NOV-2024','MEARN-NOV-2024'

    MEARN_M2 = 'MEARN-JAN-2025','MEARN-JAN-2025'

    DATA_SCIENCE_D1 = 'DS-JAN-2025','DS-JAN-2025'

    SOFTWARE_TESTING_S1 = 'ST-JAN-2025','ST-JAN-2025'

class TrainerChoices(models.TextChoices):

    PYTHON = 'ANZIL','ANZIL'

    MEARN = 'AMRITHA','AMRITHA'

    DATA_SCIENCE = 'SARATH','SARATH'

    SOFTWARE_TESTING = 'AJITH','AJITH'


class Students(BaseClass):

    profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    photo = models.ImageField(upload_to='students')

    email = models.EmailField(unique=True)

    contact = models.CharField(max_length=15)

    house_name = models.CharField(max_length=50)

    post_office = models.CharField(max_length=50)

    district = models.CharField(max_length=50,choices=DistrictChoices.choices)

    pin_code = models.CharField(max_length=6)

    adm_number = models.CharField(max_length=25)

    course = models.ForeignKey('courses.Courses',null=True,on_delete=models.SET_NULL)

    batch = models.ForeignKey('batches.Batches',null=True,on_delete=models.SET_NULL)

    # course = models.CharField(max_length=25,choices=CourseChoices.choices) #default=CourseChoices.PYTHON_DJANGO

    # batch = models.CharField(max_length=25,choices=BatchChoices.choices)

    # batch_date = models.DateField()

    join_date = models.DateField(auto_now_add=True)

    # trainer_name = models.CharField(max_length=25,choices=TrainerChoices.choices)

    trainer = models.ForeignKey('trainers.Trainers',null=True,on_delete=models.SET_NULL)

    



    def __str__(self):

        return f'{self.first_name} {self.last_name} {self.batch}'
    

    class Meta:

        verbose_name = 'Students'

        verbose_name_plural = 'Students'

        ordering = ['-id']



