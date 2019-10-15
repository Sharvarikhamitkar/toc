class DFA:
    current_state = None;
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states;
        self.alphabet = alphabet;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None;
            return;
        self.current_state = self.transition_function[(self.current_state, input_value)];
        return;
    
    def in_accept_state(self):
        return self.current_state in accept_states;
    
    def go_to_initial_state(self):
        self.current_state = self.start_state;
        return;
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list:
            self.transition_to_state_with_input(inp);
            continue;
        return self.in_accept_state();
    pass;



states = {0, 1, 2, 3};
alphabet = {'1','0'};

tf = dict();
tf[(0, '1')] = 1;
tf[(0, '0')] = 2;
tf[(0, '1')] = 3;
tf[(0, '0')] = 0;
tf[(1, '1')] = 1;
tf[(1, '0')] = 2;
tf[(1, '1')] = 3;
tf[(1, '0')] = 0;
tf[(2, '1')] = 1;
tf[(2, '0')] = 2;
tf[(2, '1')] = 3;
tf[(2, '0')] = 0;
tf[(3, '1')] = 1;
tf[(3, '0')] = 2;
tf[(3, '1')] = 3;
tf[(3, '0')] = 0;
start_state = 0;
accept_states = {2, 3};

d = DFA(states, alphabet, tf, start_state, accept_states);

inp_program = input('Enter the string:');


print (d.run_with_input_list(inp_program));




