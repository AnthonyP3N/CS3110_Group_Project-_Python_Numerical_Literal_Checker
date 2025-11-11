"""

CS 3110 Group Project: Recongize Python Numerical Literals
    Group Name: Showdown
    Group Members: Anthony Penaloza, 


"""


class NFAmain:

    def states(self):
        
        self.start_state = "START"
        self.accept_states= {"DIGIT" , "ZERO"}
        self.current_state = self.start_state


    def reset(self):

        self.current_state = self.start_state 


    def transition(self, ch):

        state = self.current_state
        
        # Start State Logic
        if state == "START":
                # Handles '0' and '1-9' transitions, normal nfa/dfa start state
                if ch == '0':
                    self.current_state = "ZERO"
                elif ch.isdigit():
                    self.current_state = "DIGIT"
                else:
                    self.current_state = "DEAD" 

        # Zero State Logic
        elif state == "ZERO":
                # Handles cases where digits/underscores follow zero, should be rejected
                    self.current_state = "DEAD"

        # Digit(s) State Logic
        elif state == "DIGIT":
                # Handles digits and underscores
                if ch.isdigit():
                    self.current_state = "DIGIT"
                elif ch == "_":
                    self.current_state = "UNDERSCORE"
                else:
                    self.current_state = "DEAD"

        # Underscore State Logic
        elif state == "UNDERSCORE":
                #  Handles cases of accept string if next ch is digit and reject if next ch is _ 
                if ch.isdigit():
                    self.current_state = "DIGIT"
                else:
                    self.current_state = "DEAD" 

        # Dead State Logic
        else: 
            # Acts as a dead state, ends reading here
            self.current_state = "DEAD"

    def run(self, s):
        self.reset()

        for ch in s:
                self.transition(ch)
                if self.current_state == "DEAD":
                    break 

        # Accept string if it ends in one of the valid accept states
        return self.current_state in self.accept_states 




