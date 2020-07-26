from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=150, null=True, blank=True)
    updated_by = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        abstract = True


class AgileValue(BaseModel):
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return "%s" % (self.title)


class AgilePrinciple(BaseModel):
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return "%s" % (self.title)
