from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.
    return render(request, 'intro/index.html', {})

def hello_world_no_template(request):
    # Just return an HttpResponse object with the HTML we want to send
    html="""
        <!DOCTYPE HTML>
        <html>
          <head>
              <meta charset="utf-8">
              <title>Hello World</title>
          </head>
          <body>
              <h1>Hello, World!</h1>
          </body>
        </html>
    """
    return HttpResponse(html)


def hello_world(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.
    return render(request, 'intro/hello-world.html', {})


# The action for the 'intro/hello.html' route.
def hello(request):
    # Retrieves the name from the request if the 'name' parameter is present.
    name_to_greet = ''
    if 'name' in request.GET:
        name_to_greet = request.GET['name']

    # Makes the data available to the view as 'person_name', then renders the view
    context = {'person_name':name_to_greet}
    return render(request, 'intro/greet.html', context)
