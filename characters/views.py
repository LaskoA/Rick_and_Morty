import random

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Character
from .serializers import CharacterSerializer


@api_view(["GET"])
def get_random_character(request):
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    random_obj = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_obj)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharactersListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
