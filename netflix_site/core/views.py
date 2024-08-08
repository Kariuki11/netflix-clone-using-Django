from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

# def add_to_list(request):
#     if request.method == 'POST':
#         # Your logic to add the item to the list
#         return JsonResponse({'message': 'Item added to list successfully'})
#     return JsonResponse({'message': 'Invalid request'}, status=400)
