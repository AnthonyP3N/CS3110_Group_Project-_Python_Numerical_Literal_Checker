"""

CS 3110 Group Project: Recongize Python Numerical Literals
    Group Name: Showdown
    Group Members: Anthony Penaloza, Elvin Florencio


"""


class NFAmain:

    def __init__(self):
        
        self.start_state = "START"

        self.accept_states= {"DIGIT", "OCT_DIGIT", "HEXDIGIT", "WITH_INT", "FRACTION", "EXPONENT"}
        
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
                elif ch == ".":
                            self.current_state = "NO_INT"
                else:
                    self.current_state = "DEAD" 

        # Zero State Logic
        elif state == "ZERO":
                # Handles cases where digits/underscores follow zero, should be rejected
                if ch in ('x', 'X'):
                    self.current_state = "HEX_START"
                elif ch in ("o", "O"):
                    self.current_state = "OCT_START"
                elif ch in ("e", "E"):
                    self.current_state = "EXPONENT"
                elif ch == ".":
                    self.current_state = "WITH_INT"
                else:
                    self.current_state = "DEAD"

        # Digit(s) State Logic
        elif state == "DIGIT":
                # Handles digits and underscores
                if ch.isdigit():
                    self.current_state = "DIGIT"
                elif ch == "_":
                    self.current_state = "UNDERSCORE" 
                elif ch == ".":
                          self.current_state = "WITH_INT"
                elif ch in "eE":
                    self.current_state = "EXP_START"
                else:
                    self.current_state = "DEAD"

        # FRACTIONAL FLOAT 
        elif state == "NO_INT":
            if ch.isdigit():
                self.current_state = "FRACTION"
            else:
                self.current_state = "DEAD"

        elif state == "WITH_INT":
            if ch.isdigit():
                self.current_state = "FRACTION"
            elif ch in "eE":
                self.current_state = "EXP_START"
            else:
                self.current_state = "DEAD"

        elif state == "FRACTION":
            if ch.isdigit():
                self.current_state = "FRACTION"
            elif ch == "_":
                self.current_state = "UNDERSCORE_FRAC"
            elif ch in "eE":
                self.current_state = "EXP_START"
            else:
                self.current_state = "DEAD"

        elif state == "UNDERSCORE_FRAC":
            if ch.isdigit():
                self.current_state = "FRACTION"
            else:
                self.current_state = "DEAD"

        #EXPONENT STATE Logic
        elif state == "EXP_START":
            if ch in "+-":
                self.current_state = "EXP_SIGN"
            elif ch.isdigit():
                self.current_state = "EXPONENT"
            else:
                self.current_state = "DEAD"

        elif state == "EXP_SIGN":
            if ch.isdigit():
                self.current_state = "EXPONENT"
            else:
                self.current_state = "DEAD"

        elif state == "EXPONENT":
            if ch.isdigit():
                self.current_state = "EXPONENT"
            elif ch == "_":
                self.current_state = "UNDERSCORE_EXP"
            else:
                self.current_state = "DEAD"

        elif state == "UNDERSCORE_EXP":
            if ch.isdigit():
                self.current_state = "EXPONENT"
            else:
                self.current_state = "DEAD"


        # Hexinteger Start State Logic 
        elif state == "HEX_START":
                # UNDERSCOREHEX and HEXDIGIT are used so strings don't get overlapped into decinteger states
                if ch in 'abcdefABCDEF':
                     self.current_state = "HEXDIGIT"  
                elif ch.isdigit():
                     self.current_state = "HEXDIGIT"
                elif ch == "_":
                     self.current_state = "UNDERSCOREHEX"
                else:
                     self.current_state = "DEAD"
        
        # Hexdigit State Logic
        elif state == "HEXDIGIT":
                if ch in 'abcdefABCDEF':
                     self.current_state = "HEXDIGIT" 
                elif ch.isdigit():
                     self.current_state = "HEXDIGIT"
                elif ch == "_":
                     self.current_state = "UNDERSCOREHEX"
                else:
                     self.current_state = "DEAD"
                     

        # Underscore State Logic
        elif state == "UNDERSCORE":
                #  Handles cases of accept string if next ch is digit and reject if next ch is _ 
                if ch.isdigit():
                    self.current_state = "DIGIT"
                else:
                    self.current_state = "DEAD" 
        
        # Underscore State Logic (used for hexdigits)
        elif state == "UNDERSCOREHEX":
                #  Handles cases of accept string if next ch is digit or a-f/A-F and reject if next ch is _ or any other invaild hexdigit ch
                if ch.isdigit():
                    self.current_state = "HEXDIGIT"
                elif ch in 'abcdefABCDEF':
                    self.current_state = "HEXDIGIT"
                elif ch == "_":
                    self.current_state = "DEAD"       
            
        # Octinteger Start State Logic    
        elif state == "OCT_START":
            if ch in "01234567":
                self.current_state = "OCT_DIGIT"
            elif ch == '_':
                self.current_state = "OCT_UNDERSCORE"
            else:
                self.current_state = "DEAD"

        # Octdigit State Logic
        elif state == "OCT_DIGIT":
            if ch in "01234567":
                self.current_state = "OCT_DIGIT"
            elif ch == "_":
                self.current_state = "OCT_UNDERSCORE"
            else:
                self.current_state = "DEAD"

        # Underscore State Logic (used for octdigits)
        elif state == "OCT_UNDERSCORE":
            #  Handles cases of accept string if next ch is a digit 0-7 and reject if next ch is _ or any other invaild octdigit ch
            if ch in "01234567":
                self.current_state = "OCT_DIGIT"
            else:
                self.current_state = "DEAD"
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
                          outfile.write("NFA Actual results\n")
                          for line_number, line in enumerate(infile, start=1):
                                input_str = line.strip()
                                if not input_str:
                                    continue
                                test_string = line.split()[0]
                                result = self.run(test_string)
                                status = "accepted" if result else "rejected"
                                outfile.write(f"Line {line_number}: '{test_string}' -> {status}\n")
                                print(f" Results written to '{output_file}'.")
                  except FileNotFoundError:
                      print(f" error in file {input_file}")
                  except Exception as e:
                      print(f"error in {e}")    

def menu(nfa):
    while True:
        print("1. Test single string")
        print("2. Run input file")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            s = input("Enter string: ").strip()
            result = nfa.run(s)
            status = "ACCEPTED" if result else "REJECTED"
            print(f"\nResult: '{s}' -> {status}\n")
            break

        elif choice == "2":
            in_file = input("Enter input filename: ").strip()
            nfa.runfile(in_file, "out.txt")
            break

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid option — choose 1, 2, or 3.")

# --- Run the automaton here ---
if __name__ == "__main__":
    nfa = NFAmain()
    menu(nfa)

                   
                                      




