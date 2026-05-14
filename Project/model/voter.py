class Voter:
    def __init__(self,voter_id=0,name="",age=0,gender="",phone="",constituency=""):
        self.voter_id=voter_id
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone
        self.constituency=constituency
    def __str__(self):
        return (f"{self.voter_id} {self.name}"