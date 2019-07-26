from django.shortcuts import render
import random



def  guesss_number(request):

	''' genrate a random and check with a user 
	entered number and return a message'''
	
	random_number = random.randint(1,999)
	if request.method == 'POST':
		random_number = int(request.POST.get('random_number'))
		guess_number = int(request.POST.get('guess_number'))

		if random_number == guess_number :
			message = "You are correct"
		elif guess_number>random_number:
			message = "You are too high" 
		elif guess_number<random_number:
			message = "You are too low"
		else:
			message = "wrong input" 
	
		context = {'message' :message}
		return render(request,'numbergame/result.html',context)

	context = {'random_number' :random_number}	
	return render(request, 'numbergame/index.html',context) 
