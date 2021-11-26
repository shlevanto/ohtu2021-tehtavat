class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    
    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1
    
    def get_score(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.win_or_tie()

        if self.player1_score == self.player2_score:
            return self.even()

        return self.straight_score()

    def win_or_tie(self):
        score_difference = self.player1_score - self. player2_score
        
        if abs(score_difference) >= 2:
            return self.win(score_difference)
        
        return self.tie(score_difference)

    def win(self, score_difference):
        if score_difference >= 2:
            return "Win for player1"
        
        return "Win for player2"
    
    def tie(self, score_difference): 
        differences = {
            -1: "Advantage player2",
            0: "Deuce",
            1: "Advantage player1",
            }
        
        return differences[score_difference]
    
    def even(self):
        if self.player1_score < 4:
            return f"{self.scores[self.player1_score]}-All"
        
        return self.win_or_tie()
    
    def straight_score(self):
        return f"{self.scores[self.player1_score]}-{self.scores[self.player2_score]}"


