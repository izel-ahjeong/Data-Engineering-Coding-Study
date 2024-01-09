from django.shortcuts import render

def ping(request):

    return render(request, 'form/ping.html')


def pong(request):
    title = request.GET['title']
    content =request.GET['content']

    return render(request, 'form/pong.html', {
        'title' :title,
        'content':content,
    })


