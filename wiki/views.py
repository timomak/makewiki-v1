from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpRequest

def index(request):
    # return render(request, 'wiki/templates/base.html')
    return HttpRequest("Hello World!")

class PageList(ListView):
    """
    PageList will list all the pages.
    - get() retuns query set of all the pages.

    Runtime: O(n)

    CHALLENGES:
      1. On GET, display a homepage that shows all Pages in your wiki.
      2. Replace this CHALLENGE text with a descriptive docstring for PageList.
      3. Replace pass below with the code to render a template named `list.html`.
    """
    model = Page
    # template_name = 'wiki/list.html'
    # context_object_name = 'page_list'

    def get(self, request):
        """ Returns a list of wiki pages. """
        # return Page.objects.order_by('-created')[:5]
        pages = self.get_queryset().all()
        return render(request, 'wiki/list.html', { 'pages': pages })


class PageDetailView(DetailView):
    """
    CHALLENGES:
      1. On GET, render a template named `page.html`.
      2. Replace this docstring with a description of what thos accomplishes.

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    model = Page
    # template_name = 'wiki/page.html'

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'wiki/page.html', { 'page': page })

    def post(self, request, slug):
        pass
