from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
from django import forms 

from . import util


# creating a form class for the layout
class CreateSearch(forms.Form):
    q = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "search", "placeholder": "Search Encyclopedia"}))

# creating a form classs for the create page
class CreatePage(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': "Title", 'maxlength': '50'}))
    mark_down = forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder": 'Write the markdown', 'rows': '20', 'column': '6'}))



# dealing with the fact that the form is only on one page with a custom template tag


def search_form(request):
    q = request.GET.get("q", "")
    form = CreateSearch(request.GET or None, initial={"q": q})
    return {"form": form}

def index(request):
    form = CreateSearch(request.GET or None)
    # making sure the form is valid 
    if form.is_valid():
        # grabbing the data from the form 
        q = form.cleaned_data['q'] 

        # find all the matching substrings
        matching = [s for s in util.list_entries() if q in s]
        
        # if match found return match
        if q in util.list_entries():
            page_md = util.get_entry(q)
            html = util.md_to_html(page_md)
            return render(request, 'encyclopedia/pages.html', {
                'title': q, 'body': mark_safe(html)
            })
        # else if check for matching 
        elif matching:
            return render(request, 'encyclopedia/substring.html', {
                'substrings': matching
            })
        # else return not found
        else:
            # making the html safe for insertion
            text = '<h1>404</h1><p>Page Not found</p>'
            return render(request, 'encyclopedia/pages.html', {
            'title': 'Page Not Found', 'body': mark_safe(text)
        })
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
        
def create(request):
    form = CreatePage(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data['title']
        print(title)
    return render(request, 'encyclopedia/creation.html', {
        'forms': CreatePage(),
        'title': 'Create new page',
    })