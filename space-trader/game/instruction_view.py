import arcade
import arcade.gui
from game import constants
from game import menu_view


class InstructionView(arcade.View):
    """
    Show instructions for the game and then go back to main view.

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

        # Add text
        instruction_text = arcade.gui.UILabel(
            text=constants.INSTRUCTIONS_TEXT, font_size=constants.FONT_SIZE_MEDIUM, text_color=arcade.color.WHITE, )
        self._v_box.add(instruction_text.with_space_around(bottom=40))

        # Create the Back button
        back_button = arcade.gui.UIFlatButton(
            text=constants.BACK_BUTTON_TEXT, width=200)
        back_button.on_click = self.on_click_back
        self._v_box.add(back_button.with_space_around(bottom=20))

        # Create a widget to hold the v_box widget, that will center the buttons
        self._manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self._v_box)
        )

    def on_click_back(self, event):
        """Go back to main menu"""
        menu = menu_view.MenuView()
        self.window.show_view(menu)

    def on_show(self):
        """Set the background color."""
        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)

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
        arcade.draw_text(constants.INSTRUCTION_VIEW_TITLE, constants.SCREEN_WIDTH / 2, line_y,
                         arcade.color.YELLOW, font_size=constants.FONT_SIZE_BIG, anchor_x="center")

        # Draw the Gui
        self._manager.draw()
