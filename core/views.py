from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render


# Create your views here.
def homepage(request):
    context = {
        'Name': '01_Usman',
        'Position': 'DPDK',
        'Office': 'Pakistan',
        'Age': '32',
        'Start_date': '2024-04-18',
        'Salary': '$200,000',
    }
    return render(request, 'core/homepage.html', context=context)


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'


def ajax_view(request):
    if is_ajax(request) and request.method == 'POST':
        # Handle AJAX POST request here
        data = {'message': 'This is a sample AJAX response!'}
        return JsonResponse(data)
    else:
        # Handle non-AJAX requests or other HTTP methods
        return HttpResponseNotAllowed(['POST'])
