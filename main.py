
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from ui_fen_viewer import Ui_FenViewer
import string, re


class FenViewer(QWidget, Ui_FenViewer):
    BOARD_HEIGHT = 10
    BOARD_WIDTH = 10

    WHITE = "#CCCCCC"
    WHITETOWN = "#FFFFFF"
    BLACK = "#444444"
    BLACKTOWN = "#000000"
    NEUTRAL = "#309070"

    MOVETO = "#406030"
    MOVEHIT = "#933010"
    MOVEFROM = "#104010"

    def __init__(self):
        super(FenViewer, self).__init__()
        self.setupUi(self)

        self.board_move_colors = []
        self.board_colors = []
        self.board = []
        self.all_moves = []
        self.current_moves_to_display = []

        self.figure_color = {"w": self.WHITE, "b": self.BLACK, "W": self.WHITETOWN, "B": self.BLACKTOWN, "1": self.NEUTRAL}

        # Regex
        self.regex_fen = re.compile("([1WwBb]{10}\/){9}[1WwBb]{10}")
        self.regex_move_list = re.compile("\[(?:(?:[a-j][0-9]-[a-j][0-9]),?)+\]")

        # Connect Signals
        self.le_fen_string.textEdited.connect(self.on_le_fen_string_edited)
        self.le_move_string.textEdited.connect(self.on_le_move_string_edited)
        self.cb_show_all_moves.stateChanged.connect(self.on_cb_show_all_moves)
        self.pb_insert_default_board.pressed.connect(self.on_pb_insert_initial_board)

        self.setup_matrices()
        self.setup_board_labels()

    def setup_matrices(self):
        for y in range(self.BOARD_HEIGHT):
            self.board.append([None])
            self.board_colors.append([])
            self.board_move_colors.append([])
            for x in range(self.BOARD_WIDTH):
                self.board[y].append(None)
                self.board_colors[y].append(self.NEUTRAL)
                self.board_move_colors[y].append(None)

    def setup_board_labels(self):
        for y in range(self.BOARD_HEIGHT):
            for x in range(self.BOARD_WIDTH):
                l = QLabel(self.f_board)
                l.setText(string.ascii_lowercase[x] + str(9 - y))
                l.setFixedHeight(60)
                l.setFixedWidth(60)
                l.setStyleSheet(
                    "border: 1px solid black; qproperty-alignment: AlignCenter; background-color: {0}".format(
                        self.board_colors[x][y]))
                l.move(x * 60, y * 60)
                self.board[x][y] = l

    def update_fields_from_fen(self, fen_str):
        for y, row in enumerate(fen_str.split("/")):
            for x, char in enumerate(list(row)):
                self.board_colors[x][y] = self.figure_color[char]

    def update_fields_from_moves(self):
        for move in self.all_moves:
            if move:
                coord = self._get_coordinates(move)
                to = coord[1]

                color = self.board_colors[to[0]][to[1]]

                self.board_move_colors[to[0]][to[1]] = self.MOVETO if color == self.NEUTRAL else self.MOVEHIT

    def flush_fields_from_moves(self):
        for y in range(self.BOARD_HEIGHT):
            for x in range(self.BOARD_WIDTH):
                self.board_move_colors[x][y] = None

# Parser
    def isFEN(self, fen_string):
        pre_parsed_fen = ""
        rows = fen_string.split("/")
        size = len(rows)
        for index, row in enumerate(rows):
            for char in list(row):
                number_str = re.match("[2-9]", char)
                if number_str:
                    pre_parsed_fen += "1" * int(number_str.group(0))
                else:
                    pre_parsed_fen += char

            if row == "":
                pre_parsed_fen += "1" * 10

            if (size - 1) != index:
                pre_parsed_fen += "/"

        isCorrect = self.regex_fen.fullmatch(pre_parsed_fen)
        return isCorrect != None, pre_parsed_fen

    def isMoves(self, moves_string):
        return not not self.regex_move_list.fullmatch(moves_string)

# UI modification
    def ui_was_correct_fen(self):
        self.le_fen_string.setStyleSheet("border: 1px solid green;")

    def ui_was_wrong_fen(self):
        self.le_fen_string.setStyleSheet("border: 1px solid red;")

    def ui_was_correct_move(self):
        self.le_move_string.setStyleSheet("border: 1px solid green;")

    def ui_was_wrong_move(self):
        self.le_move_string.setStyleSheet("border: 1px solid red;")

    def ui_update_labels(self):
        for y in range(self.BOARD_HEIGHT):
            for x in range(self.BOARD_WIDTH):
                label = self.board[x][y]
                label.setStyleSheet("border: 1px solid black; background-color: {0}".format(self.board_colors[x][y]))

    def ui_update_move_labels(self):
        for y in range(self.BOARD_HEIGHT):
            for x in range(self.BOARD_WIDTH):
                label = self.board[x][y]
                color = self.board_move_colors[x][y]
                if color:
                    label.setStyleSheet("border: 1px solid black; background-color: {0}".format(color))

    def ui_clear_labels(self):
        for y in range(self.BOARD_HEIGHT):
            for x in range(self.BOARD_WIDTH):
                label = self.board[x][y]
                label.setStyleSheet(
                    "border: 1px solid black; background-color: {0}".format(self.NEUTRAL))

    def ui_update_all(self):
        self.ui_update_labels()

        if self.cb_show_all_moves.isChecked():
            self.ui_update_move_labels()

    # Signal Functions
    def on_le_fen_string_edited(self, fen_string):
        is_correct, pre_parsed_fen = self.isFEN(fen_string)
        if is_correct:
            self.ui_was_correct_fen()
            self.update_fields_from_fen(pre_parsed_fen)
            if self.cb_show_all_moves.isChecked() and self.all_moves:
                self.update_fields_from_moves()
            self.ui_update_all()
        else:
            self.ui_was_wrong_fen()

    def on_le_move_string_edited(self, move_string):
        is_correct = self.isMoves(move_string)
        if is_correct:
            self.flush_fields_from_moves()
            self.all_moves = []
            self.all_moves = move_string[1:-1].split(",")
            self.update_fields_from_moves()
            self.ui_update_all()
            self.ui_was_correct_move()
        else:
            self.flush_fields_from_moves()
            self.ui_update_all()
            self.ui_was_wrong_move()

    def on_pb_insert_initial_board(self):
        default_fen = "/1w1w1w1w1w/1w1w1w1w1w/1w1w1w1w1w///b1b1b1b1b1/b1b1b1b1b1/b1b1b1b1b1/"
        self.le_fen_string.setText(default_fen)
        self.on_le_fen_string_edited(default_fen)

    def on_cb_show_all_moves(self, checked):
        if self.all_moves:
            #self.flush_fields_from_moves()
            self.ui_update_all()




# Helpers
    def _get_coordinates(self, move):
        return [(ord(move[0]) - 97, 9 - int(move[1])), (ord(move[3]) - 97, 9 - int(move[4]))]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = FenViewer()
    view.show()
    sys.exit(app.exec_())
