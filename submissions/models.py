# submissions/models.py
from django.db import models

class AbstractSubmission(models.Model):
    TITLE = [
        ('MSC-S', 'Msc Student'),
        ('PHD-S', 'Phd Student'),
        ('POST-DOC', 'Post-Doc'),
        ('PROF.', 'Prof.'),
        ('ASSO.PROF', 'Associate Prof.'),
        ('ASSI.PROF', 'Assistant Prof.'),
        ('OTHER', 'Other')
    ]
    
    PRESENTATION = [
        ('ORAL', 'Oral presentation.'),
        ('POSTER', 'Poster presentation.')
    ]

    TOPICS = [
        ('TOPIC1', 'Renewable Energy & Sustainability.'),
        ('TOPIC2', 'Hydrogen Technology & Energy Storage.'),
        ('TOPIC3', 'Cross-cutting Challenges & Advanced Materials.'),
        ('TOPIC4', 'Modeling, Simulation & Digitalization.')
    ]

    title = models.CharField(max_length=300,choices=TITLE,default='PHD-S')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20,default='+216 00 000 000')
    institution = models.CharField(max_length=500)
    laboratory = models.CharField(max_length=500)
    presentation = models.CharField(max_length=300,choices=PRESENTATION,default='POSTER')
    subject = models.CharField(max_length=500)
    topic = models.CharField(max_length=500,choices=TOPICS,default='TOPIC1')
    document = models.FileField(upload_to='documents/submissions/abstracts/')
    demande_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        ABSTRACT_INFOS=  '{} {} {} {} {} {} {} {} {} {} {}'.format(
                                    self.title,
                                    self.first_name,
                                    self.last_name,
                                    self.email,
                                    self.phone,
                                    self.institution,
                                    self.laboratory,
                                    self.presentation,
                                    self.subject,
                                    self.topic,
                                    self.document,
                                    self.demande_date)
        return ABSTRACT_INFOS


    def get_document_url(self):
        return self.document.url