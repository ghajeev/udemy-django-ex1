from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello bitches!', 'number':100}
    return render(request, 'a_tempos/index.html', context_dict)

def other(request):
    return render(request, 'a_tempos/other.html')

def relative(request):
    return render(request, 'a_tempos/relative_url_templates.html')
