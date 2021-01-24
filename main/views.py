from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def MercuryPage(request):
    return render(request, 'main/mercury.html')

def VenusPage(request):
    return render(request, 'main/venus.html')

def EarthPage(request):
    return render(request, 'main/earth.html')

def MarsPage(request):
    return render(request, 'main/mars.html')

def JupiterPage(request):
    return render(request, 'main/jupiter.html')

def SaturnPage(request):
    return render(request, 'main/saturn.html')

def UranusPage(request):
    return render(request, 'main/uranus.html')