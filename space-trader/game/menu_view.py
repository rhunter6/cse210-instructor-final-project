import arcade
import arcade.gui
from game import constants
from game import instruction_view
from game import solar_view


class MenuView(arcade.View):
    """
    The starting menu for the game.  Allows the user to see instructions or start the game.

    Stereotype:
        User Interfacer
    """

    def __init__(self):
        """
        The class constructor.  This sets up the buttons on screen.
        """
        super().__init__()

        # a UIManager to handle the UI.
        self._manager = arcade.gui.UIManager()
        self._manager.enable()

        # Create a vertical BoxGroup to align buttons
        self._v_box = arcade.gui.UIBoxLayout()

        # Create the instruction button
        instructions_button = arcade.gui.UIFlatButton(
            text=constants.INSTRUCTION_BUTTON_TEXT, width=200)
        instructions_button.on_click = self.on_click_instructions
        self._v_box.add(instructions_button.with_space_around(bottom=20))

        # Create the start game button
        start_button = arcade.gui.UIFlatButton(
            text=constants.START_GAME_BUTTON_TEXT, width=200)
        start_button.on_click = self.on_click_start
        self._v_box.add(start_button.with_space_around(bottom=20))

        # Create a widget to hold the v_box widget, that will center the buttons
        self._manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self._v_box)
        )

    def on_click_instructions(self, event):
        """Show the instructions"""
        instructions = instruction_view.InstructionView()
        self.window.show_view(instructions)

    def on_click_start(self, event):
        """Show Solar Sysem View"""
        solar = solar_view.SolarView()
        solar.setup()
        self.window.show_view(solar)

    def on_show(self):
        """Set the background color."""
        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)

    def on_hide_view(self):
        """Disable gui manager"""
        super().on_hide_view()
        self._manager.disable()

    def on_draw(self):
        """Draw the buttons"""
        arcade.start_render()

        # Draw a title for the screen.
        line_y = constants.SCREEN_HEIGHT - \
            constants.FONT_SIZE_BIG - constants.TEXT_PADDING * 2
        arcade.draw_text(constants.MENU_VIEW_TITLE, constants.SCREEN_WIDTH / 2, line_y,
                         arcade.color.YELLOW, font_size=constants.FONT_SIZE_BIG, anchor_x="center")

        # Draw the Gui
        self._manager.draw()
