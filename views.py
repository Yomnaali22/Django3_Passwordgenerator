from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def Home(request):
	return render(request, 'generator/Home.html')



def password(request):
	characters = list('abcdefjhijklmnopqrsxyz12345678910')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCKJDHSKJHKJHWKRLJHWKJHDOIPI'))

		if request.GET.get('special'):
			characters.extend(list('#!)*$@)*!)#!(#*!$)!($*)@'))


	length = int(request.GET.get('length', 123))

	ppassword = ''

	for x in range(length):
		ppassword += random.choice(characters)

		return render(request, 'generator/password.html', {'password':ppassword})


def About(request):
	return render(request, 'generator/aboutus.html')