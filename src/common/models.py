# -*- coding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel


class CommonMethods(models.Model):
    _old_obj = None

    @property
    def old_obj(self):
        return self._old_obj

    def _is_created(self):
        if self.pk:
            return True
        return False

    class Meta:
        abstract = True


class CommonModel(TimeStampedModel):
    """
    Common abstract base class.
    """

    name = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
