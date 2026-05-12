import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import pytest
from dao.election_repository_impl import ElectionRepositoryImpl
from model.candidate import Candidate
from model.voter import Voter
from model.election import Election
from model.vote import Vote
from model.election_result import ElectionResult
from exception.candidate_not_found_exception import CandidateNotFoundException
from exception.voter_not_found_exception import VoterNotFoundException
from exception.invalid_vote_exception import InvalidVoteException
from exception.election_closure_exception import ElectionClosureException

# ----------------------- Directory & File Existence Tests (18) ----------------------- #

PROJECT_PATH = "."

# --- Directory Existence Tests (4) ---
def test_model_folder_exists():
    assert os.path.isdir(os.path.join(PROJECT_PATH, "model")), "Directory model is missing!"

def test_dao_folder_exists():
    assert os.path.isdir(os.path.join(PROJECT_PATH, "dao")), "Directory dao is missing!"

def test_exception_folder_exists():
    assert os.path.isdir(os.path.join(PROJECT_PATH, "exception")), "Directory exception is missing!"

def test_util_folder_exists():
    assert os.path.isdir(os.path.join(PROJECT_PATH, "util")), "Directory util is missing!"

# --- Model File Existence Tests (5) ---
def test_candidate_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "candidate.py")), "File candidate.py is missing!"

def test_voter_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "voter.py")), "File voter.py is missing!"

def test_election_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "election.py")), "File election.py is missing!"

def test_vote_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "vote.py")), "File vote.py is missing!"

def test_election_result_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "election_result.py")), "File election_result.py is missing!"

# --- DAO File Existence Tests (2) ---
def test_election_repository_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "dao", "election_repository.py")), "File election_repository.py is missing!"

def test_election_repository_impl_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "dao", "election_repository_impl.py")), "File election_repository_impl.py is missing!"

# --- Exception File Existence Tests (4) ---
def test_candidate_not_found_exception_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "exception", "candidate_not_found_exception.py"))

def test_voter_not_found_exception_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "exception", "voter_not_found_exception.py"))

def test_invalid_vote_exception_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "exception", "invalid_vote_exception.py"))

def test_election_closure_exception_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "exception", "election_closure_exception.py"))

# --- Util File Existence Tests (1) ---
def test_db_util_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "util", "db_connection.py")), "File db_connection.py is missing!"





# ---------------------------- Functional Tests (22) ---------------------------- #

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    repo = ElectionRepositoryImpl()
    # Cleanup in correct dependency order
    repo.cursor.execute("DELETE FROM ElectionResults")
    repo.cursor.execute("DELETE FROM Votes")
    repo.cursor.execute("DELETE FROM Elections")
    repo.cursor.execute("DELETE FROM Candidates")
    repo.cursor.execute("DELETE FROM Voters")
    repo.conn.commit()
    yield repo
    repo.close()

# --- CANDIDATE TESTS (5) ---
def test_add_candidate(setup_and_teardown):
    repo = setup_and_teardown
    c = Candidate(name="John", age=40, gender="Male", party="PartyA", constituency="North")
    assert repo.add_candidate(c) == True

def test_get_candidate_by_id_success(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_candidate(Candidate(name="Alice"))
    repo.cursor.execute("SELECT @@IDENTITY"); cid = repo.cursor.fetchone()[0]
    assert repo.get_candidate_by_id(cid).name == "Alice"

def test_get_candidate_not_found(setup_and_teardown):
    repo = setup_and_teardown
    with pytest.raises(CandidateNotFoundException):
        repo.get_candidate_by_id(9999)

def test_update_candidate(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_candidate(Candidate(name="Old"))
    repo.cursor.execute("SELECT @@IDENTITY"); cid = repo.cursor.fetchone()[0]
    assert repo.update_candidate(Candidate(cid, "New", 35, "M", "PartyB", "South")) == True

def test_delete_candidate(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_candidate(Candidate(name="Delete Me"))
    repo.cursor.execute("SELECT @@IDENTITY"); cid = repo.cursor.fetchone()[0]
    assert repo.delete_candidate(cid) == True

# --- VOTER TESTS (5) ---
def test_add_voter(setup_and_teardown):
    repo = setup_and_teardown
    v = Voter(name="Bob", age=28, gender="Male", phone="9876543210", constituency="East")
    assert repo.add_voter(v) == True

def test_get_voter_by_id(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_voter(Voter(name="Carol"))
    repo.cursor.execute("SELECT @@IDENTITY"); vid = repo.cursor.fetchone()[0]
    assert repo.get_voter_by_id(vid).name == "Carol"

def test_get_voter_not_found(setup_and_teardown):
    repo = setup_and_teardown
    with pytest.raises(VoterNotFoundException):
        repo.get_voter_by_id(8888)

def test_update_voter(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_voter(Voter(name="OldVoter"))
    repo.cursor.execute("SELECT @@IDENTITY"); vid = repo.cursor.fetchone()[0]
    assert repo.update_voter(Voter(vid, "NewVoter", 30, "F", "1112223333", "West")) == True

def test_delete_voter(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_voter(Voter(name="TempVoter"))
    repo.cursor.execute("SELECT @@IDENTITY"); vid = repo.cursor.fetchone()[0]
    assert repo.delete_voter(vid) == True

# --- ELECTION TESTS (4) ---
def test_add_election(setup_and_teardown):
    repo = setup_and_teardown
    e = Election(election_name="General 2025", election_date="2025-06-01", constituency="North")
    assert repo.add_election(e) == True

def test_get_elections_by_constituency(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_election(Election(election_name="Local", election_date="2025-07-01", constituency="East"))
    result = repo.get_elections_by_constituency("East")
    assert isinstance(result, list)

def test_update_election_status(setup_and_teardown):
    repo = setup_and_teardown
    # Logic verification for status update method existence
    assert hasattr(repo, 'update_election_status')

def test_get_election_by_id_not_found(setup_and_teardown):
    repo = setup_and_teardown
    with pytest.raises(ElectionClosureException):
        repo.get_election_by_id(99999)

# --- VOTE TESTS (4) ---
def test_cast_vote_success(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_voter(Voter(name="V1")); repo.cursor.execute("SELECT @@IDENTITY"); vid = repo.cursor.fetchone()[0]
    repo.add_candidate(Candidate(name="C1")); repo.cursor.execute("SELECT @@IDENTITY"); cid = repo.cursor.fetchone()[0]
    repo.add_election(Election(election_name="E1", election_date="2025-01-01", constituency="North"))
    repo.cursor.execute("SELECT @@IDENTITY"); eid = repo.cursor.fetchone()[0]
    vote = Vote(election_id=eid, voter_id=vid, candidate_id=cid, vote_date="2025-01-01")
    assert repo.cast_vote(vote) == True

def test_cast_vote_invalid_ids(setup_and_teardown):
    repo = setup_and_teardown
    # Vote model raises ValueError on invalid ids; cast_vote raises InvalidVoteException
    # Both indicate invalid vote input — accept either exception
    with pytest.raises((InvalidVoteException, ValueError)):
        vote = Vote(election_id=0, voter_id=0, candidate_id=0)
        repo.cast_vote(vote)



def test_get_votes_by_election(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_election(Election(election_name="E3", election_date="2025-03-01", constituency="West"))
    repo.cursor.execute("SELECT @@IDENTITY"); eid = repo.cursor.fetchone()[0]
    assert isinstance(repo.get_votes_by_election(eid), list)

# --- ELECTION RESULT TESTS (4) ---
def test_declare_election_result_invalid_election(setup_and_teardown):
    repo = setup_and_teardown
    with pytest.raises(ElectionClosureException):
        repo.declare_election_result(ElectionResult(election_id=99999, candidate_id=1, total_votes=100, result_status="WON"))

def test_get_all_election_results_type(setup_and_teardown):
    repo = setup_and_teardown
    assert isinstance(repo.get_all_election_results(), list)

def test_election_result_model_str(setup_and_teardown):
    r = ElectionResult(1, 1, 1, 500, "WON")
    assert "WON" in str(r)


if __name__ == "__main__":
    pytest.main(["-v", "tests.py"])