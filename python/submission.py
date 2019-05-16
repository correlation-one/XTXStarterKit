import subprocess
from core import Submission

class MySubmission(Submission):

    def run_submission(self):
        while(True):
            ### Get next line of data
            data = self.get_next_data()

            ### Guess 0 every time
            self.submit_prediction(1)


if __name__ == "__main__":
    MySubmission()
