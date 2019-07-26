from django.shortcuts import render
import random

# Create your views her
def  guesss_number(request):
	random_number = random.randint(1,999)
	context = {'random_number' :random_number}

	if request.method == 'POST':
		random_number = request.POST.get('random_number')
		guess_number = request.POST.get('guess_number')

		if random_number == guess_number :
			message = "You are correct"
		elif guess_number>random_number:
			message = "You are too high" 
		elif guess_number<random_number:
			message = "You are too low"
		else:
			message = "wrong input" 
					
		
		return render(request,'numbergame/result.html',{'message' :message})

		
	return render(request, 'numbergame/index.html',context) 
