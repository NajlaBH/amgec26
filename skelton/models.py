from django.db import models

class Contact(models.Model):
    TYPES_ORGANISME=[("C.","CENTRE"),("F.","FACULTE"), ("U.","UNIVERSITE"),("A.","AUTRE")]
    DEMANDE = [
        ('INFO-VENUE', 'VENUE'),
        ('INFO-ABSTRACT', 'ABSTRACT SUBMISSION'),
        ('INFO-PAPER', 'PAPER SUBMISSION'),
        ('INFO-REGISTRATION', 'REGISTRATION'),
        ('OTHER-DEMANDE', 'OTHERS')
    ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20,default='+216 00 000 000')
    demande = models.CharField(max_length=300,choices=DEMANDE,default='INFO-ABSTRACT')
    message = models.TextField()
    demande_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        CONTACT_INFOS=  '{} {} {} {} {} {} {}'.format(
                                    self.first_name, 
                                    self.last_name,
                                    self.email,
                                    self.phone,
                                    self.demande,
                                    self.message,
                                    self.demande_date)
        return CONTACT_INFOS

