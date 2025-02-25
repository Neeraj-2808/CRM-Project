from django import forms 


from .models import Students,DistrictChoices,CourseChoices,BatchChoices,TrainerChoices

from courses.models import Courses
from batches.models import Batches
from trainers.models import Trainers





class StudentRegisterForm(forms.ModelForm):


    class Meta:

        model = Students

        # fields = ['first_name','last_name','photo','email','contact','house_name','post_office','district','pin_code','course
        #         'batch','batch_date','trainer_name']
        
        #if all field matches in the models used

        # fields = '__all__'

        exclude = ['adm_number','join_date','uuid','active_status','profile']

        widgets = {'first_name' :forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                        'placeholder':'Enter first name',
                                                        'required':'required'}),
                'last_name' :forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                        'placeholder':'Enter second name',
                                                        'required':'required'}),
                'photo' :forms.FileInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                        }),
                'email' :forms.EmailInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                        'placeholder':'Enter mail',
                                                        'required':'required'}),
                'contact' :forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                        'required':'required'}),
                'house_name' :forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                        'required':'required'}),
                'post_office' :forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                        'required':'required'}),
                'pin_code' :forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                        'required':'required'}),
                # 'batch_date' :forms.DateInput(attrs={   'type':'date',
                #                                         'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                #                                         'required':'required'}),
                                                        }
        

    district = forms.ChoiceField(choices=DistrictChoices.choices,widget=forms.Select(attrs={'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                            'required':'required'}))
    # batch = forms.ChoiceField(choices=BatchChoices.choices,widget=forms.Select(attrs={'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                         'required':'required'}))

    batch = forms.ModelChoiceField(queryset=Batches.objects.all(),widget=forms.Select(attrs={'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                           'required':'required'}))
    # course = forms.ChoiceField(choices=CourseChoices.choices,widget=forms.Select(attrs={'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                         'required':'required'}))

    course = forms.ModelChoiceField(queryset=Courses.objects.all(),widget=forms.Select(attrs={'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                           'required':'required'}))


    # trainer_name = forms.ChoiceField(choices=TrainerChoices.choices,widget=forms.Select(attrs={'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    
    # 'required':'required'}))
    trainer = forms.ModelChoiceField(queryset=Trainers.objects.all(),widget=forms.Select(attrs={'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                           'required':'required'}))                                                                                      
    

    def clean(self):

        cleaned_data  =super().clean()

        pin_code = cleaned_data.get('pin_code')  
        
        email = cleaned_data.get('email')

        if len(pin_code)<6:
            
            self.add_error('pin_code','pincode must be six digit')


        # if Students.objects.filter(profile__username=email).exists():

        #     self.add_error('email','This email is already been taken,please use another mail')

        return cleaned_data
    
    
    def __init__(self,*args,**kwargs):

        super(StudentRegisterForm,self).__init__(*args,**kwargs)

        if not self.instance:

            self.fields.get("photo").widget.attrs['required'] = "required"

