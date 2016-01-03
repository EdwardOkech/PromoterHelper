
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# from django.utils.encoding import python_2_unicode_compatible
from rapidsms.models import Contact

#


class Coordinator(models.Model):
    """
     List of area co-ordinators
    """
    name = models.ForeignKey(Contact)
    phone = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=75, unique=True)

    def __str__(self):
        return 'Coordinator %s' % self.name

#


class Group(models.Model):
    """
    Grouping promoters in area of operation basis  i.e KRA2-Migori, KRA3-Kuria
    """
    slug = models.SlugField(max_length=10, unique=True, default='')
    created_on = models.DateTimeField(default=timezone.now)
    # coordinator = models.ForeignKey(Coordinator, default='coordinator')

    def __str__(self):
        return 'Group %s' % self.slug


# @python_2_unicode_compatible
class Member(models.Model):
    """
    Member of an SMS group
    """
    contact = models.ForeignKey(Contact)
    group = models.ForeignKey(Group)
    is_creator = models.BooleanField(default=False, blank=True)
    joined_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s/%s' % (self.group, self.contact)

