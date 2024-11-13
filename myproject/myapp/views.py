# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .utils import my_function
from django.shortcuts import render
from .forms import ExecuteForm
from .utils import my_function

def home(request):
    header_text = ""
    
    if request.method == 'POST':
        # When the button is clicked, call the function
        header_text = my_function()
    
    form = ExecuteForm()
    return render(request, 'myapp/home.html', {'form': form, 'header_text': header_text})
    
def execute_python_code(request):
    # Call the function
    result = my_function()
    return JsonResponse({
        'message': result
        })