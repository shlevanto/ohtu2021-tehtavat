class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    
    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1
    
    def deuce(self):
        score_difference = self.m_score1 - self. m_score2
        if score_difference > 2:
            return "Win for player1"
        if score_difference < -2:
            return "Win for player2"
        
        differences = {
            -2: "Win for player2", 
            -1: "Advantage player2",
            0: "Deuce",
            1: "Advantage player1",
            2: "Win for player1"
            }
        
        return differences[score_difference]

    
    def even(self):
        if self.m_score1 < 4:
            return f"{self.scores[self.m_score1]}-All"
        
        return self.deuce()
    
    def simple(self):
        return f"{self.scores[self.m_score1]}-{self.scores[self.m_score2]}"

    def get_score(self):
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.deuce()

        if self.m_score1 == self.m_score2:
            return self.even()
      
        else:
            return self.simple()
