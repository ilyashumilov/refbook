from rest_framework.views import APIView
from .serializers import RefbookSerializer, RefbookElementSerializer
from .models import Refbook, RefbookVersion, RefbookElement
from rest_framework.response import Response
from rest_framework import status, serializers
from django.shortcuts import get_object_or_404
from django.utils import timezone
from drf_spectacular.utils import extend_schema, OpenApiParameter, inline_serializer


class RefbookView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(name='date', location=OpenApiParameter.QUERY, description='date',
                             required=False, type=str),
        ],
        responses={
            200: inline_serializer(
                name='Refbooks',
                fields={
                    'refbooks': RefbookSerializer(many=True)
                }
            )
        }
    )
    def get(self, request):
        queryset = Refbook.objects.all()
        date = request.query_params.get("date")

        if date:
            versions = RefbookVersion.objects.filter(date__range=[date, timezone.now()])
            queryset = Refbook.objects.filter(refbookversion__in=versions)

        serializer = RefbookSerializer(queryset, many=True)
        to_response = {"refbooks": serializer.data}

        return Response(
            to_response,
            status=status.HTTP_200_OK,
        )


class RefbookElementView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(name='version', location=OpenApiParameter.QUERY, description='version',
                             required=False, type=str),
        ],
        responses={
           200: inline_serializer(
               name='Elements',
               fields={
                   'elements': RefbookElementSerializer(many=True)
               }
           )
        }
    )
    def get(self, request, id):

        version = request.query_params.get("version")
        try:
            if version:
                refbooks_versions_query = RefbookVersion.objects.filter(
                    refbook=get_object_or_404(Refbook, id=id)
                ).order_by("-date")[int(version.replace(".0", ""))]
            else:
                refbooks_versions_query = (
                    RefbookVersion.objects.filter(refbook=get_object_or_404(Refbook, id=id))
                    .order_by("-date")
                    .first()
                )
        except:
            return Response(
                "No refbook with that version or id found",
                status=status.HTTP_404_NOT_FOUND,
            )

        queryset = RefbookElement.objects.filter(
            refbook_version=refbooks_versions_query
        )

        serializer = RefbookElementSerializer(queryset, many=True)
        to_response = {"elements": serializer.data}

        return Response(
            to_response,
            status=status.HTTP_200_OK,
        )


class CheckRefbookElementView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(name='version', location=OpenApiParameter.QUERY, description='refbook version',
                             required=False, type=str),
            OpenApiParameter(name='code', location=OpenApiParameter.QUERY, description='code',
                             required=False, type=str),
            OpenApiParameter(name='value', location=OpenApiParameter.QUERY, description='value',
                             required=False, type=str),
        ],
        responses={
           200: inline_serializer(
               name='Elements',
               fields={
                   'status': serializers.BooleanField()
               }
           )
        }
    )
    def get(self, request, id):

        code = request.query_params.get("code")
        value = request.query_params.get("value")
        version = request.query_params.get("version")

        if version:
            try:
                refbooks_versions_query = RefbookVersion.objects.filter(
                    refbook=Refbook.objects.get(id=id)
                ).order_by("-date")[int(version.replace(".0", ""))]
                queryset = RefbookElement.objects.filter(
                    refbook_version=refbooks_versions_query
                )
            except:
                return Response(
                    "No refbook with that version found",
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                "No refbook with that version found",
                status=status.HTTP_404_NOT_FOUND,
            )

        if code:
            queryset = queryset.filter(code=code)

        if value:
            queryset = queryset.filter(value=value)

        if queryset.count() == 0:
            return Response(
                {"status": False},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"status":True},
            status=status.HTTP_200_OK,
        )
