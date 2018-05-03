from django import forms

class ContactoForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=60,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresa tu nombre'}))
    telefono = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresa tu teléfono'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresa tu email', 'type':'email'}))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Ingresa tu mensaje'}))