from api.models import Candidat
from api.serializers import CandidatSerializer
from api.models import Recruteur
from api.serializers import RecruteurSerializer
from api.models import Partenaire
from api.serializers import PartenaireSerializer
from api.models import Client
from api.serializers import ClientSerializer
from api.models import Offre
from api.serializers import OffreSerializer
from api.models import Meeting
from api.serializers import MeetingSerializer
from rest_framework import generics

#####
class CandidatList(generics.ListCreateAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer


class CandidatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
######
class RecruteurList(generics.ListCreateAPIView):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer


class RecruteurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer
######

class PartenaireList(generics.ListCreateAPIView):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer


class PartenaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer

######

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
######

class OffreList(generics.ListCreateAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer


class OffreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
######

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer