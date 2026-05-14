class Vote:
    def __init__(self,vote_id=0,election_id=0,voter_id=0,candidate_id=0,vote_date=""):
        if election_id<=0 or voter_id<=0 or candidate_id<=0:
            raise ValueError(
                "election_id, voter_id and candidate_id must be greater than 0"
            )
        self.vote_id=vote_id
        self.election_id=election_id
        self.voter_id=voter_id
        self.candidate_id=candidate_id
        self.vote_date=vote_date
    def __str__(self):
        return (f"Vote(vote_id={self.vote_id}, election_id={self.election_id}, "
        f"voter_id={self.voter_id}, candidate_id={self.candidate_id}, "
        f"vote_date={self.vote_date})")