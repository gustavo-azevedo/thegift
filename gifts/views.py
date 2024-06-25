from django.shortcuts import render, get_object_or_404
from accounts.models import UserInfo
from gifts.models import Gift
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def friends_activity(request):
    user_info = UserInfo.objects.get(user_id=request.user)
    friends_list = user_info.friends.all()
    peoples_list = []
    for people in friends_list:
        name = people.name
        id = people.user_id
        #last_gift = people.likes.order_by('-id').first()
        last_gift = people.likes.first()
        if last_gift:
            activity_dict = {
                "name": name,
                "person_id": id,
                "last_gift":last_gift
            }
            
            peoples_list.append(activity_dict)
    
    return peoples_list

def my_friends(request):
    activity = friends_activity(request)
    context = {}
    user_info = UserInfo.objects.get(user_id=request.user)
    if request.GET.get("query", False):
        search_term = request.GET["query"].lower()
        people_list = user_info.friends.filter(name__icontains=search_term)
        context = {"people_list": people_list, 
                   "len_list": len(people_list),
        "friends_activity": activity}
    else:
        people_list = user_info.friends.all()
        context = {"people_list": people_list, 
                   "len_list": len(people_list),
        "friends_activity": activity}
        
    return render(request, "gifts/people.html", context)

def my_gifts(request):
    activity = friends_activity(request)
    user_info = UserInfo.objects.get(user_id=request.user)

    my_gifts = user_info.likes.all()

    context = {
        "gifts_list": my_gifts,
        "friends_activity": activity
    }
    return render(request, "gifts/my_list.html", context)


def detail_people(request, people_id):
    activity = friends_activity(request)
    user_info = UserInfo.objects.get(user_id=request.user)
    
    friend_info = UserInfo.objects.get(user_id=people_id)
    
    
    user_friends = user_info.friends.all()
    user_gifts = friend_info.likes.all()
    gifts_list = Gift.objects.filter(pk__in=user_gifts.values_list('pk', flat=True))
    
    if friend_info in user_friends:
        friends = True
    else:
        friends = False
        
    context = {
        "is_friend": friends,
        "people": friend_info,
        "friends_activity": activity,
        "gifts_list": gifts_list
    }
    return render(request, "gifts/profile.html", context)

def friend_request(request, people_id):
    
    user_info = UserInfo.objects.get(user_id=request.user)
    
    friend_info = UserInfo.objects.get(user_id=people_id)
    
    
    user_friends = user_info.friends.all()
    
    if friend_info in user_friends:
        user_info.friends.remove(friend_info)
    else:
        user_info.friends.add(friend_info)
        
    user_info.save()
    return HttpResponseRedirect(
                reverse('detail_people', args=(people_id, )))


def search_users(request):
    context = {}
    activity = friends_activity(request)
    if request.GET.get("query", False):
        search_term = request.GET["query"].lower()
        people_list = UserInfo.objects.filter(name__icontains=search_term)
        context = {"people_list": people_list, 
                   "len_list": len(people_list),
                   "friends_activity": activity}
    else:
        people_list = UserInfo.objects.all()
        context = {"people_list": people_list, 
                   "len_list": len(people_list),
                   "friends_activity": activity}
        
    return render(request, "gifts/people.html", context)


def tinder_base(request):
    activity = friends_activity(request)
    if request.method == "POST":

        points = json.loads(request.POST.get("points_counter"))
        
        print(type(points))
        user_info = UserInfo.objects.get(user_id=request.user)
        print(user_info)
        
        user_info.roupas=user_info.roupas + int(points.get("roupas"))
        user_info.fitness=user_info.fitness + int(points.get("fitness"))
        user_info.beleza=user_info.beleza + int(points.get("beleza"))
        user_info.eletronicos=user_info.eletronicos + int(points.get("eletronicos"))
        user_info.outros=user_info.outros + int(points.get("outros"))

        for gift in points.get('liked_gifts'):
            gift_obj = Gift.objects.get(pk = int(gift))
            user_info.likes.add(gift_obj)
        user_info.save()
        return HttpResponse("Form submitted successfully")
    else:

        id_user = request.user
        user_info = UserInfo.objects.get(user_id=request.user)

        my_gifts = user_info.likes.all()
        gifts_list = Gift.objects.exclude(pk__in=my_gifts.values_list('pk', flat=True))
        points_dict = {
            "roupas": 0,
            "fitness": 0,
            "beleza": 0,
            "eletronicos": 0,
            "outros": 0,
            "liked_gifts": []
        }
        context = {
            "gifts_list": gifts_list,
            "len_gifts_list": len(gifts_list),
            "points_dict": json.dumps(points_dict),
            "friends_activity": activity
        }

        return render(request, "gifts/tinderbase.html", context)
