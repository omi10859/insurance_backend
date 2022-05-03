import csv
import io
from datetime import datetime

from policy import models

from policy.models import UserPolicy

# todo: background task, automic transaction 
def proccess_file(file):
    file = file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(file))
    
    for i in reader:
        # YYY-MM-DD 
        date_obj = datetime.strptime(i['Date of Purchase'], '%m/%d/%Y')
        UserPolicy.objects.create(
            policy_id = i['Policy_id'],
            date_of_purchase = date_obj.strftime('%Y-%m-%d'),
            customer_id = i['Customer_id'],
            fuel = i['Fuel'],
            vehicle_segment = i['VEHICLE_SEGMENT'],
            premium = i['Premium'],
            bodily_injury_liability = i['bodily injury liability'],
            personal_injury_protection = i[' personal injury protection'],
            property_damage_liability = i[' property damage liability'],
            collision = i[' collision'],
            comprehensive = i[' comprehensive'],
            customer_gender = i['Customer_Gender'],
            customer_income_group = i['Customer_Income group'],
            customer_region = i['Customer_Region'],
            customer_marital_status = i['Customer_Marital_status'],
        )
