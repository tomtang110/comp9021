# Written by Eric Martin for COMP9021


import tkinter as tk
import tkinter.messagebox
from copy import deepcopy
from random import randrange


class WinningStrategy(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Winning Strategies and Learning')
        menubar = tk.Menu()
        help_menu = tk.Menu(menubar)
        menubar.add_cascade(label = 'Winning Strategies and Learning Help', menu = help_menu)
        help_menu.add_command(label = 'Rules of the game', command = self.rules_help)
        help_menu.add_command(label = 'Search tree', command = self.search_tree_help)
        help_menu.add_command(label = 'Opponent', command = self.opponent_help)
        help_menu.add_command(label = 'Learning', command = self.learning_help)
        self.config(menu = menubar)

        self.search_tree = SearchTree()
        DisplayedSearchTree(self.search_tree.tree).grid()
        SimulationBoard(self.search_tree.tree).grid(row = 0, column = 1)

    def rules_help(self):
        tkinter.messagebox.showinfo('Rules of the game',
            "Pawns can move forward or take an opponent's pawn diagonally.\n\n"
            'Black or red wins when one of its pawns has reached the opposite line, '
            'or the opponent cannot move.')

    def search_tree_help(self):
        tkinter.messagebox.showinfo('Search tree',
            "Click on a state to expand the tree and display the opponent's possible moves, "
            'if any.\n'
            'Control click on a state to collapse the tree and hide all displayed possible '
            'subsequent states, if any.\n\n'
            'The outline of a state is boldfaced if that state is part of a winning strategy; '
            'it can only be for the black player.\n'
            'The outline of a state is dashed boldfaced if that state is part of a winning '
            'strategy at some point in the game, but not from its beginning; '
            'it can be for either the black or the red player.')

    def opponent_help(self):
        tkinter.messagebox.showinfo('Opponent',
            'The opponent is the red player.\n\n'
            'The random opponent randomly choses a state amongst all possible next states.\n\n'
            'The good opponent randomly choses a state amongst all possible next states in case '
            'no such state is part of a winning strategy at that point in the game; otherwise, '
            'it randomly chooses a state amongst all possible next states that happen to be part '
            'of a winning strategy at that point in the game.')

    def learning_help(self):
        tkinter.messagebox.showinfo('Learning',
            'The learner is the black player.\n\n'
            'The learner randomly choses a state amongst all possible next states.\n'
            "When the opponent wins, the learner eliminates the state which made that oppent's "
            'last move possible from its future choices.\n'
            'When the opponent plays, does not win, but all possible next states for the learner '
            "have been eliminated, then the learner 'gives up' and eliminates the state "
            "which made that oppent's move possible from its future choices.\n\n"
            'Learning cannot be improved when enough states have been eliminated and '
            'all possible moves from the learner are part of a winning strategy.')


class State:
    black = 0
    red = 1
    free = 2
    on_track_to_lose = 0
    on_track_to_win = 1
    on_track_for_lucky_win = 2
    width = 36
    third_width = width // 3
    offset = width // 2

    def __init__(self, depth = 0, displayed = False, state = None):
        self.depth = depth
        self.expected_outcome = self.on_track_to_lose
        self.displayed = displayed
        # self.state represents a 3x3 board where each cell contains
        # a black pawn (0), a red pawn (1), or is empty (2).
        self.state = state
        self.code = self.code_state()
        self.x = 0
        self.y = 0
        self.next_states = []

    def code_state(self):
        code = 0
        for i in range(3):
            for j in range(3):
                code = code * 3 + self.state[i][j]
        return code

    def display_state(self, canvas, line):
        for i in range(3):
            for j in range(3):
                x = self.offset + self.depth * self.width
                y = self.offset + line * self.width
                canvas.create_polygon(x + 1, y + 1, x + self.width - 1, y + 1, x + self.width - 1,
                                           y + self.width - 1, x + 1, y + self.width - 1, fill = '',
                                   outline = {self.black: 'black', self.red: 'red'}[self.depth % 2],
                                  width = {self.on_track_to_lose: 1, self.on_track_for_lucky_win: 2,
                                                    self.on_track_to_win: 2}[self.expected_outcome],
                                   dash = {self.on_track_to_lose: 1, self.on_track_for_lucky_win: 3,
                                        self.on_track_to_win: 1}[self.expected_outcome], dashoff = 1
                                     )
                canvas.create_oval(x + j * self.third_width + 3, y + i * self.third_width + 3,
                                         x + j * self.third_width + 8, y + i * self.third_width + 8,
                                    fill = {self.black: 'black', self.red: 'red', self.free: 'white'
                                           }[self.state[i][j]], outline = 'black'
                                  )
                self.x = x
                self.y = y

                
class SearchTree:
    def __init__(self):
        self.tree = State(displayed = True, state = ([State.black] * 3, [State.free] * 3,
                                                                                    [State.red] * 3)
                         )
        self.complete_search_tree(self.tree)
        self.determine_winning_strategy(self.tree)
        self.identify_lucky_wins(self.tree)
        for subtree in self.tree.next_states:
            self.identify_lucky_wins(subtree)

    def complete_search_tree(self, tree):
        next_color = 1 - tree.depth % 2
        next_states = self.determine_next_states(tree.state, next_color)
        if next_states:
            subtrees = [State(depth = tree.depth + 1, state = next_state)
                                                                       for next_state in next_states
                       ]
            tree.next_states = subtrees
            for subtree in subtrees:
                self.complete_search_tree(subtree)

    def determine_next_states(self, state, colour):
        # For Black (0), arrival_line is 2 (lower row).
        # For Red (1), arrival_line is 0 (upper row).
        arrival_line = (1 - colour) * 2
        if 1 - colour in state[2 - arrival_line]:
            return
        # For Black (0), starting_line is 0 (upper row).
        # For Red (1), starting_line is 2 (lower row).
        starting_line = colour * 2
        # Black (0) move from from upper to lower rows, so increasing by 1.
        # Red (1) move from from lower to upper rows, so decreasing by 1.
        direction = arrival_line - 1
        next_states = []
        for i in (starting_line, 1):
            for j in range(3):
                if state[i][j] == colour and state[i + direction][j] == State.free:
                    self.extend_states(next_states, state, i, j, i + direction, j, colour)
            for j in range(2):
                if state[i][j] == colour and state[i + direction][j + 1] == 1 - colour:
                    self.extend_states(next_states, state, i, j, i + direction, j + 1, colour)
            for j in range(1, 3):
                if state[i][j] == colour and state[i + direction][j - 1] == 1 - colour:
                    self.extend_states(next_states, state, i, j, i + direction, j - 1, colour)
        return next_states

    def extend_states(self, next_states, state, i1, j1, i2, j2, color):
        next_state = deepcopy(state)
        next_state[i1][j1] = State.free
        next_state[i2][j2] = color
        next_states.append(next_state)

    def determine_winning_strategy(self, tree):
        if not tree.next_states:
            tree.expected_outcome = State.on_track_to_win
        else:
            for subtree in tree.next_states:
                self.determine_winning_strategy(subtree)
            if all(subtree.expected_outcome == State.on_track_to_lose for subtree in tree.next_states):
                tree.expected_outcome = State.on_track_to_win

    def identify_lucky_wins(self, tree):
        if not tree.next_states:
            return
        if tree.expected_outcome != State.on_track_to_win:
            for subtree in tree.next_states:
                for subsubtree in subtree.next_states:
                    if subsubtree.expected_outcome == State.on_track_to_win:
                        subsubtree.expected_outcome = State.on_track_for_lucky_win
        for subtree in tree.next_states:
            for subsubtree in subtree.next_states:
                self.identify_lucky_wins(subsubtree)


class DisplayedSearchTree(tk.Frame):
    def __init__(self, tree):
        tk.Frame.__init__(self, pady = 20)
        self.tree = tree
        self.displayed_tree = tk.Canvas(self, width = 9 * State.width, height = 20 * State.width)
        self.displayed_tree.grid()
        scrollbar = tk.Scrollbar(self, orient = tk.VERTICAL, command = self.displayed_tree.yview)
        self.displayed_tree.config(yscrollcommand = scrollbar.set)
        scrollbar.grid(row = 0, column = 1, sticky = tk.NS)
        self.displayed_tree.bind('<1>', lambda event, expand = True:
                                                         self.expand_or_collapse_tree(event, expand)
                                )
        self.displayed_tree.bind('<Control-1>', lambda event, expand = False:
                                                         self.expand_or_collapse_tree(event, expand)
                                )
        self.display_state(0, self.tree)

    def display_search_tree(self, tree):
        if tree.displayed:
            self.display_state(self.current_line, tree)
            self.current_line += 1
            for subtree in tree.next_states:
                self.display_search_tree(subtree)

    def display_state(self, line, tree):
        tree.display_state(self.displayed_tree, line)

    def expand_or_collapse_tree(self, event, expand):
        states = [self.tree]
        found_state = None
        while states:
            state = states.pop()
            if state.displayed and\
                         state.x < self.displayed_tree.canvasx(event.x) < state.x + State.width and\
                             state.y < self.displayed_tree.canvasy(event.y) < state.y + State.width:
                found_state = state
                break
            states.extend(state.next_states)
        if found_state:
            if expand:
                for subtree in found_state.next_states:
                    subtree.displayed = True
            else:
                for subtree in found_state.next_states:
                    self.cancel_display(subtree)
            self.displayed_tree.delete(tk.ALL)
            height = self.number_of_states_to_display(self.tree)
            self.displayed_tree.config(scrollregion = (0, 0, 9 * State.width,
                                                                         (height + 1) * State.width)
                                      )
            self.current_line = 0
            self.display_search_tree(self.tree)

    def number_of_states_to_display(self, tree):
        if tree.displayed:
            return 1 + sum(self.number_of_states_to_display(subtree) for subtree in tree.next_states
                          )
        return 0

    def cancel_display(self, tree):
        if tree.displayed:
            tree.displayed = False
            for subtree in tree.next_states:
                self.cancel_display(subtree)


class Game:
    def __init__(self, search_tree):
        self.search_tree = deepcopy(search_tree)

    def learn(self, displayed_games = None, game_nb = None):
        return self.play(self.search_tree, State.red, displayed_games, game_nb)

    def play(self, current_state, depth, displayed_games, game_nb):
        # Red's turn to play...
        if depth % 2:
            # 1. ... It can't.
            if not current_state.next_states:
                return State.black
            # 2. ... It can.
            next_state = self.pick_next_state(current_state, depth, displayed_games, game_nb)
            # Then it will be Black's turn to play....
            # 1. ... It won't be able to.
            # Then it won't give Red a chance again to reach current_state and win.
            if not next_state.next_states:
                for tree in self.search_tree.next_states:
                    self.remove_state_from_possible_states(tree, current_state)
                return State.red
            # 2. ... It will be able to.
            return self.play(next_state, depth + 1, displayed_games, game_nb)
        # Black's turn to play.
        next_state = self.pick_next_state(current_state, depth, displayed_games, game_nb)
        return self.play(next_state, depth + 1, displayed_games, game_nb)

    def pick_next_state(self, current_state, depth, displayed_games, game_nb):
        next_state = current_state.next_states[randrange(len(current_state.next_states))]
        next_state.depth = depth
        if displayed_games:
            next_state.display_state(displayed_games, game_nb)
        return next_state

    def remove_state_from_possible_states(self, tree, current_state):
        for subtree in tree.next_states:
            if subtree.code == current_state.code:
                tree.next_states.remove(subtree)
                break
        for subtree in tree.next_states:
            for subsubtree in subtree.next_states:
                self.remove_state_from_possible_states(subsubtree, current_state)

    def prune(self, tree):
        # If Red gets a chance to win at a given round...
        if any(subtree.expected_outcome != State.on_track_to_lose for subtree in tree.next_states):
            # ... it makes sure it doesn't play foolishly then.
            for subtree in tree.next_states:
                if subtree.expected_outcome == State.on_track_to_lose:
                    tree.next_states.remove(subtree)
        for subtree in tree.next_states:
            for subsubtree in subtree.next_states:
                self.prune(subsubtree)

    def well_pruned(self, tree):
        if tree.expected_outcome != State.on_track_to_win or\
            any(not self.well_pruned(subsubtree) for subtree in tree.next_states
                                                               for subsubtree in subtree.next_states
               ):
            return False
        return True


class SimulationBoard(tk.Frame):
    def __init__(self, search_tree):
        tk.Frame.__init__(self, padx = 20, pady = 20)
        self.search_tree = search_tree
        opponent_button = tk.Menubutton(self, text = 'Opponent', pady = 20)
        opponent_button.grid()
        players = tk.Menu(opponent_button)
        players.add_command(label = 'Random player', command = lambda random_player = True:
                                                                               self.learn(random_player))
        players.add_command(label = 'Good player', command = lambda random_player = False:
                                                                               self.learn(random_player))
        opponent_button.config(menu = players)
        self.displayed_games = tk.Canvas(self, width = 9 * State.width, height = 20 * State.width)
        self.displayed_games.grid()
        self.displayed_wins = tk.Canvas(self, width = 250, height = 500)
        self.displayed_wins.grid(row = 1, column = 2)

    def learn(self, random_player):
        black_wins = [None] * 100
        self.displayed_games.delete(tk.ALL)
        self.game = Game(self.search_tree)
        if not random_player:
            self.game.prune(self.game.search_tree)
        learning_over = False
        for i in range(19):
            black_wins[i] = self.game.learn(self.displayed_games, i)
            if not learning_over and self.game.well_pruned(self.game.search_tree):
                learning_over = i + 1
        for i in range(19, 100):
            black_wins[i] = self.game.learn()
            if not learning_over and self.game.well_pruned(self.game.search_tree):
                learning_over = i + 1
        self.displayed_wins.delete(tk.ALL)
        self.displayed_wins.create_line(5, 250, 205, 250, fill = 'yellow')
        y = 0
        for x in range(100):
            if black_wins[x] == State.black:
                self.displayed_wins.create_line(2 * x + 5, y + 250, 2 * x + 7, y + 248)
                y -= 2
            else:
                self.displayed_wins.create_line(2 * x + 5, y + 250, 2 * x + 7, y + 252)
                y += 2
        if random_player:
            self.displayed_wins.create_text(100, 17,
                                                 text = 'Results with random player\nover 100 games'
                                           )
        else:
            self.displayed_wins.create_text(100, 17,
                                                   text = 'Results with good player\nover 100 games'
                                           )
        if learning_over:
            self.displayed_wins.create_text(125, 445,
                                       text = f'Learning was completed\nafter {learning_over} games'
                                           )
        else:
            for i in range(100, 1000):
                self.game.learn()
                if self.game.well_pruned(self.game.search_tree):
                    self.displayed_wins.create_text(125, 445,
                                                      text = f'No more to learn after {i + 1} games'
                                                   )
                    learning_over = True
                    break
            if not learning_over:
                self.displayed_wins.create_text(125, 445,
                                                      text = '1000 games over, and more to learn...'
                                               )


if __name__ == '__main__':
    WinningStrategy().mainloop()
