from django import forms
from .models import Author, Book


class AddAuthorForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}))
    date_of_birth = forms.DateField(label='', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder':'DOB'}))

    class Meta:
        model = Author
        fields=(
            'name',
            'date_of_birth',
        )

class AddBookForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}))
    # author = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author'}))
    author = forms.ModelChoiceField(
        queryset= Author.objects.all(),
        label='', 
        widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Author'}))
    published_date = forms.DateField(label='', widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Published date'}))
    isbn = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ISBN'}))
    price = forms.DecimalField(label='', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Price'}))

    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'published_date',
            'isbn',
            'price',
        )