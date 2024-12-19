from .models import WatchesUploads
from django import forms

class UploadForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
        max_digits=10,
        decimal_places=2
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=True
    )

    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = WatchesUploads
        fields = ['name', 'price', 'description', 'image']
