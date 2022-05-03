import random
from datetime import datetime
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Count

from .models import UserPolicy

# todo: background task
def get_chart_data():
    queryset = UserPolicy.objects.all()

    regions = queryset.values_list('customer_region', flat=True).distinct()
    
    colours = ['rgba(56, 193, 86, 0.8)', 
            'rgba(193, 56, 146, 0.8)', 
            'rgba(193, 106, 56, 0.8)', 
            'rgba(75, 56, 193, 0.9)',
            'rgba(192, 56, 193, 0.9)',
            'rgba(115, 29, 182, 0.5)',
            'rgba(193, 189, 56, 0.9)',
            ]

    dataset = []
    for region in regions:
        monthwise_count = queryset.filter(customer_region=region, date_of_purchase__gte='2018-01-01', date_of_purchase__lt='2019-01-01').annotate(
            month=ExtractMonth('date_of_purchase')
        ).values('month').order_by('month').annotate(count=Count('id'))
        list_data = [0]*12

        for i in list(monthwise_count):
            list_data[i['month']-1] = i['count']
        
        data = {
                'label': region,
                'data': list_data,
                'borderColor': random.choice(colours),
                'backgroundColor': random.choice(colours),    
        }
        dataset.append(data)
    
    data = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'datasets': dataset
        }

    return data