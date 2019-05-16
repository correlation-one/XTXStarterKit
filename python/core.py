import sys

class Submission():
    def __init__(self):
        try:
            self.run_submission()
        except AttributeError():
            e_print()
        except EOFError as e:
            pass

    def get_next_data(self):
        """
        Reads input from standard input

        Use this to supply your model with input
        Input will not be supplied until output is 
        generated for the previous input
        """
        return input()

    def submit_prediction(self, prediction):
        """
        Submits your prediction to standard output
        """
        print(str(prediction))

    def e_print(self, msg):
        """
        Prints to standard error

        Use this to debug / develop. 
        This output will not be scored
        """
        print(msg, file=sys.stderr)

