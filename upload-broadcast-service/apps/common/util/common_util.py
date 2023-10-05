import base64


def get_image_uri(self, filename):
    name, ext = filename.split('.')
    return 'artifact/images/%s.%s' % (base64.b64encode(name.encode()), ext)


def get_video_uri(self, filename):
    name, ext = filename.split('.')
    return 'artifact/videos/%s.%s' % (base64.b64encode(name.encode()), ext)
