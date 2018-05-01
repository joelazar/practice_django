import json

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource
from tastypie.paginator import Paginator
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie.validation import Validation

from .models import Presentation
from .serializers import PrettyJSONSerializer


def send_error(status_code, message):
    response = {"error_message": "%s" % message}
    raise ImmediateHttpResponse(response=HttpResponse(json.dumps(response), status=status_code, content_type="application/json"))


class MyAuthentication(BasicAuthentication):

    def is_authenticated(self, request, **kwargs):
        super(MyAuthentication, self).is_authenticated(request)
        print(request.user.is_authenticated)

        if request.method == 'GET':
            return True
        if request.method == 'PUT':
            try:
                p_id = int(request.get_full_path().split('/')[3])
                if not request.user.is_authenticated:
                    send_error(401, message="You are not logged in.")

                presentation = Presentation.objects.get(id=p_id)
                if presentation.creator != str(request.user).replace('_', ' ').title():
                    send_error(401, message="You are only allowed to edit your own presentations.")
            except (ObjectDoesNotExist, ValueError):
                send_error(400, message="Presentation id does not exist.")

            return True

        return False


class MyAuthorization(Authorization):

    def is_authorized(self, request, object=None):
        if request.method == 'PUT':
            if not request.user.is_authenticated:
                return False
            return True
        else:
            return super(MyAuthorization, self).is_authorized(request, object)


class PresentationResource(ModelResource):
    class Meta:
        allowed_methods = ['get', 'put']
        authentication = MyAuthentication()
        authorization = MyAuthorization()
        filtering = {
            "presentation_id": ('exact',),
            "creator": ALL,
            "title": ALL,
        }
        ordering = ['created_at']
        paginator_class = Paginator
        queryset = Presentation.objects.all()
        resource_name = 'presentation'
        serializer = PrettyJSONSerializer()
        validation = Validation()
