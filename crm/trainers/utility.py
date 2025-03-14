import uuid

import string


import random

from .models import Trainers

def get_employee_number():

    while True :

        pattern = str(uuid.uuid4().int)[:2]

        employee_num = f'LM-E{pattern}'

        if not Trainers.objects.filter(employee_id=employee_num).exists():

            return employee_num
        

def get_password():

    password = ''.join(random.choices(string.ascii_letters + string.digits,k=8))

    print(password)

    return password

