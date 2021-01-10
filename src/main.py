# main.py
#
# Copyright 2021 Dave Patrick
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_border_width(6)
        self.set_default_size(250, 250)

        self.header_bar = Gtk.HeaderBar()
        self.header_bar.set_show_close_button(True)
        self.header_bar.props.title = "Tic-Tac-Toe"
        self.set_titlebar(self.header_bar)

        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)
        self.add(grid)

        self.button_state = ["","","","","","","","",""]
        self.num_turn = 0
        self.turn = ''

        self.button1 = Gtk.Button(label=self.button_state[0])
        self.button1.connect("clicked", self.button1_clicked)
        grid.attach(self.button1, 0, 0, 1, 1)
        self.button2 = Gtk.Button(label=self.button_state[1])
        self.button2.connect("clicked", self.button2_clicked)
        grid.attach(self.button2, 1, 0, 1, 1)
        self.button3 = Gtk.Button(label=self.button_state[2])
        self.button3.connect("clicked", self.button3_clicked)
        grid.attach(self.button3, 2, 0, 1, 1)
        self.button4 = Gtk.Button(label=self.button_state[3])
        self.button4.connect("clicked", self.button4_clicked)
        grid.attach(self.button4, 0, 1, 1, 1)
        self.button5 = Gtk.Button(label=self.button_state[4])
        self.button5.connect("clicked", self.button5_clicked)
        grid.attach(self.button5, 1, 1, 1, 1)
        self.button6 = Gtk.Button(label=self.button_state[5])
        self.button6.connect("clicked", self.button6_clicked)
        grid.attach(self.button6, 2, 1, 1, 1)
        self.button7 = Gtk.Button(label=self.button_state[6])
        self.button7.connect("clicked", self.button7_clicked)
        grid.attach(self.button7, 0, 2, 1, 1)
        self.button8 = Gtk.Button(label=self.button_state[7])
        self.button8.connect("clicked", self.button8_clicked)
        grid.attach(self.button8, 1, 2, 1, 1)
        self.button9 = Gtk.Button(label=self.button_state[8])
        self.button9.connect("clicked", self.button9_clicked)
        grid.attach(self.button9, 2, 2, 1, 1)

        self.buttonclear = Gtk.Button()
        icon = Gio.ThemedIcon(name="view-refresh-symbolic")
        self.image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        self.buttonclear.set_image(self.image)
        self.buttonclear.connect("clicked", self.reset)
        self.header_bar.pack_start(self.buttonclear)
        self.buttonclear.set_sensitive(False)

        self.button1.set_vexpand(True)
        self.button4.set_vexpand(True)
        self.button7.set_vexpand(True)

        self.button1.set_hexpand(True)
        self.button2.set_hexpand(True)
        self.button3.set_hexpand(True)

        self.button_state[0] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button_state = ["","","","","","","","",""]
        self.num_turn += 2

    def is_odd(self, num_turn):
        remainder = num_turn % 2
        if remainder > 0:
            self.turn = 'X'
        else:
            self.turn = 'O'

    def button1_clicked(self, widget):
        self.button_state[0] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button1.set_label(self.turn)
        self.button1.set_sensitive(False)
        self.buttonclear.set_sensitive(True)
        self.win_check()

    def button2_clicked(self, widget):
        self.button_state[1] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button2.set_label(self.turn)
        self.button2.set_sensitive(False)
        self.buttonclear.set_sensitive(True)
        self.win_check()

    def button3_clicked(self, widget):
        self.button_state[2] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button3.set_label(self.turn)
        self.button3.set_sensitive(False)
        self.buttonclear.set_sensitive(True)
        self.win_check()

    def button4_clicked(self, widget):
        self.button_state[3] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button4.set_label(self.turn)
        self.button4.set_sensitive(False)
        self.buttonclear.set_sensitive(True)
        self.win_check()

    def button5_clicked(self, widget):
        self.button_state[4] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button5.set_label(self.turn)
        self.button5.set_sensitive(False)
        self.buttonclear.set_sensitive(True)
        self.win_check()

    def button6_clicked(self, widget):
        self.button_state[5] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button6.set_label(self.turn)
        self.button6.set_sensitive(False)
        self.buttonclear.set_sensitive(True)
        self.win_check()

    def button7_clicked(self, widget):
        self.button_state[6] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button7.set_label(self.turn)
        self.button7.set_sensitive(False)
        self.buttonclear.set_sensitive(True)
        self.win_check()

    def button8_clicked(self, widget):
        self.button_state[7] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button8.set_label(self.turn)
        self.button8.set_sensitive(False)
        self.buttonclear.set_sensitive(True)
        self.win_check()

    def button9_clicked(self, widget):
        self.button_state[8] = self.turn
        self.is_odd(self.num_turn)
        self.num_turn += 1
        self.button9.set_label(self.turn)
        self.button9.set_sensitive(False)
        self.buttonclear.set_sensitive(True)
        self.win_check()

    def reset(self, widget):
        self.buttonclear.set_sensitive(False)
        self.header_bar.props.title = "Tic-Tac-Toe"
        self.button_state = ["","","","","","","","",""]
        self.num_turn += 2
        self.button1.set_sensitive(True)
        self.button1.set_label('')
        self.button2.set_sensitive(True)
        self.button2.set_label('')
        self.button3.set_sensitive(True)
        self.button3.set_label('')
        self.button4.set_sensitive(True)
        self.button4.set_label('')
        self.button5.set_sensitive(True)
        self.button5.set_label('')
        self.button6.set_sensitive(True)
        self.button6.set_label('')
        self.button7.set_sensitive(True)
        self.button7.set_label('')
        self.button8.set_sensitive(True)
        self.button8.set_label('')
        self.button9.set_sensitive(True)
        self.button9.set_label('')

    def won(self):
        self.button1.set_sensitive(False)
        self.button2.set_sensitive(False)
        self.button3.set_sensitive(False)
        self.button4.set_sensitive(False)
        self.button5.set_sensitive(False)
        self.button6.set_sensitive(False)
        self.button7.set_sensitive(False)
        self.button8.set_sensitive(False)
        self.button9.set_sensitive(False)

    def win_check(self):
        if self.button_state[0] == 'O' and self.button_state[1] == 'O' and self.button_state[2] == 'O':
            self.won()
            self.header_bar.props.title = "X won"
        elif self.button_state[3] == 'O' and self.button_state[4] == 'O' and self.button_state[5] == 'O':
            self.won()
            self.header_bar.props.title = "X won"
        elif self.button_state[6] == 'O' and self.button_state[7] == 'O' and self.button_state[8] == 'O':
            self.won()
            self.header_bar.props.title = "X won"
        elif self.button_state[0] == 'O' and self.button_state[3] == 'O' and self.button_state[6] == 'O':
            self.won()
            self.header_bar.props.title = "X won"
        elif self.button_state[1] == 'O' and self.button_state[4] == 'O' and self.button_state[7] == 'O':
            self.won()
            self.header_bar.props.title = "X won"
        elif self.button_state[2] == 'O' and self.button_state[5] == 'O' and self.button_state[8] == 'O':
            self.won()
            self.header_bar.props.title = "X won"
        elif self.button_state[2] == 'O' and self.button_state[4] == 'O' and self.button_state[6] == 'O':
            self.won()
            self.header_bar.props.title = "X won"
        elif self.button_state[0] == 'O' and self.button_state[4] == 'O' and self.button_state[8] == 'O':
            self.won()
            self.header_bar.props.title = "X won"
        elif self.button_state[0] == 'X' and self.button_state[1] == 'X' and self.button_state[2] == 'X':
            self.won()
            self.header_bar.props.title = "O won"
        elif self.button_state[3] == 'X' and self.button_state[4] == 'X' and self.button_state[5] == 'X':
            self.won()
            self.header_bar.props.title = "O won"
        elif self.button_state[6] == 'X' and self.button_state[7] == 'X' and self.button_state[8] == 'X':
            self.won()
            self.header_bar.props.title = "O won"
        elif self.button_state[0] == 'X' and self.button_state[3] == 'X' and self.button_state[6] == 'X':
            self.won()
            self.header_bar.props.title = "O won"
        elif self.button_state[1] == 'X' and self.button_state[4] == 'X' and self.button_state[7] == 'X':
            self.won()
            self.header_bar.props.title = "O won"
        elif self.button_state[2] == 'X' and self.button_state[5] == 'X' and self.button_state[8] == 'X':
            self.won()
            self.header_bar.props.title = "O won"
        elif self.button_state[2] == 'X' and self.button_state[4] == 'X' and self.button_state[6] == 'X':
            self.won()
            self.header_bar.props.title = "O won"
        elif self.button_state[0] == 'X' and self.button_state[4] == 'X' and self.button_state[8] == 'X':
            self.won()
            self.header_bar.props.title = "O won"
        elif self.button_state[0] != '' and self.button_state[1] != '' and self.button_state[2] != '' and self.button_state[3] != '' and self.button_state[4] != '' and self.button_state[5] != '' and self.button_state[6] != '' and self.button_state[7] != '' and self.button_state[8] != '':
            self.won()
            self.header_bar.props.title = "Draw"


window = Window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
