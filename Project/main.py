
class ElectionApp:

    def __init__(self):
        self.repo = ElectionRepositoryImpl()

#Write your code here

if __name__ == "__main__":
    app = ElectionApp()
    app.run()
