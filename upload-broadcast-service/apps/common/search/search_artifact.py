from abc import ABC, abstractmethod


class SearchArtifact(ABC):

    @abstractmethod
    def add_artifact(self, artifact):
        ...

    @abstractmethod
    def update_artifact(self, artifact):
        ...

    @abstractmethod
    def delete_artifact(self, pk):
        ...

    @abstractmethod
    def list_artifact(self, page_no=0, page_size=10):
        ...

    @abstractmethod
    def search_artifact(self, query, page_no=0, page_size=10):
        ...

    @abstractmethod
    def create_index(self):
        ...

    @abstractmethod
    def delete_index(self):
        ...
