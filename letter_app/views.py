from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UploadedFile
from .forms import FileUploadForm

@login_required
def letter_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'letter_app/letter_list.html', {'files': files})

@login_required
def view_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, id=file_id)
    return render(request, 'letter_app/view_file.html', {'file': uploaded_file})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.uploaded_by = request.user
            file_instance.save()
            return redirect('letter_app:letter_list')
    else:
        form = FileUploadForm()
    return render(request, 'letter_app/upload_file.html', {'form': form})

@login_required
def delete_file(request, file_id):
    file_to_delete = get_object_or_404(UploadedFile, id=file_id)

    if request.method == 'POST':
        file_to_delete.delete()
        return redirect('letter_app:letter_list')

    return render(request, 'letter_app/delete_file.html', {'file': file_to_delete})