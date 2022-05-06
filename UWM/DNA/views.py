from django import forms
from django.shortcuts import render

class NewExcelForm(forms.Form):
    sets = forms.IntegerField(label="How many groups of data do you have (i.e sets of samples)?", min_value=10)
    samples = forms.IntegerField(label="What is the largest number of items in one set of samples?", min_value=1)
    ref_genes = forms.IntegerField(label="How many reference genes do you have?", min_value=1)
    intrest_genes = forms.IntegerField(label="How many genes of interest do you have?", min_value=1)


def index(request):
    if request.method == "POST":
        form = NewExcelForm(request.POST)
        if form.is_valid():
            sets = form.cleaned_data["sets"]
            samples = form.cleaned_data["samples"]
            ref_genes = form.cleaned_data["ref_genes"]
            intrest_genes = form.cleaned_data["intrest_genes"]
        else:
            return render(request, "DNA/index.html",{
                "form": form
            })

    return render(request, "DNA/index.html", {
        "form": NewExcelForm()
    })