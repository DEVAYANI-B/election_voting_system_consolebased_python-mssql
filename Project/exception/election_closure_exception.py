class ElectionClosureException(Exception):
    def __init__(self,message="Election closure error"):
        super().__init__(message)
        self.message=message
    def __str__(self):
        return self.message