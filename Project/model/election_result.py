class ElectionResult:
    def __init__(self,result_id=0,election_id=0,candidate_id=0,total_votes=0,result_status="PENDING"):
        if total_votes<0:
            raise ValueError("total_votes must be >=0")
        self.result_id=result_id
        self.election_id=election_id
        self.candidate_id=candidate_id
        self.total_votes=total_votes
        self.result_status=result_status
    def __str__(self):
        return (f"ElectionResult(result_id={self.result_id}, election_id={self.election_id}, "
        f"candidate_id={self.candidate_id}, total_votes={self.total_votes}, "
        f"result_status={self.result_status})")