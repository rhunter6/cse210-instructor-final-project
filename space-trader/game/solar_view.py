import arcade
import arcade.gui
from game import constants


class SolarView(arcade.View):
    """
    A view of the solar system for the game.

    Stereotype:
        User Interfacer
    """

    def __init__(self):
        """
        The class constructor.  This sets up the locations to trade in the game.
        """
        super().__init__()

        # a UIManager to handle the UI.
        self._manager = arcade.gui.UIManager()
        self._manager.enable()

        self._resources = None

    def setup(self):
        """
        Setup the game before playing the first time.
        """
        # Create the 3 planets you can trade with
        planets = {
            "Planet 1": {"x": 20, "y": 20},
            "Planet 2": {"x": 500, "y": 400},
            "Planet 3": {"x": 100, "y": 300},
        }
        for name, planet in planets.items():
            planet_button = arcade.gui.UIFlatButton(
                text=name, style={"bg_color": arcade.color.RED_BROWN})
            planet_button.on_click = self.on_planet_click
            self._manager.add(arcade.gui.UIAnchorWidget(
                anchor_x="left",
                align_x=planet["x"],
                anchor_y="bottom",
                align_y=planet["y"],
                child=planet_button)
            )

        self._resources = [constants.RESOURCE_ONE_START,
                           constants.RESOURCE_TWO_START,
                           constants.RESOURCE_THREE_START]

    def on_planet_click(self, event):
        """Show the instructions"""
        print("Planet: ", event.source.text)

    def on_show(self):
        """Set the background color."""
        arcade.set_background_color(arcade.color.BLACK)

    def on_hide_view(self):
        """Disable the gui manager"""
        super().on_hide_view()
        self._manager.disable()

    def on_draw(self):
        """Draw the buttons"""
        arcade.start_render()

        # Draw a title for the screen.
        line_y = constants.SCREEN_HEIGHT - \
            constants.FONT_SIZE_BIG - constants.TEXT_PADDING * 2
        arcade.draw_text(constants.SOLAR_VIEW_TITLE, constants.SCREEN_WIDTH / 2, line_y,
                         arcade.color.YELLOW, font_size=constants.FONT_SIZE_BIG, anchor_x="center")

        # Draw the Gui
        self._manager.draw()
