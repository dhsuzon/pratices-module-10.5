from django.shortcuts import render


def index(request):
    my_text = ['a','b','c','d']
    return render(request, 'index.html', {'my_text': my_text})

def index_2(request):
    values ="django"
    return render(request, 'home.html', {'values': values})
def index_3(request):
    program ="django  is the best framework in python"
    return render(request, 'home1.html', {'program': program})


def index_4(request):
    adress = [
        
        {'name': 'Josh', 'age': 19},
        {'name': 'Dave', 'age': 22},
        {'name': 'Joe', 'age': 31},
    ]
    return render(request, 'home2.html', {'adress': adress})
def index_5(request):
    first_filter =  ['Apple', 'Mango', 'Orange']
    return render(request, 'home3.html', {'first_filter':first_filter})

def index_6(request):
    first_filter =  ['Apple', 'Mango', 'Orange']
    return render(request, 'home3.html', {'first_filter':first_filter})
def index_7(request):
    length_filter =  ['Apple', 'Mango', 'Orange']
    return render(request, 'home3.html', {'length_filter': length_filter })
def index_8(request):
    line = [     'Apple', 'Mango', 'Orange'
                  'Apple', 'Mango', 'Orange'
                  'Apple', 'Mango', 'Orange'
                  'Apple', 'Mango', 'Orange'
            ]           
    return render(request, 'home4.html', {'line':line })
def index_9(request):
    capitallitter ="my name is dider hussain suzon"           
    return render(request, 'home5.html', {'capitallitter':capitallitter })
def index_10(request):
    SMALLlitter ="MY NAME IS SUZON MIA"           
    return render(request, 'home6.html', {'SMALLlitter': SMALLlitter })
def index_11(request):
    titledesign='Its a new day'          
    return render(request, 'home7.html', {' titledesign':  titledesign })

def index_12(request):
    word='bangladesh india maldives malasiya sylhet daka'          
    return render(request, 'home8.html', {' word':  word })
def index_of(request):
    wordchar='bangladesh india maldives malasiya sylhet daka'          
    return render(request, 'home9.html', {' wordchar':  wordchar })

