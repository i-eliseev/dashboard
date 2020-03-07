from images.models import Image

for image in Image.objects.all():
    image.total_likes = image.users_like.count()
    image.save()