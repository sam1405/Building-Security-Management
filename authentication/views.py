from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import SignupUser, AddGuests
from django.utils import timezone
#import face_recognition

# Create your views here.
def signup_view(request):
    name=''
    password=''
    email=''
    buildingname=''
    roles=''
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        buildingname = request.POST.get('buildingname')
        roles = request.POST.get('roles')
        password = request.POST.get('password')

        if SignupUser.objects.filter(name=name).exists():
            messages.error(request, "name already exists")
            return render(request, 'authentication/Signup.html')
    
        hashed_password = make_password(password)

        new_user = SignupUser(name=name, email=email, buildingname=buildingname, role=roles, password=hashed_password)
        new_user.save()
        messages.success(request, "Account Created Successfully! Please Login!")
        return redirect('login')
    return render(request, 'authentication/Signup.html')

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        print(f"DEBUG: Entered Name: {name}")
        print(f"DEBUG: Entered Password: {password}")
        
        try:
            user = SignupUser.objects.get(name=name)

            if check_password(password, user.password):
                request.session['id'] = user.id
                request.session['role'] = user.role

                if user.role.strip().lower() == 'watchman':
                    return redirect('homepagew')
                else:
                    return redirect('homepagepm')
            else:
                messages.error(request, "Incorrect Password!")
                return redirect('login')


        except SignupUser.DoesNotExist:
            messages.error(request, "Username Does Not Exists!")
            return redirect('login')

    return render(request, 'authentication/Login.html')

def homepagew_view(request):
    if 'id' not in request.session:
        messages.error(request, "Please Login First.")
        return redirect('login')
    
    return render(request, 'authentication/HomePageW.html')

def homepagepm_view(request):
    if 'id' not in request.session:
        messages.error(request, "Please Login First.")
        return redirect('login')
    
    return render(request, 'authentication/HomePagePM.html')

def addguests_view(request):
    role = request.session.get('role')
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        destination = request.POST.get('destination')
        vehical = request.POST.get('vehical')
        purpose = request.POST.get('purpose')

        if role.strip().lower() == 'member':
            uploaded_image = request.FILES.get('image')

            new_guest = AddGuests(name=name, contact=contact, address=address, destination=destination, vehical=vehical, purpose=purpose, image = uploaded_image)
            new_guest.save()
            messages.success(request, "Guest Registered Successfully!")
            return redirect('guestslist')
        else:
            new_guest = AddGuests(name=name, contact=contact, address=address, destination=destination, vehical=vehical, purpose=purpose)
            new_guest.save()
            messages.success(request, "Guest Registered Successfully!")
            return redirect('guestslist')
        
    if role.strip().lower() == 'member':
        return render(request, 'authentication/AddGuestsPM.html')
    else:
        return render(request, 'authentication/AddGuests.html')

def guestslist_view(request):
    show_all = request.GET.get('view') == 'all'

    if show_all:
        all_guests = AddGuests.objects.all().order_by('-intime')
    else:
        today = timezone.now().date()
        all_guests = AddGuests.objects.filter(intime__date=today).order_by('-intime')

    return render(request, 'authentication/Guests.html', {'guests': all_guests})

def checkout_view(request, guest_id):
    if request.method =='POST':
        guest = get_object_or_404(AddGuests, id=guest_id)

        guest.outtime = timezone.now()
        guest.save()

    return redirect('guestslist')

def checkin_view(request, guest_id):
    if request.method =='POST':
        guest = get_object_or_404(AddGuests, id=guest_id)

        guest.intime = timezone.now()
        guest.save()

    return redirect('guestslist')

def about_view(request):
    return render(request, 'authentication/About.html')