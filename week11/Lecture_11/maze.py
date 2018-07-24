# Written by Eric Martin for COMP9021


import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog


class Maze(tk.Tk):
    background_colour = '#FAF5F3'
    line_colour = '#115523'
    space = 15

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Simple, alternating transit mazes')
        menubar = tk.Menu()
        help_menu = tk.Menu(menubar)
        menubar.add_cascade(label = 'Maze Help', menu = help_menu)
        help_menu.add_command(label = 'Input', command = self.input_help)
        help_menu.add_command(label = 'S.a.t. mazes', command = self.sat_mazes_help)
        help_menu.add_command(label = 'Output', command = self.output_help)
        self.config(menu = menubar)

        tk.Label(self, text = 'Level sequence: ').grid(sticky = tk.E, padx = 5, pady = 20)
        self.input = tk.Entry(self, width = 36)
        self.input.grid(row = 0, column = 1, sticky = tk.W)
        self.shown_level_sequence = tk.StringVar()
        tk.Label(self, width = 70, height = 1, textvariable = self.shown_level_sequence,
                                                                                      fg = 'magenta'
                ).grid(columnspan = 2, pady = 20)
        self.maze = tk.Canvas(self, width = 40 * self.space, height = 40 * self.space,
                                                                         bg = self.background_colour
                             )
        self.maze.grid(columnspan = 2, padx = 20)
        tk.Button(self, text = 'Display maze', command = self.display_maze).grid(pady = 20)
        latex_code_button = tk.Button(self, text = 'Save Latex code',
                                                                      command = self.save_latex_code
                                     ).grid(row = 3, column = 1)
        self.displayed_maze = False

    def input_help(self):
        tkinter.messagebox.showinfo('Input',
            'The input should be a permutation of all numbers from 0 to N with N between 3 and 19, '
            'that forms a level sequence, that is:\n'
            ' - starts with 0 and ends in N\n'
            ' - alternates between even and odd numbers\n'
            ' - is such that for all pairs of successive numbers (p1, p2) and (q1, q2) '
            'with p1 and q1 of the same parity (and so also p2 and q2 of the same parity), '
            'the intervals [p1, p2] and [q1, q2] are disjoint or one is included in the other.'
                                   )

    def sat_mazes_help(self):
        tkinter.messagebox.showinfo('S.a.t. mazes',
            'See http://www.math.stonybrook.edu/~tony/mazes/ for a description of simple, '
            'alternative transit (s.a.t.) mazes, and in particular the proof of necessity and '
            'sufficiency for a permutation of the numbers from 0 to N to be the level sequence of '
            'an s.a.t. maze of depth N, from which the current implementation is derived.'
                                   )

    def output_help(self):
        tkinter.messagebox.showinfo('Output',
            'If some input has been provided and the user clicks on either button, then the input '
            'is checked for validity and in case it is valid, the maze determined by the input is '
            'displayed; moreover, in case the user has clicked on the "Save Latex code" button '
            'then Latex code for that maze is generated and saved.\n\n'
            'In case the user clicks on the "Save Latex code" button, a maze has been displayed '
            'and no new input has been provided, then Latex code for the displayed maze is '
            'generated and saved.'
                                   )

    def display_maze(self, input = None):
        if not input:
            input = self.input.get()
            if not input:
                return
        input = self.get_level_sequence(input)
        if not input:
            self.displayed_maze = False
            return
        self.shown_level_sequence.set('Level sequence ' + str(self.level_sequence))
        self.complete_pairs_and_depths(self.left_pairs, self.left_depths)
        self.complete_pairs_and_depths(self.right_pairs, self.right_depths)
        self.maze.delete(tk.ALL)
        self.draw_maze('screen')
        self.displayed_maze = True

    def save_latex_code(self):
        input = self.input.get()
        if input:
            self.display_maze(input)
        if self.displayed_maze:
            self.generate_latex_code()

    def generate_latex_code(self):
        filename = tkinter.filedialog.asksaveasfilename(defaultextension='.tex')
        if filename:
            latex_file = open(filename, 'w')
            print('\\documentclass[10pt]{article}',
                  '\\usepackage{tikz}',
                  '\\pagestyle{empty}',
                  '',
                  '\\begin{document}',
                  '',
                  '\\vspace*{\\fill}',
                  '\\begin{center}',
                  '\\begin{tikzpicture}[scale = 1.5, x = 0.25cm, y = -0.25cm, thick, purple]',
                  sep = '\n', file = latex_file
                 )
            self.draw_maze(latex_file)
            print('\\end{tikzpicture}',
                  '\\end{center}',
                  '\\vspace*{\\fill}',
                  '',
                  '\\end{document}', sep = '\n', file = latex_file
                 )
            latex_file.close()

    def get_level_sequence(self, input):
        self.input.delete(0, tk.END)
        try:
            self.level_sequence = [int(i) for i in input.split()]
        except ValueError:
            tkinter.messagebox.showinfo('Input', 'The input should consist of numbers.')
            return False
        self.max_level = len(self.level_sequence) - 1
        if not 2 < self.max_level < 20:
            tkinter.messagebox.showinfo('Input',
                                             'The input should consist of between 4 and 20 numbers.'
                                       )
            return False
        if set(self.level_sequence) != set(range(len(self.level_sequence))):
            tkinter.messagebox.showinfo('Input',
                                          'The input should consist of 0, 1, 2... N, in some order.'
                                       )
            return False
        if self.level_sequence[0] != 0 or self.level_sequence[self.max_level] != self.max_level:
            tkinter.messagebox.showinfo('Input',
                                    'The input should start with 0 and end with the largest number.'
                                       )
            return False
        if any(self.level_sequence[i] % 2 != i % 2 for i in range(len(self.level_sequence))):
            tkinter.messagebox.showinfo('Input',
                                          'The input should alternate between even and odd numbers.'
                                       )
            return False
        self.left_pairs = {self.level_sequence[i]: self.level_sequence[i + 1]
                                      for  i in range(0, self.max_level - 1 + self.max_level % 2, 2)
                          }
        self.right_pairs = {self.level_sequence[i]: self.level_sequence[i + 1]
                                          for  i in range(1, self.max_level - self.max_level % 2, 2)
                           }
        self.left_depths = {0 : 0}
        self.right_depths = {1 : 0}
        if not self.well_balanced(self.left_pairs, self.left_depths) or\
                                        not self.well_balanced(self.right_pairs, self.right_depths):
            tkinter.messagebox.showinfo('Input', 'The input defines overlapping pairs.')
            return False
        return True

    def well_balanced(self, pairs, depths):
        # If self.level_sequence is [0, 7, 6, 3, 2, 1, 4, 5, 8] then
        # - dealing with left_pairs, namely {0: 7, 2: 1, 4: 5, 6: 3},
        #   we make level_sequence equal to [0, 2, 2, 6, 4, 4, 6, 0];
        # - dealing with right_pairs, namely {1: 4, 3: 2, 5: 8, 7: 6},
        #   we consider {0: 3, 2: 1, 4: 7, 6: 5} (with keys and values shifted by 1)
        #   and we make level_sequence equal to [0, 2, 2, 0, 4, 6, 6, 4].
        level_sequence = []
        for i in sorted(pairs):
            level_sequence.extend((i, pairs[i]))
        shift = 0
        if level_sequence[0]:
            shift = 1
            level_sequence = [x - 1 for x in level_sequence]
        for i in range(0, len(level_sequence), 2):
            level_sequence[pairs[i + shift] - shift] = i
        stack = [level_sequence[0]]
        for i in range(1, len(level_sequence)):
            if not stack or stack[-1] != level_sequence[i]:
                depths[i + shift] = len(stack)
                stack.append(level_sequence[i])
            else:
                stack.pop()
        return stack == []

    def complete_pairs_and_depths(self, pairs, depths):
        keys = tuple(pairs)
        for i in keys:
            pairs[pairs[i]] = i
            if i in depths:
                depths[pairs[i]] = depths[i]
            else:
               depths[i] = depths[pairs[i]]

    def draw_maze(self, where):
        self._draw_maze(where, 1 - self.max_level % 2)

    def _draw_maze(self, where, even):
        # Left half of top horizontal line.
        self.draw_line(where, 0, 0, self.max_level - 1 - even, 0)
        # Right half of top horizontal line.
        self.draw_line(where, self.max_level - even, 0, 2 * self.max_level - even, 0)
        for i in range(1, self.max_level - 1):
            if self.left_depths[i] == self.left_depths[i + 1] and self.left_pairs[i] != i + 1:
                j = self.max_level - self.left_depths[i] - even
            else:
                j = max(self.max_level - self.left_depths[i] - 1 - even,
                                                 self.max_level - self.left_depths[i + 1] - 1 - even
                       )
            if i < j:
                # Horizontal lines in upper left quarter of maze.
                self.draw_line(where, i, i, j, i)
            if self.right_depths[i] == self.right_depths[i + 1] and self.right_pairs[i] != i + 1:
                j = self.max_level + self.right_depths[i] - even
            else:
                j = min(self.max_level + self.right_depths[i] + 1 - even,
                                                self.max_level + self.right_depths[i + 1] + 1 - even
                       )
            if j < 2 * self.max_level - i - even:
                # Horizontal lines in upper right quarter of maze.
                self.draw_line(where, j, i, 2 * self.max_level - i - even, i)
        if not even:
            # Small horizontal line in the middle of maze when odd number of levels.
            self.draw_line(where, self.max_level, self.max_level - 1, self.max_level + 1,
                                                                                  self.max_level - 1
                          )
        for i in range(self.max_level):
            # Horizontal lines in lower half of maze.
            self.draw_line(where, self.max_level - i - 1, self.max_level + i - even,
                                            self.max_level + i + 1 - even, self.max_level + i - even
                          )
        for i in self.left_pairs:
            if self.left_pairs[i] < i or self.left_pairs[i] == i + 1:
                continue
            # Vertical lines in left half of maze that represent right walls.
            self.draw_line(where, self.max_level - self.left_depths[i] - 1 - even, i,
                             self.max_level - self.left_depths[i] - 1 - even, self.left_pairs[i] - 1
                          )
        self.draw_line(where, self.max_level - even, 0, self.max_level - even, self.max_level - 1)
        for i in self.right_pairs:
            if self.right_pairs[i] < i or self.right_pairs[i] == i + 1:
                continue
            # Vertical lines in right half of maze that represent left walls.
            self.draw_line(where, self.max_level + self.right_depths[i] + 1 - even, i,
                           self.max_level + self.right_depths[i] + 1 - even, self.right_pairs[i] - 1
                          )
        for i in range(self.max_level):
            # Vertical lines in left half of maze that represent left walls.
            self.draw_line(where, i, i, i, 2 * self.max_level - i - 1 - even)
            # Vertical lines in right half of maze that represent right walls.
            self.draw_line(where, 2 * self.max_level - i - even, i, 2 * self.max_level - i - even,
                                                                  2 * self.max_level - i - 1 - even
                          )

    def draw_line(self, where, i1, j1, i2, j2):
        if where == 'screen':
            width = 2 * self.max_level + self.max_level % 2 - 1
            height = 2 * self.max_level + self.max_level % 2 - 2
            width_offset = (40 - width) * self.space / 2
            height_offset = (40 - height) * self.space / 2
            self.maze.create_line(i1 * self.space + width_offset, j1 * self.space + height_offset,
                                    i2 * self.space + width_offset, j2 * self.space + height_offset,
                                                                width = 0.5, fill = self.line_colour
                                 )
        else:
            print('\draw(', i1, ', ', j1, ') -- (', i2, ', ', j2, ');', sep = '', file = where)


if __name__ == '__main__':
    Maze().mainloop()
