from django.db import models

# Create your models here.

class users(models.Model):
	user_id = models.CharField(max_length=64, primary_key=True);
	user_name = models.CharField(max_length=128, null=True);
	user_password = models.CharField(max_length=15);
	user_primary_contact = models.IntegerField(max_length=15);
	user_secondary_contact = models.IntegerField(max_length=15, null=True);

	def __str__(self):
		return f"{self.user_name} - {self.user_id} - {self.user_password}"

class courses(models.Model):
	course_name = models.CharField(max_length=64)
	course_id = models.CharField(max_length=64)
	course_description = models.CharField(max_length=1024)
	course_fee = models.IntegerField(null=True)

	def __str__(self):
		return f"{self.course_name} - {self.course_description}"