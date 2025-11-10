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


    def transition(self, ch);

        state = self.current_state
        
            if state == "START":
                # TODO: handle '0' and '1-9' transitions, normal nfa/dfa start state
                pass 

            elif state == "ZERO":
                # TODO: stop accepting digits after '0'
                pass

            elif state == "DIGIT":
                # TODO: handle digits and underscores
                pass

            elif state == "UNDERSCORE":
                # TODO: acts as a space bar move onto next digit 
                pass 

            else: 
                # TODO: acts as a dead state, ends reading here
                self.current_state = "DEAD"

    def run(self, s):
        self.reset()

            for ch in s:
                self.transition(ch)
                if self.current_state == "DEAD":
                    break 

            # Accept string if it ends in one of the valid accept states
            return self.current_state in self.accept_states 




