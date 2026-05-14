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
        self.get_candidate_by_id(candidate.Candidate_id)
        self.cursor.execute(
            "UPDATE Candidates SET name=?,age=?,gender=?,party=?,constituency=? where candidate_id=?"
            (candidate.name,candidate.age,candidate.gender,candidate.party,candidate.constituency,candidate.candidate_id)

        )
        self.conn.commit()
        return True
    def delete_candidates(self,candidate_id: int)-> bool:
        self.get_candidate_by_id(candidate_id)
        self.cursor.execute("DELETE FROM Candidates where candidate_id=?",(candidate_id,))
        self.conn.commit()
        return True
    def get_candidate_by_id(self,candidate_id: int)->Candidate:
        self.cursor.execute("SELECT * FROM Candidates where candidate_id=?",
        (candidate_id,))
        row=self.cursor.fetchone()
        if row is None:
            raise CandidateNotFoundException(f"Candidate with ID {candidate_id} not found")
        return Candidate(row[0], row[1], row[2], row[3], row[4], row[5])
    def add_voter(self,voter: Voter)->bool:
        try:
            self.cursor.execute(
                "INSERT INTO Voters(name,age,gender,phone,constituency) values (?,?,?,?,?)",
                (voter.name,voter.age,voter.gender,voter.phone,voter.constituency)

            )
            self.conn.commit()
            return True
        except Exception:
            return False
    def update_voter(self,voter:Voter)->bool:
        self.get_voter_by_id(voter.voter_id)
        self.cursor.execute(
            "UPDATE Voters SET name=?,age=?,gender=?,phone=?,constituency=? where voter_id=?",
        )