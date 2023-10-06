import uuid


def get_image_uri(self, filename):
    name, ext = filename.split('.')
    return 'artifact/images/%s.%s' % (uuid.uuid4().__str__(), ext)


def get_video_uri(self, filename):
    name, ext = filename.split('.')
    return 'artifact/videos/%s.%s' % (uuid.uuid4().__str__(), ext)
