# Written by Eric Martin for COMP9021


'''
A Prolog interpreter for pure definite logic programs.
Illustrates the use of a deque for depth-first search for a solution.

'''


from collections import deque

import term


class Clause:
    class ClauseError(Exception):
        def __init__(self, message):
            self.message = message

    def __init__(self, clause):
        if clause[-1] != '.':
            raise Clause.ClauseError(f'{str(clause)} does not end in a full stop.')
        clause = clause[: -1].split(':-')
        if len(clause) == 2 and clause[0] and clause[1]:
            # Make a term out of body to easily check its syntactic validity.
            head, body = clause[0], ''.join(('x(', clause[1], ')'))
            if not term.is_syntactically_valid(body):
                raise Clause.ClauseError(f'{str(clause[1])} is syntactically invalid.') 
            body = term.parse(body)[1: ]
            # Would pass the previous test if some atoms were incorrectly interpreted as variables.
            if any(not atom[0].islower() for atom in body):
                raise Clause.ClauseError(f'{str(clause[1])} is syntactically invalid.') 
        elif len(clause) == 1 and clause[0]:
            head, body = clause[0], []
        else:
            raise Clause.ClauseError(f'{str(clause)} is neither a fact nor a rule.')
        if not term.is_syntactically_valid(head):
            raise Clause.ClauseError(f'{str(head)} is syntactically invalid.')
        self.head = term.nicely_formatted(head)
        self.body = body
        self.variables = term.variables(head) |\
                                              {var for atom in body for var in term.variables(atom)}


class LogicProgram:
    class QueryError(Exception):
        def __init__(self, message):
            self.message = message

    def __init__(self, filename):
        self.program = []
        with open(filename) as file:
             for clause in file:
                clause = clause.strip()
                if not clause or clause.startswith('%'):
                    continue
                self.program.append(Clause(clause))

    def solve(self, *query_goals):
        for query_goal in query_goals:
            if not term.is_syntactically_valid(query_goal) or not query_goal[0].islower():
                raise LogicProgram.QueryError(f'{str(query_goal)} is syntactically invalid.') 
        query_variables = {var for atom in query_goals for var in term.variables(atom)}
        # A list of pairs consisting of:
        # - a list of goals to be solved, and
        # - the substitution to apply to the variables that occur in the query
        #   as determined by the unifications computed so far.
        goals_solution_list = deque([(deque(query_goals), {var: var for var in query_variables})])
        while goals_solution_list:
            goals, solution = goals_solution_list.popleft()
            if not goals:
                yield solution
                continue
            reserved_variables = query_variables |\
                                             {var for atom in goals for var in term.variables(atom)}
            goal = goals.popleft()
            next_goals_solution_list = deque()
            for clause in self.program:
                variable_renaming = term.fresh_variables(clause.variables, reserved_variables)
                head = term.substitute(clause.head, variable_renaming)
                mgu = term.unify(goal, head)
                if mgu is not None:
                    new_goals = deque(term.substitute(term.substitute(atom, variable_renaming), mgu)
                                                                             for atom in clause.body
                                     )
                    new_goals.extend(term.substitute(goal, mgu) for goal in goals)
                    new_solution = {var: term.substitute(solution[var], mgu) for var in solution}
                    next_goals_solution_list.appendleft((new_goals, new_solution))
            goals_solution_list.extendleft(next_goals_solution_list)
 

if __name__ == '__main__':
    LP = LogicProgram('prolog_ex.pl')
    print('A query for prolog_ex.pl')
    print('  Solutions to relation(f(f(f(g(f(a))))), f(f(g(g(a)))), X):')
    for solution in LP.solve('relation(f(f(f(g(f(a))))), f(f(g(g(a)))), X)'):
        print('   ', solution)
    print()
    
    LP = LogicProgram('prolog_ex_1.pl')
    print('A few queries for prolog_ex_1.pl')
    print('  Solutions to sisterof(victoria, harry):')
    for solution in LP.solve('sisterof(victoria, harry)'):
        print('   ', solution)
    print('  Solutions to sisterof(alice, harry):')
    for solution in LP.solve('sisterof(alice, harry)'):
        print('   ', solution)
    print('  Solutions to sisterof(alice, X):')
    for solution in LP.solve('sisterof(alice, X)'):
        print('   ', solution)
    print('  Solutions to sisterof(alice, X), loves(X, wine):')
    for solution in LP.solve('sisterof(alice, X)', 'loves(X, wine)'):
        print('   ', solution)
    print()
    
    LP = LogicProgram('prolog_ex_2.pl')
    print('A few queries for prolog_ex_2.pl')
    print('  Solutions to father(X, jack):')
    for solution in LP.solve('father(X, jack)'):
        print('   ', solution)
    print('  Solutions to grandparent(john, X):')
    for solution in LP.solve('grandparent(john, X)'):
        print('   ', solution)
    print()
    LP = LogicProgram('prolog_ex_3.pl')
    print('A query for prolog_ex_3pl')
    print('  Solutions to loves(Who, What):')
    for solution in LP.solve('loves(Who, What)'):
        print('   ', solution)
    print()
    
    LP = LogicProgram('prolog_ex_4.pl')
    print('A few queries for prolog_ex_4.pl')
    print('  Solutions to conflict(R1, R2, b):')
    for solution in LP.solve('conflict(R1, R2, b)'):
        print('   ', solution)
    print('  Solutions to conflict(R1, R2, b), color(R1, C, b):')
    for solution in LP.solve('conflict(R1, R2, b)', 'color(R1, C, b)'):
        print('   ', solution)
