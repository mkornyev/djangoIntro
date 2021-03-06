from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    if 'firstname' in request.GET:
        context['person_name'] = request.GET['firstname']

    # Pass the context to the templated HTML file (aka the "view")
    return render(request, 'intro/greet.html', context)


# The action for the 'greet_get' path.
def greet_post(request):
    if request.method == 'GET':
        return render(request, 'intro/greet-post-form.html')

    # Creates a context dictionary (map) to send data to the templated HTML file
    context = {}

    # The 'name' parameter is not present.  Display error message (using a template)
    if not 'firstname' in request.POST:
        context['message'] = 'Parameter "firstname" was not sent in the POST request'
        return render(request, 'intro/greet-post-message.html', context)

    # The 'name' parameter is present so add it to context and render templated HTML file
    context['person_name'] = request.POST['firstname']
    return render(request, 'intro/greet-post-hello.html', context)


# Action function to display some interesting information in a request
@csrf_exempt
def show(request):
    context = {
        'method':  request.method,
        'scheme':  request.scheme,
        'cookies': request.COOKIES,
        'meta':    request.META,
        'body':    str(request.body)[2:-1],
    }

    header_names = ('HTTP_HOST', 'REMOTE_ADDR','HTTP_REFERER',
                    'CONTENT_TYPE', 'CONTENT_LENGTH', 'QUERY_STRING')

    interesting_data = {}
    for key in header_names:
        if key in request.META:
            interesting_data[key] = request.META[key]
        else:
            interesting_data[key] = ''

    context['interesting'] = interesting_data

    return render(request, 'intro/show.html', context)


# Code for the quiz
def broken_greet(request):
    if request.method == 'GET':
        return render(request, 'intro/quiz-post-form.html')

    context = { 'person_name': request.POST['firstname'] }
    return render(request, 'intro/quiz-post-hello.html', context)
