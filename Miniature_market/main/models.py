from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

UserModel = get_user_model()


class ShopItem(models.Model):
    SPACE_MARINE = 'space marine'
    ASTRA_MILITARUM = 'astra militarum'
    CHAOS_SPACE_MARINES = 'chaos space marines'
    NECRONS = 'necrons'
    ORKS = 'orks'
    AELDAR = 'aeldar'

    NAME_MAX_LENGTH = 30

    TYPES = [(x, x) for x in (SPACE_MARINE, ASTRA_MILITARUM, CHAOS_SPACE_MARINES, NECRONS, ORKS, AELDAR)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,

    )

    image = models.ImageField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )

    seller = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(0),
        )

    )
    def __str__(self):
        return self.name


class BoughtItem(models.Model):
    SPACE_MARINE = 'space marine'
    ASTRA_MILITARUM = 'astra militarum'
    CHAOS_SPACE_MARINES = 'chaos space marines'
    NECRONS = 'necrons'
    ORKS = 'orks'
    AELDAR = 'aeldar'

    NAME_MAX_LENGTH = 30

    TYPES = [(x, x) for x in (SPACE_MARINE, ASTRA_MILITARUM, CHAOS_SPACE_MARINES, NECRONS, ORKS, AELDAR)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,

    )
    image = models.ImageField()

    buyer = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(0),
        )

    )
    def __str__(self):
        return self.name


class BlogPost(models.Model):
    POST_TITLE_MAX_LENGTH = 30
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length= POST_TITLE_MAX_LENGTH,
    )

    article = models.TextField()

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )

    title_image= models.URLField()

    def __str__(self):
        return self.title