class ElectionResult:
    def __init__(self,result_id=0,election_id,candidate_id=0,total_votes=0,result_status="PENDING"):
        if total_votes<0:
            raise ValueError("Votes cannot be negative")
        self.result_id=result_id
        self.election_id=election_id
        self.candidate_id=candidate_id
        self.total_votes=total_votes
        self.result_status=result_status
    def __str__(self):
        return f"{self.result_id} {self.result_status}"