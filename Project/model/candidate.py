class Candidate:
    def __init__(Self,candidate_id=0,name="",age=0,gender="",party="",constituency=""):
        self.candidate=candidate_id
        self.name=name
        self.age=age
        self.gender=gender
        self.party=party
        self.constituency=constituency
    def __str__(self):
        return (f"Candidate(candidate_id={self.candidate_id},name={self.name},
        f"age={self.age}, gender={self.gender}, party= {self.party}, "
        f"constituency={self.constituency})")