import os
dirname = os.path.dirname(__file__)

class ScoreSaving:

    def read_score(self):
        """Reads the score from file

        Returns:
            int: the score value, or a 0 if there is no set score yet
        """
        with open(os.path.join(dirname, "assets", "score.txt"),
                  "r",encoding="utf-8") as file:
            try:
                score = int(file.read())
            except ValueError:
                score = 0
        return score

    def save_score(self, new):
        """Saves a new score if it's higher than the last saved score

        Args:
            new (int): The new score that is being compared to the old score
        """
        saved = self.read_score()
        if new > saved:
            with open(os.path.join(dirname, "assets", "score.txt"), "w",
                      encoding="utf-8") as file:
                file.write(str(new))
