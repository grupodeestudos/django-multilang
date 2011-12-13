# Create your views here.

from django.http import HttpResponse

def nomultilang(view):
    def _wrap(req, **kwargs):
        if 'lang' in kwargs:
            kwargs.pop('lang')
        return view(req, **kwargs)
    return _wrap

def home(r, lang='pt'):
    return HttpResponse("Blog home\n")

def post(r, id, lang='pt'):
    return HttpResponse("Some specific post, id={0}, lang={1}\n".format(id, lang))

@nomultilang
def archive(req, month):
    return HttpResponse("Archive for {0}\n".format(month))
