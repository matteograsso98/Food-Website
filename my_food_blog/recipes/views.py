from django.http import HttpResponse
from django.template import loader
from .models import Recipe
from django.shortcuts import render

def recipes(request):
  myrecipes = Recipe.objects.all().values()
  template = loader.get_template('all_recipes.html')
  context = {
    'myrecipes': myrecipes,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  myrecipe = Recipe.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myrecipe': myrecipe,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def courses(request):
  template = loader.get_template('courses.html')
  return HttpResponse(template.render())

def thoughts(request):
  template = loader.get_template('thoughts.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))