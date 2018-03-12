from django.db import models

class UserProjects(models.Model):
	pass

class ProjectProfile(models.Model):
	# Can have many to one relation with UserProjects model.
	# This will include all profiles which are added by user
	# using different integration.
	# Though, how to find profile's integration type is not clear yet.
	pass

class ProjectReport(models.Model):
	# Can have many to one relation with UserProjects model.
	pass
