from Bio import SeqIO
import sys

"""
    This script will take in a variable number of command line arguments
    and will print the the total number of arguments along with each
    one on a different line.

    NOTE: This script is written for python 2.7.

    Here is an example run of the program and the output it will produce
    
    $ python echo.py 1 2 3
    Total number of arguments:  3
    Argument  0  :  1
    Argument  1  :  2
    Argument  2  :  3
 """

#This function uses a dynamic programming algorithm to calculate the optimal
#alignment score between two strings using gap, mismatch, and match scores
#Parameters: s1 and s2 are two strings (do not have to be the same length)
#            gap, mismatch, and match are all integers, gap and mismatch are
#            typically negative values, match is typically a positive value
#Returns: the optimal global alignment score, as we as a 2-D list of hints
#         to help determine the actual alignment
def NeedlemanWunsch_global(s1, s2, gap_open, gap_extend, mismatch, match):
    m = len(s1)
    n = len(s2)
    max_all_score = 0

    #Initialize 2 2-d lists of size (m+1)rows * (n+1)columns
    matrix = [[0 for i in range(n+1)] for j in range(m+1)]  #scores
    hints = [[0 for i in range(n+1)] for j in range(m+1)]   #backtracking hints
    
    #Below is the pseudocode for computing the alignment score table (matrix)
    #Once you get this working, add in code to keep track of the hints
    #You'll see in get_alignment, that it is expecting you to present hints as:
    # \\ (diagonal), | (from above), - (from left)

    matrix[0][0] = 0
    for i in range(1, m+1):
        gap = (gap_open + gap_extend) if i == 1 else gap_extend
        matrix[i][0] = matrix[i-1][0] + gap
        hints[i][0] = "| "

    for j in range(1, n+1):
        gap = (gap_open + gap_extend) if j == 1 else gap_extend
        matrix[0][j] = matrix[0][j-1] + gap
        hints[0][j] = "- "

    is_prev_path_a_gap = False
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                score1 = matrix[i-1][j-1] + match
            else:
                score1 = matrix[i-1][j-1] + mismatch
            
            gap = gap_extend if is_prev_path_a_gap else (gap_open + gap_extend)

            score2 = matrix[i][j-1] + gap
            score3 = matrix[i-1][j] + gap
            
            
            maxScore = max(score1, score2, score3) 


            # If the chosen path is not running from a diagonal path, reset the prev_path_is_gap value 
            # so we know the next gap would be a gap open and not gap extend
            is_prev_path_a_gap = True if (maxScore != score1) else False

            matrix[i][j] = maxScore

            if maxScore == score1:
                hints[i][j] = "\\"
            elif maxScore == score2:
                hints[i][j] = "- "
            else:
                hints[i][j] = "| "

    print()
    # for row in matrix:
    #     print(row)
    # print()
    # for row in hints:
    #     print(row)
    # print()
    return matrix[m][n], hints

def NeedlemanWunsch_local(s1, s2, gap_open, gap_extend, mismatch, match):
    m = len(s1) 
    n = len(s2) 
    max_all_score = 0
    max_all_score_row = 0
    max_all_score_col = 0

    #Initialize 2 2-d lists of size (m+1)rows * (n+1)columns
    matrix = [[0 for i in range(n+1)] for j in range(m+1)]  #scores
    hints = [[0 for i in range(n+1)] for j in range(m+1)]   #backtracking hints
    
    #Below is the pseudocode for computing the alignment score table (matrix)
    #Once you get this working, add in code to keep track of the hints
    #You'll see in get_alignment, that it is expecting you to present hints as:
    # \\ (diagonal), | (from above), - (from left)


    matrix[0][0] = 0
    for i in range(1, m+1):
        matrix[i][0] = 0
        hints[i][0] = "| "

    for j in range(1, n+1):
        matrix[0][j] = 0
        hints[0][j] = "- "


    is_prev_path_a_gap = False
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                score1 = matrix[i-1][j-1] + match
            else:
                score1 = matrix[i-1][j-1] + mismatch
            
            gap = gap_extend if is_prev_path_a_gap else (gap_open + gap_extend)

            score2 = matrix[i][j-1] + gap
            score3 = matrix[i-1][j] + gap
            
            
            maxScore = max(score1, score2, score3, 0)


            # If the chosen path is not running from a diagonal path, reset the prev_path_is_gap value 
            # so we know the next gap would be a gap open and not gap extend
            is_prev_path_a_gap = False if (maxScore == 0 or maxScore == score1) else True

            matrix[i][j] = maxScore
            if matrix[i][j] > max_all_score:
                max_all_score = matrix[i][j]
                max_all_score_row = i
                max_all_score_col = j

            if maxScore == score1:
                hints[i][j] = "\\"
            elif maxScore == score2:
                hints[i][j] = "- "
            else:
                hints[i][j] = "| "

    # print()
    # for row in matrix:
    #     print(row)
    # print()
    # for row in hints:
    #     print(row)
    # print()
    print(type(matrix))
    # return_matrix = matrix[:(max_all_score_row + 1)][:, :(max_all_score_col + 1)]
    return_matrix = [row[:max_all_score_col+1] for row in matrix[:max_all_score_row+1]]

    return matrix[m][n], hints, return_matrix, max_all_score, max_all_score_row, max_all_score_col

#This function takes in 2 strings and a 2-D list of backtracking hints
#and returns the global alignment of the strings
#Parameters: A and B are two strings (do not have to be the same length)
#            hints is a 2-D lists containing \\, -, or | symbols
#Returns: two strings describing the global alignment between A and B

def get_alignment_global(A, B, hints):
    i = len(A)
    j = len(B)
    align1 = ''
    align2 = ''
    
    while i > 0 or j > 0:
        print("i: ", i, "j: ", j)
        
        if hints[i][j] == '\\':
            align1 = A[i-1] + align1
            align2 = B[j-1] + align2
            i -= 1
            j -= 1        

        elif hints[i][j] == '|':

            if i == 0:
                align1 = A[i-1] + align1
                align2 = "-" + align2

            else:
                align1 = A[i-1] + align1
                align2 = "-" + align2
                i -= 1
        else:
            if j == 0:
                align1 = "-" + align1
                align2 = B[j-1] + align2
            else:
                align1 = "-" + align1
                align2 = B[j-1] + align2
                j -= 1

    print(i, j)
    return align1, align2


def get_alignment_local(A, B, hints, opt_row, opt_col, opt_matrix):
    A = A[0:opt_row]
    B = B[0:opt_col]
    i = len(A) 
    j = len(B) 
    align1 = ''
    align2 = ''
    while i > 0 or j > 0:
        print("i: ", i, "j: ", j)
        print(opt_matrix[i][j])
        if opt_matrix[i][j] == 0:
            break
        elif hints[i][j] == '\\':
            align1 = A[i-1] + align1
            i -= 1
            align2 = B[j-1] + align2
            j -= 1
        elif hints[i][j] == '|':
            align1 = A[i-1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = B[j-1] + align2
            j -= 1


    return align1, align2

def read_single_file_fast(filename):
    for seq_record in SeqIO.parse(filename, "fasta"):
        sequence = str(seq_record.seq)
    return sequence.upper()

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

    vals = line.split() #turn string into list of items originally
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



num_params = len(sys.argv)-1

print("Total number of arguments:",num_params)

for v in range(num_params):
    print ("Argument",v,":",sys.argv[v+1])

scoring = read_file(sys.argv[1])
s1 = read_single_file_fast(sys.argv[2])
s2 = read_single_file_fast(sys.argv[3])
# print(s1)
# print(s2)
choice = str(sys.argv[4])
# s1 = "AAAG"
# s2 = "AAG"
scoring = tuple(map(int, scoring))
print("Scoring tuple", scoring)

# match_score = scoring[0]
# mismatch_score = scoring[1]
# gap_extend = scoring[2]
# gap_open = scoring[3]

gap_open = -3
gap_extend = -1
mismatch_score = -1
match_score = 1
# choice = "global"





if choice == "global": 
    print(s1)
    print(s2)
    score, hints  = NeedlemanWunsch_global(s1, s2, gap_open, gap_extend,  mismatch_score, match_score)
    print("Gloval alignment score is", score)
    align1, align2 = get_alignment_global(s1, s2, hints)
    print()
    print(align1)
    print(align2)
else:
    score, hints, opt_matrix,opt_score_local, opt_row, opt_col = NeedlemanWunsch_local(s1, s2, gap_open, gap_extend,  mismatch_score, match_score)

    print("opt row: ", opt_row)
    print("opt col", opt_col)
    print("Local alignment score is", opt_score_local)
    align1, align2 = get_alignment_local(s1, s2, hints, opt_row, opt_col, opt_matrix)
    print()
    print(align1)
    print()
    print(align2)