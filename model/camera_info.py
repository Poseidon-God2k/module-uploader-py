from random import choice
from mongoengine.document import Document, QuerySet
from mongoengine.fields import EnumField, BooleanField, ListField,StringField, DateTimeField, DictField, IntField
from bson.objectid import ObjectId
from datetime import datetime
from enum import Enum

class StreamingTypes(Enum):
    YOUTUBE = "YOUTUBE",
    RTSP = "RTSP"

class CameraInfos(Document):
    uuid = StringField(required=True, default=str(ObjectId()))
    camera_name = StringField(required=True)
    camera_url = StringField(required=True)
    streaming_type: EnumField(StreamingTypes,required= True)
    address = DictField(default = {
        "lat": 0,
        "long": 0,
        "name": ""
    })
    status = BooleanField(required=True, default=False)
    roi = ListField(ListField(IntField(), max_length=2), default=[], required=True)
    lp_roi = ListField(ListField(IntField(), max_length=2), default=[])
    direction_vector = ListField(ListField(IntField()), max_length=2, default=[0,0], required=True)
    updated_at = DateTimeField(default=datetime.now)
    created_at = DateTimeField(default=datetime.now)
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(CameraInfos, self).save(*args, **kwargs)

    @staticmethod
    def get_by_name(camera_name: str):
        try:
            result: CameraInfos = CameraInfos.objects.get(camera_name=camera_name)
            return result
        except Exception:
            return None