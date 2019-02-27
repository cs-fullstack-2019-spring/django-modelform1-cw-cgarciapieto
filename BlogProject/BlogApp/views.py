from django.shortcuts import render

from .forms import NewBlogForm



# Create your views here.
# created for testing
def index(request):
    return render(request, 'BlogApp/home.html', )

# function that handles grabs the model and  the data is posted/saved back to the database and also rendered on the result.html paging
def blogFunction(request):
    new_form = NewBlogForm()

    if request.method == "POST":
        new_form = NewBlogForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            context = {
                "name": new_form.cleaned_data["text"],
            }
            # returns data to be rendered on the results page
            return render(request, 'BlogApp/results.html', context)  # go back home
        else:
            print('ERROR')
    #
    return render(request, 'BlogApp/home.html', {'form': new_form})



