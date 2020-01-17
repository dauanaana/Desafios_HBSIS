from app.deck import Deck
from app.cartas import A, Dois, Tres, Quatro, Cinco, Seis, Sete, Oito,Nove, Dez, J, Q, K

class BlackJack():
    def __init__(self):
        full_cartas = []
        cartas = [
            A(),
            Dois(),
            Tres(),
            Quatro(),
            Cinco(),
            Seis(),
            Sete(),
            Oito(),
            Nove(),
            Dez(),
            J(),
            Q(),
            K()
        ]
        for i in range(4):
            for carta in cartas:
                full_cartas.append(carta)
        self._deck = Deck(full_cartas)
        self.player_hand = []
        self.score = 0

    def play(self):
        self._deck.shuffle_deck()
        while self.score < 21:
            self._round()
            if self._is_done():
                self.finish()

    def apresentacao(self):
        print('='*55)
        print('BlackJack')
        
    def _round(self):
        input('Aperte enter para virar uma carta')
        carta = self._deck.get_pega_carta()
        self.player_hand.append(carta)
        self._calcular_pontos(carta)
        print(f"Você virou a carta {carta.name}")
        print(f"Pontuação: {self.score}")

    def _is_done(self):
        if self.score >= 21:
            return True

    def _calcular_pontos(self, carta):
        self.score = sum(map(lambda carta: carta.value, self.player_hand))

    def finish(self):
        mensagem = "BLACKJACK" if self.score == 21 else "Você Perdeu..."

        print("-" * 55)
        print(f"{mensagem::^55}")
        print("-" * 55)
        print(f"Pontuação total: {self.score}")


    @patch('app.deck.blackjack.BlackJack._calculate_score')
    @patch('app.deck.deck.Deck.get_a_card')
    @patch('app.deck.blackjack.print')
    @patch('app.deck.blackjack.input')
    def test_if_get_a_card_in_a_round_works(self, mock_input, mock_print, mock_deck_get_a_card, mock_calculate_score):
        mock_card = Mock(name='A', value=10)
        mock_deck_get_a_card.return_value = mock_card

        mock_calculate_score.return_value = 10
        blackjack = BlackJack()

        result = blackjack._round()
        self.assertEqual(result, blackjack._score)
        self.assertTrue(mock_deck_get_a_card.called_once)
        self.assertEqual(mock_calculate_score.call_count, 1)


