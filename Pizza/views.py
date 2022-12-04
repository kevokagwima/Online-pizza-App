from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Dinner_platter, User_Profile, Order, Order_items

def signup(request):
  if request.method =="POST":
    password = request.POST["password"]
    password1 = request.POST["password1"]
    if password1 != password:
      messages.error(request, "Passwords do not match")
      return redirect('signup')
    elif User.objects.filter(username=request.POST["username"]).exists():
      messages.error(request, "Username already exists")
      return redirect('signup')
    elif User.objects.filter(email=request.POST["email"]).exists():
      messages.error(request, "Email address already exists")
      return redirect('signup')
    else:
      new_user = User.objects.create(
        username=request.POST["username"],
        email=request.POST["email"],
        password=request.POST["password"]
      )
      new_user.save()
      user_model = User.objects.get(username=request.POST["username"])
      new_profile = User_Profile.objects.create(user=user_model, id_user=user_model.id)
      new_profile.save()
      messages.success(request, "Registration successfull")
      return redirect('signin')
  else:
    return render(request, 'signup.html')

def signin(request):
  if request.method == "POST":
    username = request.POST["username"]
    user = User.objects.filter(username=username).first()
    if user is None:
      messages.error(request, "No user with that username")
      return redirect('signin')
    else:
      password = request.POST["password"]
      if user.password != password:
        messages.error(request, "Invalid Credentials")
        return redirect('signin')
      else:
        login(request, user)
        messages.success(request, "Login successfull")
        return redirect('index')
  else:
    return render(request, 'signin.html')

@login_required(login_url='/signin')
def index(request):
  user_profile = User_Profile.objects.get(user=request.user)
  dinner_platters = Dinner_platter.objects.all()
  existing_order = Order.objects.filter(user=request.user, status="Active").first()
  order_items = Order_items.objects.filter(user=request.user).all()
  context = {
    'user_profile': user_profile,
    'dinner_platters': dinner_platters,
    'order': existing_order,
    'order_items': order_items
  }

  return render(request, 'index.html', context)

def profile(request, pk):
  user = User.objects.get(username=pk)
  user_profile = User_Profile.objects.filter(user=user).first()
  context = {
    'user': user,
    'user_profile': user_profile
  }
  if request.method == "POST":
    if request.FILES.get("profile") == None:
      user.first_name = request.POST["fname"]
      user.last_name = request.POST["lname"]
      user_profile.phone_number = request.POST["phone"]
      user.save()
      user_profile.save()
      messages.success(request, "Profile updated successfully")
      return redirect('index')
    if request.FILES.get("profile") != None:
      user_profile.profileimg = request.FILES.get("profile")
      user.first_name = request.POST["fname"]
      user.last_name = request.POST["lname"]
      user_profile.phone_number = request.POST["phone"]
      user.save()
      user_profile.save()
      messages.success(request, "Profile updated successfully")
      return redirect('index')

  return render(request, 'profile.html', context)

def delivery(request, pk):
  user = User.objects.get(username=pk)
  user_profile = User_Profile.objects.filter(user=user).first()
  context = {
    'user': user,
    'user_profile': user_profile
  }
  if request.method == "POST":
    user_profile.county = request.POST["county"]
    user_profile.city = request.POST["city"]
    user_profile.town = request.POST["town"]
    user_profile.street = request.POST["street"]
    user_profile.House_no = request.POST["houseno"]
    user_profile.save()
    messages.success(request, "Profile updated successfully")
    return redirect('index')

  return render(request, 'profile.html', context)

@login_required(login_url='/signin')
def product_description(request, pk):
  dinner_platter = Dinner_platter.objects.filter(name=pk).first()
  other_dinner_platter = Dinner_platter.objects.all()
  existing_order = Order.objects.filter(user=request.user, status="Active").first()
  user_profile = User_Profile.objects.get(user=request.user)
  order_items = Order_items.objects.filter(user=request.user).all()
  context = {
    'dinner_platter': dinner_platter,
    'user_profile': user_profile,
    'other_dinner_platter': other_dinner_platter,
    'order': existing_order,
    'order_items': order_items
  }

  return render(request, "description.html", context)

@login_required(login_url='/signin')
def new_order(request, pk):
  dinner_platter = Dinner_platter.objects.filter(id=pk).first()
  existing_order = Order.objects.filter(user=request.user, status="Active").first()
  all_order_items = Order_items.objects.filter(order=existing_order).all()
  if dinner_platter is None:
    messages.error(request, "Item not found")
    return redirect('index')
  if existing_order is None:
    new_order = Order.objects.create(user=request.user)
    new_order.save()
    if request.method == "POST":
      new_order_item = Order_items(user=request.user, order=new_order, item=dinner_platter, quantity=request.POST["quantity"], amount=request.POST["size"])
      new_order_item.save()
      messages.success(request, "A new order has been initiated")
      return redirect('order-details', pk=new_order_item.order.id)
  else:
    if all_order_items is not None:
      all_items = []
      for order_items in all_order_items:
        all_items.append(order_items.item)
      if dinner_platter.name in all_items:
        if request.method == "POST":
          order_item = Order_items.objects.filter(item=dinner_platter.name).first()
          order_item.quantity = request.POST["quantity"]
          order_item.amount = request.POST["size"]
          order_item.save()
          messages.info(request, "Your cart has been updated")
          return redirect('order-details', pk=existing_order.id)
      else:
        if request.method == "POST":
          new_order_item = Order_items(user=request.user, order=existing_order, item=dinner_platter.name,quantity=request.POST["quantity"], amount=request.POST["size"])
          new_order_item.save()
          messages.info(request, "Your cart has been updated")
          return redirect('order-details', pk=existing_order.id)
    else:
      if request.method == "POST":
        new_order_item = Order_items(user=request.user, order=existing_order, item=dinner_platter.name,quantity=request.POST["quantity"], amount=request.POST["size"])
        new_order_item.save()
        messages.info(request, "Your cart has been updated")

    return redirect('order-details', pk=existing_order.id)

@login_required(login_url='/signin')
def order_details(request, pk):
  existing_order = Order.objects.filter(id=pk).first()
  order_items = Order_items.objects.filter(order=existing_order).all()
  total = []
  dinners = []
  for order in order_items:
    dinner_platter = Dinner_platter.objects.filter(name=order.item).first()
    dinners.append(dinner_platter)
    total.append(order.amount*order.quantity)
  user_profile = User_Profile.objects.get(user=request.user)
  context = {
    'order': existing_order,
    'user_profile': user_profile,
    'dinners': dinners,
    'order_items': order_items,
    'total': sum(total)
  }

  return render(request, "order.html", context)

@login_required(login_url='/signin')
def increase_quantity(request, pk):
  order_item = Order_items.objects.get(id=pk)
  if order_item:
    order_item.quantity = order_item.quantity + 1
    order_item.save()
    messages.success(request, "Order item updated successfully")
  else:
    messages.error(request, "Order not found")

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/signin')
def decrease_quantity(request, pk):
  order_item = Order_items.objects.get(id=pk)
  if order_item:
    order_item.quantity = order_item.quantity - 1
    order_item.save()
    messages.success(request, "Order item updated successfully")
  else:
    messages.error(request, "Order not found")

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/signin')
def remove_item(request, pk):
  order_item = Order_items.objects.get(id=pk)
  if order_item is None:
    messages.error(request, "Could not remove the item")
  else:
    order_item.delete()
    messages.success(request, "Item removed successfully")
  
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/signin')
def order_summary(request, pk):
  existing_order = Order.objects.filter(id=pk).first()
  order_items = Order_items.objects.filter(order=existing_order).all()
  total = []
  dinners = []
  for order in order_items:
    dinner_platter = Dinner_platter.objects.filter(name=order.item).first()
    dinners.append(dinner_platter)
    total.append(order.amount*order.quantity)
  user_profile = User_Profile.objects.get(user=request.user)
  context = {
    'order': existing_order,
    'user_profile': user_profile,
    'dinners': dinners,
    'order_items': order_items,
    'total': sum(total)
  }

  return render(request, "summary.html", context)

@login_required(login_url='/signin')
def confirm_order(request, pk):
  existing_order = Order.objects.get(id=pk)
  user_profile = User_Profile.objects.get(user=request.user)
  if existing_order:
    if user_profile.county and user_profile.House_no:
      existing_order.status = "Closed"
      existing_order.save()
    else:
      messages.info(request, "Update your delivery information")
      return redirect("profile", pk=request.user.username)
  else:
    messages.error(request, "Order not found")
  context = {
    'order': existing_order,
    'user_profile': user_profile
  }

  return render(request, "order-confirmed.html", context)  

@login_required(login_url='/signin')
def logout_view(request):
  logout(request)
  messages.success(request, "Logout successfull")
  return redirect('signin')
