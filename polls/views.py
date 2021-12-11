from django.shortcuts import render
from django.core.mail import send_mail

from .models import Blog, Feedback
from .forms import FeedbackForm



# Create your views here.
# def blog(request):
#     #blog = Blog.objects.all()[:1].get()
#     blog = Blog.objects.filter(name='tuan').get()
#     return render(request, 'blog.html', {'blog': blog})

def handleFeedback(request):
    # create a variable to keep track of the form
    messageSent = False

    if request.method == 'POST':

        form = FeedbackForm(request.POST)
        
         # check if data from the form is clean
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            fromEmail = data['fromEmail']
            message = data['message']
            subject = data['subject']

            fb = Feedback(id=Feedback.objects.count() + 1, name=name, email=fromEmail, subject=subject, message=message)
            fb.save()

            # send the email to the recipent
            send_mail('Feedback', 'Cảm ơn bạn đã gửi phản hồi cho chúng tôi!', 'anonymoustpt11@gmail.com', [fromEmail])

            # set the variable initially created to True
            messageSent = True
    else:
        form = FeedbackForm()

    return render(request, 'contact.html', {
        'form': form,
        'messageSent': messageSent,
    })