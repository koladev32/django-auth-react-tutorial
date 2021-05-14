from django.db import models
from uuid import uuid4
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class AbstractManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
        return instance


class AbstractModel(models.Model):
    public_id = models.UUIDField(db_index=True, unique=True, editable=False, default=uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = AbstractManager()

    class Meta:
        abstract = True
