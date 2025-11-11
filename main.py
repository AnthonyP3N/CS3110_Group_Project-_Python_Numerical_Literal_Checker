"""

CS 3110 Group Project: Recongize Python Numerical Literals
    Group Name: Showdown
    Group Members: Anthony Penaloza, Elvin Florencio


"""


class NFAmain:

    def __init__(self):
        
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
    
    def runfile(self, input_file: str, output_file: str) -> None:
                  try:
                      with open (input_file, 'r') as infile, open(output_file, 'w') as outfile:
                          for line_number, line in enumerate(infile, start=1):
                                input_str = line.strip()
                                if not input_str:
                                    continue
                                result = self.run(input_str)
                                status = "accepted" if result else "rejected"
                                outfile.write(f"Line {line_number}: '{input_str}' -> {status}\n")
                                print(f" Results written to '{output_file}'.")
                  except FileNotFoundError:
                      print(f" error in file {input_file}")
                  except Exception as e:
                      print(f"error in {e}")    

# --- Run the automaton here ---
if __name__ == "__main__":
    nfa = NFAmain()
    nfa.runfile("numbers.txt", "results.txt")

                   
                                      




