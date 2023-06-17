from django.shortcuts import render
from django.utils.safestring import mark_safe
from django import forms, template

from . import util


# creating a form class for the layout
class CreateSearch(forms.Form):
    q = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "search", "placeholder": "Search Encyclopedia"}))

# dealing with the fact that the form is only on one page with a custom template tag


def search_form(request):
    q = request.GET.get("q", "")
    form = CreateSearch(request.GET or None, initial={"q": q})
    return {"form": form}

def index(request):
    form = CreateSearch(request.GET or None)
    if form.is_valid():
        q = form.cleaned_data['q']
        print(q)
        
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'form': form
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
        
