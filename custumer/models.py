from cloudinary.models import CloudinaryField
from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

ANIMAL = (
    ('dog', 'Cachorro'),
    ('cat', 'Gato'),
    ('other', 'Outros'),
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError("User must have an email adress")
        if not password:
            raise ValueError("User must have an password")

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self.db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField('email', max_length=255, unique=True)
    active = models.BooleanField('ativo', default=True)
    staff = models.BooleanField('desenvolvedor', default=False)
    admin = models.BooleanField('administrador', default=False)
    timestamp = models.DateTimeField('data criação', auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'


class Pet(models.Model):
    animal = models.CharField('tipo animal', choices=ANIMAL, max_length=5)
    namepet = models.CharField('nome: ', max_length=50)
    birthdate = models.DateField('Data nascimento', auto_now=False, auto_now_add=False)
    age = models.PositiveIntegerField('idade', null=True, blank=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.namepet

    def save(self, *args, **kwargs):
        # self.age = datetime.today().year - self.birthdate.year
        super(Pet, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuario", on_delete=models.CASCADE)
    fullname = models.CharField('nome', max_length=100)
    phone = models.CharField('Telefone', max_length=15)
    image = CloudinaryField('image', blank=True, null=True)
    pet = models.ManyToManyField(Pet, related_name="pets", verbose_name="Animais", blank=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = "Perfis"
        verbose_name = "Perfil"
