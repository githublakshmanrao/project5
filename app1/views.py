from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def emp_data_view(request):
    emp_data={
        'eno':200 ,
        'ename': 'vikas',
        'esal':60000  ,
        'e address':'benglur',
    }
    resp =<a>'<h1>employeeno:{}<br> employee name:{}<br> employee sal:{}<br> employee address:{} ' \
          '</h1>'\
        .format( emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['e address'])
    return HttpResponse(resp)