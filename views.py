from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext

from models import *
from forms import *

def cdbform(request, template):
    if request.method == 'POST':
	form = CDBForm(template=template, data=request.POST)
	if form.is_valid():
	    data = form.save()
	    tmpl = get_template('sample.html')
	    html = tmpl.render(RequestContext(request, {'data': data}))
	    return HttpResponse(html)
    else:
	form = CDBForm(template=template)
    tmpl = get_template('sample.html')
    html = tmpl.render(RequestContext(request, {'form': form}))
    return HttpResponse(html)

