from django.shortcuts import render

# Create your views here.
def home(requests):
   person = [
      {'name' : 'Ram Kc', 'age': '17', 'remarks': 'Pass'},
      {'name' : 'Sita Karki', 'age': '19', 'remarks': 'Pass'},
      {'name' : 'Gopal Kc', 'age': '18', 'remarks': 'Pass'},
      {'name' : 'Govinda Thapa', 'age': '18', 'remarks': 'Fail'}
             ]
   return render (requests, "index.html", context={'person':person, 'page':'Myportfolio'} )

def about(requests):
   return render(requests, "about.html", context={'page' : 'About'})