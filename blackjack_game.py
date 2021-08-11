from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        self.player_list = []
        self.dealer = Dealer()
        for name in player_names:
            self.player_list.append(Player(name, self.dealer))

    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """
        output = ''
        for game in range(num_rounds):
            self.dealer.shuffle_deck()
            for player in self.player_list:
                self.dealer.signal_hit(player)
            self.dealer.signal_hit(self.dealer)    
            for player in self.player_list:
                self.dealer.signal_hit(player)
            self.dealer.signal_hit(self.dealer)
            for player in self.player_list:
                player.play_round()
            self.dealer.play_round()
            output += 'Round '+str(game+1)+'\n'
            output += str(self.dealer) + '\n'
            for player in self.player_list:
                if player.card_sum > 21:
                    player.record_loss()
                elif player.card_sum == self.dealer.card_sum:
                    player.record_tie()
                elif self.dealer.card_sum > player.card_sum:
                    player.record_loss()
                elif player.card_sum > self.dealer.card_sum:
                    player.record_win()       
                elif self.dealer.card_sum > 21 and player.card_sum <= 21:
                    player.record_win()
                output += str(player)+ '\n'
                player.discard_hand()
            self.dealer.discard_hand()
        return output[:-1]
                
        

            
        

    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """

        for players in self.player_list:
            players.discard_hand()
            players.reset_stats()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
