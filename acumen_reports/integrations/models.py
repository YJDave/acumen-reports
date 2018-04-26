import base64
import pickle
import oauth2client
from django.db import models
from oauth2client.contrib.django_util.models import CredentialsField
from django.utils.encoding import smart_text
from useraccounts.models import User
# Derive every integration authentication model from this model, ex:
# class AnalyticsAuth(ProfileAuth):
#     auth_token = models.CharField(max_length=150)


class ProfileAuth(models.Model):
    id = models.OneToOneField(User, primary_key=True)


class FlowField(models.Field):
    def __init__(self, *args, **kwargs):
        if 'null' not in kwargs:
            kwargs['null'] = True
        super(FlowField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'TextField'

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def to_python(self, value):
        if value is None:
            return None
        if isinstance(value, oauth2client.client.Flow):
            return value
        return pickle.loads(base64.b64decode(value))

    def get_prep_value(self, value):
        if value is None:
            return None
        return smart_text(base64.b64encode(pickle.dumps(value)))

    def value_to_string(self, obj):
        """Convert the field value from the provided model to a string.

        Used during model serialization.

        Args:
            obj: db.Model, model object

        Returns:
            string, the serialized field value
        """
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)


class FlowModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    flow = FlowField()


class AnalyticsCredentialModel(ProfileAuth):
    credential = CredentialsField()
