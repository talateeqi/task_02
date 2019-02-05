from django.shortcuts import render


# Create your views here.
def genzapp(request):
	context = {
			'msg' : 'Hello World'
	}
	return render(request, "Task02.html", context)