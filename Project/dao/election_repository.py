from abc import ABC, abstractmethod
from typing import List
from model.candidate import Candidate
from model.voter import Voter
from model.election import Election
from model.vote import Vote
from model.election_result import ElectionResult


class ElectionRepository(ABC):
    @abstractmethod
    def add_candidate(self,candidate: Candidate)-> bool:
        pass
    @abstractmethod
    def update_candidate(self,candidate:Candidate)->bool:
        pass
    @abstractmethod
    def delete_candidate(self,candidate_id: int)->bool:
        pass

    @abstractmethod
    def get_candidate_by_id(self,candidate_id: int)-> Candidate:
        pass
    @abstractmethod
    def add_voter(self,voter: Voter)->bool:
        pass
    @abstractmethod
    def update_voter(self,voter:Voter)->bool:
        pass
    @abstractmethod
    def delete_voter(self,voter_id:int)->bool:
        pass
    @abstractmethod
    def get_voter_by_id(self,voter_id:int)->Voter:
        pass
    @abstractmethod
    def add_election(self,election):
        pass
    @abstractmethod
    def update_election_status(self,election_id:int,status:str)->bool:
        pass
    @abstractmethod
    def 
    @abstractmethod
    def cast_vote(self,vote):
        pass
    @abstractmethod
    def declare_election_result(self,result):
        pass
        