

from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(req, lang='pt'):
    o = {'path_info': req.path_info}
    return render_to_response('index.html', {'lang': lang, 'o': o})
    #return HttpResponse("The lang was {0}\n".format(lang))
