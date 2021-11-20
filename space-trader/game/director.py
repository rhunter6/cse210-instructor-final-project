import arcade
from game import constants
from game.menu_view import MenuView


class Director:
    """
    A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller
    """

    def __init__(self):
        """
        The class constructor.
        """
        self._window = arcade.Window(
            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        self._menu = MenuView()

    def start_game(self):
        """Start the game."""
        self._window.show_view(self._menu)
        arcade.run()
