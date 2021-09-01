from django.shortcuts import render,redirect
from Place.models import Basic_travel, Destination_image, Destination_tour, type_hotel, mode_of_travel, explore_route, location_destination, Acti
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/accounts/login")
def goa(request):
    if(request.method =="POST" and "travel" not in request.POST):
        name=request.POST["name"]
        num = request.POST["number"]
        days = request.POST["days"]
        date = request.POST["date"]
        origin = request.POST["origin"]
        traveller = request.POST["traveller"]
        proof=request.POST["proof"]
        abudget = request.POST["budget"]
        a=Basic_travel.objects.create(name=name,phone_number=num,days=days,departure=date,origin=origin,Numberoftravellers=traveller,proof=proof,abudget=abudget)
        a.save()
        di = Destination_image.objects.filter(place__name="Goa")
        dt = Destination_tour.objects.filter(place__name="Goa")
        th = type_hotel.objects.filter(place__name="Goa")
        mot = mode_of_travel.objects.filter(place__name="Goa")
        er = explore_route.objects.filter(place__name="Goa")
        ld = location_destination.objects.filter(place__name="Goa")
        A = Acti.objects.filter(place__name="Goa")
        bkjn = True
        context = {"Destination_image": di, "Destination_tour": dt, "type_hotel": th, "mode_of_travel": mot,
                   "explore_route": er, "location_destination": ld, "Activities": A, "a": False}
        return(render(request, 'plan.html', context))
    elif(request.method == "POST" and "travel"  in request.POST):
        travel = request.POST["travel"]
        cab_explo = request.POST["cab explo"]
        dest_tour = request.POST["dest tour"]
        hotel = request.POST["hotel"]
        location_dest = request.POST["locationdestination"]
        activities = request.POST.getlist("activities")
        strs=""
        for i in activities:
            strs=strs+i+","
        b=Basic_travel.objects.last()
        b.mode_of_travel=travel
        b.explore_route=cab_explo
        b.Destination_tour=dest_tour
        b.type_hotel=hotel
        b.location_destination=location_dest
        b.Activities=strs
        b.save()

        return HttpResponseRedirect(request.path_info)


    else:
            di=Destination_image.objects.filter(place__name="Goa")
            dt = Destination_tour.objects.filter(place__name="Goa")
            th = type_hotel.objects.filter(place__name="Goa")
            mot = mode_of_travel.objects.filter(place__name="Goa")
            er = explore_route.objects.filter(place__name="Goa")
            ld = location_destination.objects.filter(place__name="Goa")
            A = Acti.objects.filter(place__name="Goa")
            bkjn=True
            context = {"Destination_image": di, "Destination_tour":dt,"type_hotel":th,"mode_of_travel":mot,"explore_route":er,"location_destination":ld,"Activities":A,"a":bkjn}
            return(render(request,'plan.html',context))


@login_required(login_url="/accounts/login")
def manali(request):
    if(request.method == "POST" and "travel" not in request.POST):
        name = request.POST["name"]
        num = request.POST["number"]
        days = request.POST["days"]
        date = request.POST["date"]
        origin = request.POST["origin"]
        traveller = request.POST["traveller"]
        proof = request.POST["proof"]
        abudget = request.POST["budget"]
        a = Basic_travel.objects.create(name=name, phone_number=num, days=days, departure=date,
                                        origin=origin, Numberoftravellers=traveller, proof=proof, abudget=abudget)
        a.save()
        di = Destination_image.objects.filter(place__name="Manali")
        dt = Destination_tour.objects.filter(place__name="Manali")
        th = type_hotel.objects.filter(place__name="Manali")
        mot = mode_of_travel.objects.filter(place__name="Manali")
        er = explore_route.objects.filter(place__name="Manali")
        ld = location_destination.objects.filter(place__name="Manali")
        A = Acti.objects.filter(place__name="Manali")
        bkjn = True
        context = {"Destination_image": di, "Destination_tour": dt, "type_hotel": th, "mode_of_travel": mot,
                   "explore_route": er, "location_destination": ld, "Activities": A, "a": False}
        return(render(request, 'plan.html', context))
    elif(request.method == "POST" and "travel"  in request.POST):
        travel = request.POST["travel"]
        cab_explo = request.POST["cab explo"]
        dest_tour = request.POST["dest tour"]
        hotel = request.POST["hotel"]
        location_dest = request.POST["locationdestination"]
        activities = request.POST.getlist("activities")
        strs=""
        for i in activities:
            strs=strs+i+","
        b=Basic_travel.objects.last()
        b.mode_of_travel=travel
        b.explore_route=cab_explo
        b.Destination_tour=dest_tour
        b.type_hotel=hotel
        b.location_destination=location_dest
        b.Activities=strs
        b.save()

        return redirect('/')

    else:
            di=Destination_image.objects.filter(place__name="Manali")
            dt = Destination_tour.objects.filter(place__name="Manali")
            th = type_hotel.objects.filter(place__name="Manali")
            mot = mode_of_travel.objects.filter(place__name="Manali")
            er = explore_route.objects.filter(place__name="Manali")
            ld = location_destination.objects.filter(place__name="Manali")
            A = Acti.objects.filter(place__name="Manali")
            bkjn=True
            context = {"Destination_image": di, "Destination_tour":dt,"type_hotel":th,"mode_of_travel":mot,"explore_route":er,"location_destination":ld,"Activities":A,"a":bkjn}
            return(render(request,'planm.html',context))




