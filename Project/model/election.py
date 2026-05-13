class Election:
    def __init__(self,election_id=0,election_name="",election_date="",constituency="",status="UPCOMING"):
        self.election_id=election_id
        self.election_name=election_name
        self.election_date=election_date
        self.constituency=constituency
        self.status=status
    def __str__