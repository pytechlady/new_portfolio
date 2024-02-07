from django.shortcuts import render
from .models import Project, Contact
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.


def home(request):
    return render(request, 'core/home.html', {'status': '200'})

def about(request):
    return render(request, 'core/about.html', {'status': '200'})


def projects(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        source_code = request.POST.get('source_code')
        web_url = request.POST.get('web_url')
        video = request.POST.get('video')
        summary = request.POST.get('summary')
        
        project = Project.objects.create(title=title, source_code=source_code,web_url=web_url, video=video, summary=summary)
        project.save()
        return render(request, 'core/projects.html', {'project': project, 'status': '200'})
        
    elif request.method == 'GET':
        project = Project.objects.all().order_by('-created_at')
        paginator = Paginator(project, 6)
        
        page_number = request.GET.get("page")
        response_obj =paginator.get_page(page_number)
        
        return render(request, 'core/projects.html', {'project': response_obj, 'status': '200'})
        
        
def contactForm(request):
    if request.method == 'POST':
        try:
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            firstname, *lastname_parts = fullname.split(' ')
            lastname = ' '.join(lastname_parts) if lastname_parts else ''
            
            contact = Contact.objects.create(firstname=firstname, lastname=lastname, email_address=email, subject=subject, message=message)
            contact.save()
            response_data = {'success': True, 'message': "Form submitted successfully, we will be in touch.", 'status': '200'}
            
            return JsonResponse(response_data)
        except Exception as e:
            print(f"Exception: {e}")
            response_data = {'success': False, 'message': "There was an error submitting your form. Please try again later.", 'status': '400'}
            return JsonResponse(response_data)

        
        