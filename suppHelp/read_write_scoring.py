'''
This code will read and then write a new copy of
a scoring file from HW4 in CS342.
'''

import sys


def print_file(filename):
    '''
    This function just prints to the screen all contents within a file.
    Input: filename (String) - the name of the file to print.
    '''
    file = open(filename, 'r') # 'r' says we are reading the file

    print("Printing contents of following file:",filename)
    for line in file: # this is an easy way to iterate through a file
        line = line.rstrip() # all lines have newline character at the end.
        print(line)
    file.close() #always close the file after opening it

    print("\n\n\n") #print a few lines of white space


def read_file(filename):
    '''
    This function takes in a filename and returns a tuple
    containing the four different scoring parameters.
    Input: filename (string) - the name of the file to open.
    Return: scores (tuple of ints) - this tuple of length 4
            contains the following values in the following order:
            match score, mismatch score, gap-extend, gap-open
    '''
    file = open(filename, 'r') # 'r' says we are reading the file

    file.readline() #skip past header line

    line = file.readline() #reads next line, returns a string.
    line = line.rstrip() #remove all white space, return characters, etc
                         #on right hand side of string.

    file.close() #done with file, so close it

    vals = line.split("\t") #turn string into list of items originally
                            #separated by tabs

    scores = tuple(vals) #convert from list (mutable) to tuple (immutable)

    return scores

def write_file(scores, filename):
    '''
    This function takes in a tuple of scores and a filename
    and saves those scores to file as a new scoring file.
    Input: scores (tuple of ints) - a tuple of length 4 containing match,
            mismatch, gap-open and gap extend values.
           filename (String) - the name of the file to create.
    Return: None
    '''
    file = open (filename, 'w') #w indicates we are writing to a file
    header = "#match\tmismatch\tgap-extend\tgap-open\n" #need to add newline at end
    file.write(header) #This adds header to the file

    #Build string of tab separated scores.
    vals = "\t".join(scores) #creates a tab sep string of everything in scores.
    vals = vals + "\n" #add newline at end
    file.write(vals) #This adds vals to the file
    file.close() #You have to close a file in order for everything you wrote
                 #into it to show up


def main():
    '''
    Read in a scoring file provided as first command line parameter.
    Print scores to the screen.  Then write out the scores in a new file
    called new_scores.txt.
    '''
    num_args = len(sys.argv) - 1 #retrieve number of command line arguments
    if (num_args != 1):
        print("Program requires one command line argument.  A file name.")
        sys.exit(-1)

    filename = sys.argv[1] #first argument should be name of scoring file.
                           #this assumes file is in same directory as this code.

    #print contents of file to screen
    print_file(filename)

    #print all scores to the screen
    scores = read_file(filename)
    print("Scores contained in:",filename)
    for v in scores:
        print("Score:", v)

    new_file = 'new_scores.txt'
    write_file(scores, new_file)

# Runs the main function when the program is called from the command line
if __name__ == '__main__':
    main()
