from __future__ import  unicode_literals
from django.db import transaction
from django.utils.crypto import get_random_string

from rapidsms.contrib.handlers import PatternHandler
from rapidsms.models import Contact
from sms.models import Coordinator,Group,Member

class CreateHandler(PatternHandler):
    pattern = 'create'

    def handle(self):
        """

        :return: creates new group
        """
        created = False
        while not created:

            slug = get_random_string(length=10, allowed_chars='01234567890')
            with transaction.atomic():
                group, created = Group.objects.get_or_create( slug=slug)
                if created:
                    connection = self.msg.connections[0]
                    contact = connection.contact
                    coordinator = connection.coordinator
                    if not contact:
                        #create contact
                        contact = Contact.objects.create(name='')
                        connection.contact = contact
                        connection.save(update_fields=('contact',))

                    Member.objects.create(contact=contact, group=group,
                                           is_creator=False)

                    error_msg = (
                        'Group can only be created by a Field Co-ordinator'
                        'Pliz go back to main menu -> Help'
                    )
                    contacts = Contact.objects.all()
                    if contacts[0]:
                        is_creator= True
                        self.respond("Welcome to Evidence Action Promoter help guide")
                    else:
                        self.respond(error_msg)

                    reply = (
                            'Group "%(code)s" created!'
                            'Use this identifer to SEND msgs or for others to JOIN.'
                    ) % {'slug': slug}
                    self.respond(reply)