from django.shortcuts import render

# Create your views here.

# Create Author
def create_author(request):
    if request.method == 'POST':
        author = Author.objects.create(**request.POST.dict())
        return redirect('fetch_author')
    return render(request, 'chapter02/myblog/backend/author/create_author.html')

# Fetch All Authors
def fetch_author(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'chapter02/myblog/backend/author/author.html', context)

# Delete Author
def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect('fetch_author')

# Edit Author
def edit_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        for key, value in request.POST.items():
            setattr(author, key, value)
        author.save()
        return redirect('fetch_author')
    return render(request, 'chapter02/myblog/backend/author/edit_author.html', {'author': author})
