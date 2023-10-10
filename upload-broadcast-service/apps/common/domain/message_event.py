class MessageEvent:
    def __init__(self, action: str, artifact: dict):
        self.action = action
        self.artifact = artifact
