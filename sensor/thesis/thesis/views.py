from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from service.models import Service
from service.models import Reminder

from django.utils import timezone
# from service.models import Reminder


def ABOUTUS(request):
     return HttpResponse("WELCOME TO ABOUTUS PAGE")

def ALERT(request):
     return render(request,"alert.html")

def BOX(request):
     return render(request,"box.html")

def INDEX(request):
     return render(request,"index.html")

def INSULIN(request):
     return render(request,"insulin.html")

def SCHEDULE(request):
     return render(request,"schedule.html")

def SEEBOXNAME(request):
     return render(request,"seeboxname.html")

def SEESCHEDULE(request):
     return render(request,"seeschedule.html")

def TEST(request):
     return render(request,"test.html")

def TIMER(request):
     return render(request,"timer.html")

def SCHEDULE_UPDATED(request):
     return render(request,"schedule update.html")


def saveEnquery(request):
      if request.method== "POST":
          #  name=request.POST.get('name')
           box_no=request.POST.get('box_no')
           name=request.POST.get('medicine_name')
           quantity=request.POST.get('quantity')

           en=Service(box_number=box_no,medicine_name=name,quantity=quantity)
           en.save()
      return render(request,"test.html") 


def saveReminder(request):
      if request.method== "POST":
           name=request.POST.get('medicine_name')
           time=request.POST.get('time1')

           en1=Reminder(medicine_name=name,time_to_take_medicine=time)
           en1.save()
      return render(request,"schedule update.html")



def check_reminders(request):
    current_time = timezone.now().strftime("%H:%M") # Get current time in format like "10am"
#     print(f"Current Time: {current_time}")

    reminders_to_show = Reminder.objects.filter(time_to_take_medicine=current_time)
#     reminders_to_show = Reminder.objects
      

#     print(f"Reminders to Show: {reminders_to_show}")
    
    return render(request, 'show_reminders.html', {'reminders_to_show': reminders_to_show})






def show_medicine_name1(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=1)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box1.html', context)






def show_medicine_name2(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=2)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box2.html', context)


def show_medicine_name3(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=3)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box3.html', context)


def show_medicine_name4(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=4)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box4.html', context)


def show_medicine_name5(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=5)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box5.html', context)


def show_medicine_name6(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=6)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box6.html', context)


def show_medicine_name7(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=7)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box7.html', context)


def show_medicine_name8(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=8)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box8.html', context)


def show_medicine_name9(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=9)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box9.html', context)


def show_medicine_name10(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=10)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box10.html', context)


def show_medicine_name11(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=11)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box11.html', context)


def show_medicine_name12(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=12)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box12.html', context)



def show_medicine_name13(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=13)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box13.html', context)



def show_medicine_name14(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=14)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box14.html', context)



def show_medicine_name15(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=15)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box15.html', context)


def show_medicine_name16(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=16)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box16.html', context)


def show_medicine_name17(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=17)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box17.html', context)


def show_medicine_name18(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=18)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box18.html', context)



def show_medicine_name19(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=19)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box19.html', context)



def show_medicine_name20(request):
    # Retrieve the Service object for box_number=1
    service = get_object_or_404(Service, box_number=20)

    # Pass the medicine_name to the template
    context = {'medicine_name': service.medicine_name}
    
    # Render the template with the context
    return render(request, 'Box20.html', context)


