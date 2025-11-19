from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from demo import custom_versions


def hello_world(request, *args, **kwargs):
    return HttpResponse("hello_world")


@api_view(["GET"])
def hello_world_drf(request, *args, **kwargs):
    return Response(data={"msg": "hello world"})


@api_view(["GET"])
def demo_version(request, *args, **kwargs):
    version = request.version
    return Response(data={"msg": f"You have hit {version} of demo-api"})


class DemoView(APIView):
    versioning_class = custom_versions.DemoViewVersion

    def get(self, request, *args, **kwargs):
        version = request.version

        return Response(data={"msg": f"You have hit {version}"})


class AnotherView(APIView):
    versioning_class = custom_versions.AnotherViewVersion

    def get(self, request, *args, **kwargs):
        version = request.version
        if version == "v1":
            return Response(data={"msg": "v1 logic"})
        elif version == "v2":
            return Response(data={"msg": "v2 logic"})
