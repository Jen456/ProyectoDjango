from django.shortcuts import render, HttpResponse

html_base= """ 
<h1> Mi web personal </h1>
<ul> 
    <li> <a href="/"> PORTADA </a> </li>
    <li> <a href="/about-me"> Acerca de  </a> </li>
</ul>

"""
# Create your views here.
def home(request):
    return HttpResponse( html_base +""" 
    <h2> Portada </h2> 
    <p> esta es la portada de bienvenida </p>
    """)

def about(request): 
    return HttpResponse(html_base + """
    <h2> Acerca de </h2> 
    <p>Soy Jenny y soy programadora y estos son mis derechos</p>
    """)