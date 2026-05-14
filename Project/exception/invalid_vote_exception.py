class InvalidVoteException(Exception):
    def __init__(self,message="Invalid vote"):
        super().__init__(message)
        self.message=message
    def __str__(self):
        return self.message
    