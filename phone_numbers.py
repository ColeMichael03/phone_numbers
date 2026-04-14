from argparse import ArgumentParser
import re
import sys


LETTER_TO_NUMBER = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'Q': '7',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9',
    'Z': '9'
}


# Replace this comment with your implementation of the PhoneNumber class and
# the `read_numbers()` function.
class PhoneNumber:
    """
    """
    def __init__(self, p_num):
        
        #error handling
        if not isinstance(p_num, (str, int)):
            raise TypeError("INPUT MUST BE INT OR STR")
        
        #make phonenumber a str of capital letters
        p_num = str(p_num).upper()
        
        #take everything that matches pattern, replace with digit from dict
        digits = re.sub(r"[A-Z]", 
                        lambda m: LETTER_TO_NUMBER[m.group()], p_num)
        
        #remove everything that is not a digit
        digits = re.sub(r"\D", "", digits)
        print(digits)
        self.number = digits
    
    
def read_numbers(path):
    
    contact_list = []
    pattern = r"""
            (?xm)
            #everything before the tab
            ^
            (?P<name>[^\t]*)
            \t
            #the entire number
            (?P<number>.*)
            """
            
    with open(path, mode='r', encoding="UTF-8") as f:
        for data in f:  
            data = data.strip()
            match = re.match(pattern, data)
            
            if match: 
                name = match.group('name')
                number = match.group('number')
                
            
            
            
     
    

def main(path):
    """Read data from path and print results.
    
    Args:
        path (str): path to a text file. Each line in the file should consist of
            a name, a tab character, and a phone number.
    
    Side effects:
        Writes to stdout.
    """
    for name, number in read_numbers(path):
        print(f"{number}\t{name}")


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file where
    each line consists of a name, a tab character, and a phone number.
    
    Args:
        arglist (list of str): a list of command-line arguments to parse.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file of names and numbers")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
