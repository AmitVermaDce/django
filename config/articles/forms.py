from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_title = self.cleaned_data
        title = cleaned_title.get('title')
        if title.strip().lower() == 'dummy':
            raise forms.ValidationError('This title is taken')
        return title

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'dummy content':
            self.add_error('title', "Dummy can't be added into title") 
        if "dummy" in content or "dummy" in title.lower():
            # this error is field specific error
            self.add_error("content", "Dummy cannot be added into content")
            # this error is for complete form
            raise forms.ValidationError("Dummy is not allowed")
        return cleaned_data
        