from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleSlugDescriptionModel
)
from utils.model_abstracts import UUIDModel 

# TimeStampedModel - An Abstract Base Class model that provides self-managed created and modified fields.
# TitleSlugDescriptionModel - An Abstract Base Class model that, like the TitleDescriptionModel, provides title and description fields but also provides a self-managed slug field which populates from the title.
# UUIDModel - Our own abstract model in utils/model_abstracts.py
class Movie(
    UUIDModel,
    TimeStampedModel,
    TitleSlugDescriptionModel):
    
    """
    movies.Movie
    Stores a single movie entry
    """

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ["year"]                 # Optional “-” prefix, which indicates descending order.

    def __str__(self):
        return self.title

    year = models.PositiveIntegerField()