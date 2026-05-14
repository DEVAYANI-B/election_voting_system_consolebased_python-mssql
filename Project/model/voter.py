class Voter:
    def __init__(self,voter_id=0,name="",age=0,gender="",phone="",constituency=""):
        self.voter_id=voter_id
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone
        self.constituency=constituency
    def __str__(self):
        return (f"Voter(voter_id={self.voter_id}, name={self.name}, "
        f"age={self.age}, gender={self.gender}, phone={self.phone}, "
        f"constituency={self.constituency})")