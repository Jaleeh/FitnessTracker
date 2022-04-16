from dataclasses import field, fields
from xml.parsers.expat import model
import graphene
from .models import Exercise, Session
from graphene_django import DjangoObjectType

class ExerciseType(DjangoObjectType):
    class Meta: 
        model = Exercise
        fields = ("name", "description", "video_slug")
        
class SessionType(DjangoObjectType):
    class Meta:
        model = Session
        fields = ("sets","rep_count","working_weight","pr_weight")
        

class Query(graphene.ObjectType):
    all_exercises = graphene.List(ExerciseType)
    all_sessions = graphene.List(SessionType)   
    
    def resolve_all_ExerciseType(root, info):
        return Exercise.objects.all()
    
    def resolve_all_SessionType(root, info):
        return Session.objects.all()
       

schema = graphene.Schema(query=Query)