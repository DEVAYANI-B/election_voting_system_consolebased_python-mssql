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
            (voter.name,voter.age,voter.gender,voter.phone,voter.constituency,voter.voter_id)

        )
        self.conn.commit()
        return True
    def delete_voter(self,voter_id: int)->bool:
        self.get_voter_by_id(voter_id)
        self.cursor.execute("DELETE FROM Voters where voter_id=?", (voter_id,))
        self.conn.commit()
        return True
    def get_voter_by_id(self,voter_id: int)->Voter:
        self.cursor.execute("SELECT * FROM Voters where voter_id=?",(voter_id,))
        row=self.cursor.fetchone()
        if row is None:
            raise VoterNotFoundException(f"Voter with ID {voter_id} not found")
        return Voter(row[0],row[1],row[2],row[3],row[4],row[5])
    def add_election(self,election:Election)->bool:
        try:
            self.cursor.execute(
                "INSERT INTO Elections (election_name,election_date,constituency,status) values (?,?,?,?)",
                (election.election_name,election.election_date,election.constituency,election.status)

            )
            self.conn.commit()
            return True
        except Exception:
            return False
    def update_election_status(self,election_id: int,status: str)->bool:
        self.cursor.execute(
            "UPDATE Elections SET status=? where election_id=?",
            (status,election_id)
        )
        self.conn.commit()
        return True
    def get_elections_by_constituency(self,constituency: str)->List[Election]:
        self.cursor.execute("SELECT * FROM Elections where constituency=?",(constituency,))
        rows=self.cursor.fetchall()
        return [Election(row[0],row[1],row[2],row[3],row[4]) for row in rows]
    def get_election_by_id(self,election_id:int)->Election:
        self.cursor.execute("SELECT * FROM Elections where election_id=?",(election_id,))
        row=self.cursor.fetchone()
        if row is None:
            raise ElectionClosureException(f"Election with ID {election_id} not found")
        return Election(row[0],row[1],row[2],row[3],row[4])
    def cast_vote(self,vote:Vote)->bool:
        if vote.election_id<=0 or vote.voter_id<=0 or vote.candidate_id <=0:
            raise InvalidVoteException("election_id, voter_id and candidate_id must be greater than 0")
        self.get_voter_by_id(vote.voter_id)
        self.cursor.execute(
            "SELECT * FROM Votes where election_id=? and voter_id=?",
            (vote.election_id, vote.voter_id)
        )
        if self.cursor.fetchone() is not None:
            raise InvalidVoteException("Voter has already voted in this election")
        self.get_candidate_by_id(vote.candidate_id)
        try:
            self.cursor.execute(
                "INSERT INTO Votes(election_id,voter_id,candidate_id,vote_date) values (?,?,?,?)",
                (vote.election_id,vote.vote_id,vote.candidate_id,vote.vote_date)

            )
            self.conn.commit()
            return True
        except Exception:
            return False
    def get_votes_by_election(self,election_id: int)->List[Vote]:
        self.cursor.execute("SELECT * FROM Votes where election_id=?",(election_id,))
        rows=self.cursor.fetchall()
        return [Vote(row[0], row[1], row[2], row[3], row[4]) for row in rows]
    def declare_election_result(self,result: ElectionResult)->bool:
        self.cursor.execute("SELECT * FROM Elections where election_id=?",(result.election_id,))
        if self.cursor.fetchone() is None:
            raise ElectionClosureException(f"Election with ID {result.election_id} not found")
        if result.total_votes<0:
            raise ElectionClosureException("total_votes must be >=0")
        valid_statuses=["PENDING", "WON", "LOST", "DRAW"]
        if result.result_status not in valid_statuses:
            raise ElectionClosureException(f"Invalid result_status: {result.result_status}")
        self.cursor.execute(
            "INSERT INTO ElectionResults(election_id,candidate_id,total_votes,result_status) values (?,?,?,?)",
            (result.election_id,result.candidate_id,result.total_votes,result.result_status)

        )
        self.conn.commit()
        return True
    def get_all_election_results(self)->List[ElectionResult]:
        self.cursor.execute("SELECT * FROM ElectionResults")
        rows=self.cursor.fetchall()
        return [ElectionResult(row[0],row[1],row[2],row[3],row[4]) for row in rows]
    def close(self):
        self.cursor.close()
        DBConnection.close_connection()

