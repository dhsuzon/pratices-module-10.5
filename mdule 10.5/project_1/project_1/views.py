from django.shortcuts import render
def index_13(request):
    
    count = "python c++ django java  c#"
    
    return render(request,'home10.html',{'count':count})
def index_14(request):
    
    rand= ['Banana', 'Mango', 'Orange']
    
    return render(request,'home11.html',{'rand':rand})
def index_15(request):
    
    cutingword= ['Banana', 'Mango', 'Orange','python','django']
    
    return render(request,'home12.html',{'cutingword':cutingword})