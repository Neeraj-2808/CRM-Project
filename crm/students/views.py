from django.shortcuts import render,redirect,get_object_or_404

from django.http import HttpResponse

from django.views.generic import View

from .models import DistrictChoices,CourseChoices,BatchChoices,TrainerChoices

from .utility import get_admission_number,get_password

from authentication.permissions import permission_roles

from django.db import transaction

from .models import Students

from .forms import StudentRegisterForm

from django.db.models import Q

from authentication.models import Profile

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

class GetStudentObject():

    def get_student(self,request,uuid):

        try:
           student = Students.objects.get(uuid=uuid)

           return student

           

        except:
           
           return render(request,'errorpages/error-404.html')
       


# Create your views here.
@method_decorator(permission_roles(roles = ['Admin','Sales','Student']),name='dispatch')
class DashBoardView(View) :

    def get(self,request,*args,**kwargs):

        return render(request,'students/dashboard.html')
    
@method_decorator(permission_roles(roles = ['Admin','Sales','Trainer','Academic Counselor','Student']),name='dispatch')   
class StudentsListView(View) :

    def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        students = Students.objects.filter(active_status = True)

        if query :

            students= Students.objects.filter(Q(active_status=True)&(Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(post_office__icontains=query)|Q(contact__icontains=query)|Q(pin_code__icontains=query)|Q(house_name__icontains=query)|Q(email__icontains=query)|Q(course__name__icontains=query)|Q(batch__name__icontains=query)|Q(district__icontains=query)))


        data = {'students':students,'query':query}

        return render(request,'students/students.html',context=data)
    

@method_decorator(permission_roles(roles = ['Admin','Sales']),name='dispatch')   
class StudentRegistrationView(View):
    def get(self,request,*args,**kwargs):

        form  = StudentRegisterForm()

        data = {'form':form}

        # data = {'districts':DistrictChoices,'courses':CourseChoices,'batches':BatchChoices,'trainers':TrainerChoices,'form':form}

        # data ={"numbers ": [1,2,3,4,5]}

        return render(request,'students/registration.html',context=data)
    
    def post(self,request,*args,**kwargs):

        form  = StudentRegisterForm(request.POST,request.FILES)

        if form.is_valid():

            with transaction.atomic():
            
                student= form.save(commit=False)

                student.adm_number = get_admission_number()

                # student.join_date = '2025-02-05'

                username = student.email

                password = get_password()

                print(password)

                profile=Profile.objects.create_user(username=username,password=password,role= 'Student')

                student.profile = profile

                student.save()

            return redirect('students-lists')
        
        else: 
            data = {'form':form}
            return render (request,'students/registration.html',context=data)
        

        # form_data = request.POST
    
        # first_name = form_data.get("first_name")
        # last_name = form_data.get("last_name")
        # photo = request.FILES.get("photo")
        # email = form_data.get("email")
        # contact_number = form_data.get("contact_number")
        # house_name = form_data.get("house_name")
        # post_office = form_data.get("post_office")
        # pincode = form_data.get("pincode")
        # course = form_data.get("course")
        # districts = form_data.get("districts")
        # batch = form_data.get("batch")
        # batch_date = form_data.get("batch_date")
        # trainer = form_data.get("trainer")

        # adm_number = get_admission_number()

        # join_date ='2024-08-16'

        # print(adm_number)

        # print(first_name)
        # print(last_name)
        # print(email)
        # print(contact_number)
        # print(house_name)
        # print(post_office)
        # print(pincode)
        # print(course)
        # print(districts)
        # print(batch)
        # print(batch_date)
        # print(trainer)

        # Students.objects.create(first_name=first_name,
        #                        last_name=last_name,
        #                        photo=photo,
        #                        email=email,
        #                        contact = contact_number,
        #                        house_name = house_name,
        #                        post_office=post_office,
        #                        district = districts,
        #                        pin_code = pincode,
        #                        adm_number=adm_number,
        #                        course=course,
        #                        batch=batch,
        #                        batch_date=batch_date,
        #                        trainer_name = trainer,
        #                        join_date=join_date


        #                     )

        
    
class CourseView(View) :

    def get(self,request,*args,**kwargs):

        return render(request,'students/course.html')
    
class BatchView(View) :

    def get(self,request,*args,**kwargs):

        return render(request,'students/course.html')
    
@method_decorator(permission_roles(roles = ['Admin','Sales','Trainer','Academic Counselor']),name='dispatch')   

class StundentDetailsView(View):

   def get(self,request,*args,**kwargs):
       
       uuid = kwargs.get('uuid')
       
       
       student=GetStudentObject().get_student(request,uuid)


       
       data = {'student':student}
       
       return render(request,'students/student-detail.html',context=data)
   
@method_decorator(permission_roles(roles = ['Admin']),name='dispatch')   

class StundentDeleteView(View):

   def get(self,request,*args,**kwargs):
       
       uuid = kwargs.get('uuid')

       student=GetStudentObject().get_student(request,uuid)

       student.active_status = False

       student.save()    
    #    student.delete()
       return redirect('students-lists')
   

@method_decorator(permission_roles(roles = ['Admin','Sales']),name='dispatch')   
   
class StudentUpdateView(View):

    def get(self,request,*args,**kwargs):
        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)

        form = StudentRegisterForm(instance=student)

        data = {'form':form}

        return render(request,'students/student-update.html',context=data)   
    

    def post(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)

        form  = StudentRegisterForm(request.POST,request.FILES,instance=student)   

        if form.is_valid():
            
            form.save()

            return redirect('students-lists')
        
        else: 
            data = {'form':form}

            return render (request,'students/student-update.html',context=data) 