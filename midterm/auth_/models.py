from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class MainUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def createuser(self, email, password=None, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = self.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email, password = None, *extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,email, password = None, *extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_stuff', True)
        return self._create_user(email, password, **extra_fields)