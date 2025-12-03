from django import forms


class URLForm(forms.Form):
    original_url = forms.URLField(
        label="",
        widget=forms.URLInput(attrs={
            "placeholder": "Enter a long URL, for example https://example.com/very/long/path",
            "class": "w-full p-2 border rounded",
            "autocomplete": "off",
        }),
        max_length=2048,
    )
