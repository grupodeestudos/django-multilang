

from django.http import HttpResponse



def home(req, lang='pt'):
    return HttpResponse("The lang was {0}\n".format(lang))
