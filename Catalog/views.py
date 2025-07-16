from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def main(request):
    a = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохраняем в модель
            submission = form.save()

            # Сохраняем данные в сессию
            request.session['user_submission'] = {
                'id': submission.id,
                'name': submission.name,
                'email': submission.email,
                'description': submission.description,
                'agreement': submission.data_agreement,
                'timestamp': submission.created_at.isoformat()
            }

            messages.success(request, 'Данные успешно сохранены!')
            a = True
            return redirect('index', a)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = ContactForm()

    return render(request, 'Catalog/main.html', {
        'form': form,
        'title': 'Форма отправки данных',
        'a': a
    })


def resume(request):
    return render (request, 'Catalog/resume.html')


def success_view(request):
    submission_data = request.session.get('user_submission', None)
    if not submission_data:
        return redirect('form_view')

    return render(request, 'submission/success.html', {
        'submission': submission_data,
        'title': 'Успешная отправка'
    })
