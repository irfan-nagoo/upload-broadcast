from apps.common.response.base_response import BaseResponse


class ArtifactResponse(BaseResponse):
    def __init__(self, code, message, artifact=None):
        super().__int__(code, message)
        self.artifact = artifact
