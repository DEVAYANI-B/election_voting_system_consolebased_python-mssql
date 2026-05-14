from typing import List
from dao.election_repository import ElectionRepository
from model.candidate import Candidate
from model.voter import Voter
from model.election import Election
from model.vote import Vote
from model.elecction_result import ElectionResult
from util.db_connection import DBConnection
from exception.candidate_not_found_exception import CandidateNotFoundException
from exception.voter_not_found_exception import VoterNotFoundException
from exception.invalid_vote_exception import InvalidVoteException
from exception.election_closure_exception import ElectionClosureException

class EelectionRepositoryImpl(ElectionRepository):
    def __init__(self):
        self.conn=DBConnection.get_connection()
        self.cursor=self.conn.cursor()
    def add_candidate(self,candidate: Candidate)->bool:
        try:
            self.cursor.execute("INSERT INTO Candidates (name,age,gender,party,constituency) VALUES (?,?,?,?,?)",
            (candidate.name,candidate.age,candidate.gender,candidate.party,candidate.constituency)
            )
            self.conn.commit()
            return True
        except Exception:
            return False
    def update_candidate(self,candidate: Candidate)->bool:
        self.get_candidate_by_id()