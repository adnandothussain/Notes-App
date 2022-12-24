from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import NoteSerializer
from .models import Note

# Create your views here.


def getNoteHelper(id):
    try:
        return Note.objects.get(id=id)
    except Note.DoesNotExist:
        return None


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getNote(request, pk):
    note = getNoteHelper(id=pk)
    if note == None:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def createNote(request):
    data = {
        'body': request.data['body']
    }
    serializer = NoteSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateNote(request, pk):
    note = getNoteHelper(id=pk)

    if note == None:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    data = {
        'body': request.data['body']
    }
    serializer = NoteSerializer(instance=note, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = getNoteHelper(id=pk)
    if note == None:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    note.delete()
    return Response(pk, status=status.HTTP_200_OK)
