# from django.http import HttpResponse




# def hello(request) :
#     num_visits = request.session.get('num_visits', 0) + 1
#     request.session['num_visits'] = num_visits
#     if num_visits > 4 : del(request.session['num_visits'])
#     return HttpResponse('view count='+str(num_visits))


from django.shortcuts import render

# Create your views here.

def view_count(request):
    new_view_count = request.session.get('views', 0) + 1
    request.session['views'] = new_view_count
    response = render(request, 'hello/view_count.html', {'view_count' : new_view_count})
    response.set_cookie('dj4e_cookie', '5de467a7', max_age=1000)
    return response