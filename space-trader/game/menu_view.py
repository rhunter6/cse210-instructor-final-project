import arcade
from game import constants


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)

    def on_draw(self):
        arcade.start_render()
        line_y = constants.SCREEN_HEIGHT - \
            constants.FONT_SIZE_BIG - constants.TEXT_PADDING * 2
        arcade.draw_text("Menu Screen", constants.SCREEN_WIDTH / 2, line_y,
                         arcade.color.YELLOW, font_size=constants.FONT_SIZE_BIG, anchor_x="center")

        line_y -= constants.FONT_SIZE_MEDIUM + constants.TEXT_PADDING * 2
        arcade.draw_text("Instructions", constants.SCREEN_WIDTH / 2, line_y,
                         arcade.color.WHITE, font_size=constants.FONT_SIZE_MEDIUM, anchor_x="center")

        line_y -= constants.FONT_SIZE_MEDIUM + constants.TEXT_PADDING
        arcade.draw_text("Start Game", constants.SCREEN_WIDTH / 2, line_y,
                         arcade.color.WHITE, font_size=constants.FONT_SIZE_MEDIUM, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # instructions_view = InstructionView()
        # self.window.show_view(instructions_view)

        arcade.exit()
