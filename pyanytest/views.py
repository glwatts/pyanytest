from django.http import HttpResponse

def home(request):
    html = "<html><body>Hello World! This is my NEW pythonanywhere test</body></html>"
    return HttpResponse(html)
