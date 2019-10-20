from django import forms

class PostForm(forms.Form):
    title = forms.CharField(
        label= 'Judul',
        max_length= 50,
        widget= forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Masukkan Judul'
            }
        )        
    )
    category = forms.ChoiceField(
        label='Kategori',
        widget = forms.RadioSelect(
            attrs={
                'class':'form-check-input',
            }
        ),
        choices= [
            ('tech', 'Teknologi'),
            ('bussiness', 'Bisnis'),
            ('health', 'Kesehatan'),
        ]
    )
    body = forms.CharField(
        label='Isi Postingan',
        widget=forms.Textarea(
            attrs= {
                'class': 'form-control',
                'placeholder':'Masukkan isi postingan'
            }
        ) 
    )

    def clean_title(self):
        title_input = self.cleaned_data.get('title')

        if 'Hoax' in title_input:
            raise forms.ValidationError("Tidak boleh ada berita hoax")

        return title_input

    def clean_body(self):
        body_input = self.cleaned_data.get('body')

        if 'Cebong' in body_input:
            raise forms.ValidationError("Tidak boleh ada kata kasar")

        return body_input