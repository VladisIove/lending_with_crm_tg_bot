from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
# Create your models here.

class UserManager(BaseUserManager):
	"""Define a model manager for User model with no username field."""

	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""Create and save a User with the given email and password."""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		"""Create and save a regular User with the given email and password."""
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		"""Create and save a SuperUser with the given email and password."""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)




class User(AbstractUser):
	username = None 
	name = models.CharField(max_length=120, blank=True, null=True, verbose_name='Имя')
	surname = models.CharField(max_length=120, blank=True, null=True, verbose_name='Фамилия')
	email = models.EmailField(max_length=120, blank=False, null=False, unique=True, verbose_name='Email')
	

	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
		)
	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active. ''Unselect this instead of deleting accounts.'
			),
		)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()
	class PERMISION_USER:
		MANAGER=1
		SUPPLIER=2
		STUFF=3
	
	CHOOICE_PREMISSIONS=(
		(PERMISION_USER.MANAGER, 'менеджер'),
        (PERMISION_USER.SUPPLIER, 'поставщик'),
        (PERMISION_USER.STUFF, 'админ')
	)
	
	permission_user = models.PositiveSmallIntegerField(choices=CHOOICE_PREMISSIONS, default=PERMISION_USER.MANAGER)
	
	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.email], **kwargs)

	def __str__(self):
		return 'User: {} , type: {}, permission: {}'.format(self.name, self.surname, self.permission_user)

	class Meta:
		ordering = ['permission_user']