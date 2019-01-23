from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.
    return render(request, 'intro/index.html', {})

def hello_world(request):
    # Just return an HttpResponse object with the HTML we want to send
    html = """
        <!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Hello World</title>
            </head>
            <body>
                <h1>Hello World!</h1>
            </body>
        </html>
    """
    return HttpResponse(html)


def hello_world_with_template(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.
    return render(request, 'intro/hello-world.html', {})


# The action for the 'greet_get' path.
def greet_get(request):
    # Create a context dictionary (map) to send data to the templated HTML file
    context = {}

    # Retrieve the 'name' parameter, if present, and add it to the context
    if 'name' in request.GET:
        context['person_name'] = request.GET['name']

    # Pass the context to the templated HTML file (aka the "view")
    return render(request, 'intro/greet.html', context)


# The action for the 'greet_get' path.
def greet_post(request):
    if request.method == 'GET':
        return render(request, 'intro/greet-post-form.html')

    # Creates a context dictionary (map) to send data to the templated HTML file
    context = {}

    # If 'name' parameter is present, add it to context, render templated HTML file
    if 'name' in request.POST:
        context['person_name'] = request.POST['name']
        return render(request, 'intro/greet-post-hello.html', context)

    # The 'name' parameter is not present.  Display error message (using template)
    context['message'] = 'Parameter "name" was not sent in the POST request'
    return render(request, 'intro/greet-post-message.html', context)
