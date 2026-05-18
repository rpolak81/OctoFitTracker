from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']


def serialize(doc):
    """Zamień ObjectId na string, _id na id."""
    result = {}
    for k, v in doc.items():
        if k == '_id':
            result['id'] = str(v) if isinstance(v, ObjectId) else v
        elif isinstance(v, ObjectId):
            result[k] = str(v)
        else:
            result[k] = v
    return result


@api_view(['GET'])
def users_list(request):
    return Response([serialize(d) for d in db['users'].find()])


@api_view(['GET'])
def teams_list(request):
    return Response([serialize(d) for d in db['teams'].find()])


@api_view(['GET'])
def activities_list(request):
    return Response([serialize(d) for d in db['activities'].find()])


@api_view(['GET'])
def workouts_list(request):
    return Response([serialize(d) for d in db['workouts'].find()])


@api_view(['GET'])
def leaderboard_list(request):
    entries = list(db['leaderboard'].find())
    entries.sort(key=lambda x: x.get('score', 0), reverse=True)
    return Response([serialize(d) for d in entries])
