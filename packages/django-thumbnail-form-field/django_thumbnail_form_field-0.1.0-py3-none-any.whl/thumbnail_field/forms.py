from django import forms
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class ThumbnailImageFormField(forms.ImageField):
    def __init__(self, output_format='WEBP', quality=70, *args, **kwargs):
        self.output_format = output_format
        self.quality = quality
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        file = super().clean(data, initial)
        if not file: return initial
        if not initial or (hasattr(file, 'name') and hasattr(initial, 'name') and file.name != initial.name):
            thumb_io = self.create_thumbnail(file)
            file = ContentFile(thumb_io.read(), name=f"{getattr(file, 'name', 'image').rsplit('.', 1)[0]}.{str(self.output_format).lower()}")
        return file
    
    def create_thumbnail(self, image):
        try: image.seek(0)
        except Exception: pass
        img = Image.open(image)
        img = img.convert('RGB')
        output_io = BytesIO()
        img.save(output_io, format=self.output_format, quality=self.quality)
        output_io.seek(0)
        return output_io
