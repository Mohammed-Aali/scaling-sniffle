from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from . import util


def index(request):
    print('here!')
    if request.method == "POST":
        print('under the post')
        
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def pages(request, title):
    page_md =  util.get_entry(title) 
    if page_md:

        # md_to_html takes advantage of markdown to convert .md to .html
        html = util.md_to_html(page_md)
        return render(request, 'encyclopedia/pages.html', {
            'title': title, 'body': mark_safe(html)
        })
    
    # making the html safe for insertion
    text = '<h1>404</h1><p>Page Not found</p>'
    return render(request, 'encyclopedia/pages.html', {
        'title': 'Page Not Found', 'body': mark_safe(text)
    })
        
