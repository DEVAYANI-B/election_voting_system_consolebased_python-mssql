from abc import ABC, abstractmethod

class ElectionRepository(ABC):
    @abstractmethod
    def add_candidate(self,candidate):
        pass
    @abstractmethod
    def get_candidate_by_id(self,candidate_id):
        pass
    @abstractmethod
    def add_voter(self,voter):
        pass
    @abstractmethod
    def get_voter_by_id(self,voter_id):
        pass
    @abstractmethod
    def add_election(self,election):
        pass
    @abstractmethod
    def cast_vote(self,vote):
        pass
    @abstractmethod
    def declar_election_result(self,result):
        pass
        