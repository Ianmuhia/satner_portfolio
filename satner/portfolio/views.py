from django.shortcuts import render
from .models import cv
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


def generate_pdf(request):
    """Generate pdf."""
    # Model data
    context = cv.objects.all()

    # Rendered
    html_string = render_to_string('portfolio/cv.html', {'context': context})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=cv.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'r')
        response.write(output.read())

    return response


def index(request):
    return render(request, 'portfolio/index.html')


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    return render(request, 'portfolio/contact.html')


def services(request):
    return render(request, 'portfolio/services.html')


def portfolio_details(request):
    return render(request, 'portfolio/portfolio-details.html')


def portfolio_home(request):
    return render(request, 'portfolio/portfolioo.html')
