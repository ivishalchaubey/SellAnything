from django.shortcuts import render,redirect,get_object_or_404
from .models import rooms
from django.core.files.storage import FileSystemStorage


def index(request):
	room = rooms.objects

	return render (request,'index.html',{'rooms':room})


def detail(request,customer_id):
	customer_detail = get_object_or_404(rooms,pk=customer_id)
	return render(request,'detail.html',{'full_info':customer_detail})

def submit(request):
	if request.method == 'POST' and request.FILES['image']:
		my_name = request.POST.get('name')
		my_email = request.POST.get('email')
		my_price = request.POST.get('price')
		my_description = request.POST.get('discription')
		my_mobile = request.POST.get('mobile')
		my_image = request.FILES['image']
		fs = FileSystemStorage()
		fs_name = fs.save(my_image.name,my_image)
		url = fs.url(fs_name)

		final_submit = rooms(name=my_name,email=my_email,price=my_price,discription=my_description,mobile=my_mobile,image=url)
		final_submit.save()
		return redirect ('/')
	
	else:
		return redirect('/')
