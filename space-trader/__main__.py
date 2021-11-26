import arcade
from game import constants
from game.menu_view import MenuView


def main():
    # Setup the game and start it.
    window = arcade.Window(
        constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()
