# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
# Create your views here.
import urllib2
import json
import inspect
from py2js.decorator import JavaScript
from py2js import convert_py2js
from math import sqrt



def scopeFunc(dscope, data):
    def success(sdata, a, b, c):
        alert(JSON.stringify(sdata)+data)
        pass
    dhttp.get('resty').success(success)
    dscope['style'] = js('john'+data)
    pass
   
def registerFunc(func):
    return "$scope.%s = function(d) { %s(dict($scope.data), d);}" % (func.__name__, func.__name__)
    
# Create your views here.

def salamresty(request):
    return HttpResponse(json.dumps({'name':'bob'}), content_type="application/json")

def salam(request, *args, **kwargs):
    """
    Returns a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    Uses a RequestContext by default.
    """
    httpresponse_kwargs = {
    'content_type': kwargs.pop('content_type', None),
    'status': kwargs.pop('status', None),
    }
    if 'context_instance' in kwargs:
        context_instance = kwargs.pop('context_instance')
    if kwargs.get('current_app', None):
        raise ValueError('If you provide a context_instance you must '
                         'set its current_app before calling render()')
    else:
        current_app = kwargs.pop('current_app', None)
        context_instance = RequestContext(request, current_app=current_app)

    kwargs['context_instance'] = context_instance
    s = loader.render_to_string('index.htm', {'PASTE_FUNCS':(convert_py2js(inspect.getsource(scopeFunc)))+registerFunc(scopeFunc)})
    s = s.replace("<[", "{{").replace("]>", "}}") # <- magic happens *here*
    s = s.replace("&#39;", "'") # <- magic happens *here*
    s = s.replace("&quot;", "'") # <- magic happens *here*

    return HttpResponse(s, **httpresponse_kwargs)
    #return render_to_response('index.htm',{})

