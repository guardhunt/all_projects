######################################################################
# Author: Roland Junior Toussaint
#
# Lab: L2
# Purpose: This program is to practice using and calling functions,
# breaking a project into small steps, and practice using strings. This
# takes a DNA sequence given by the user and gives you the otherside of
# of the DNA string, the number of times certain letter appear, replaces
# all T with U, and then gives the RNA sequence for given DNA sequence.
#
######################################################################
# Acknowledgements:

#   Modified from code written by Dr. Jan Pearce
#   Original lab specifications modified from:
#   http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
######################################################################

import sys
import doctest

def testit(did_pass):
    """ Print the result of a test. """
    # This function works correctly
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def all_nucleotide(sequence):
    '''checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T'''
    for i in sequence:  # This steps individualy through the letters
        if i not in 'ACGT': # Looks for anything that is not ACG or T
            return 'That is an invalid DNA sequence' # Retruns this string
    return sequence # Returns the string if it is valid

def num_times(sequence, nucleotide):
    '''Returns count of how many times nucleotide is found in sequence.'''
    count = 0
    for i in sequence:  # Steps through individual letter of string
        if i == nucleotide: # If i equals letter then it adds 1 to the count
            count += 1
    return count # returns times the nucleotide was encountered

def complement_strand(sequence):
    '''returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs.'''
    new_string = "" # creates a new string called new_string
    for i in sequence: # This steps individualy through the letters
        if i == 'A': # if i equals A adds T to new string
            new_string += 'T'
        if i == 'T': # if i equals T adds A to new string
            new_string += 'A'
        if i == 'C': # if i equals C adds G to new string
            new_string += 'G'
        if i == 'G': # if i equals G adds C to new string
            new_string += 'C'
    return new_string # retruns the new string

def mRNA(sequence):
    '''using the return from secondStrand(sequence) with each occurrence of the
    nucleotide T replaced with the nucleotide U'''
    fixed_string = "" # Creates new string called fixed_string
    for i in sequence:# Steps through the sting
        if i == 'T': # if letter or i equals T it replaces with U
            fixed_string += 'U'
        else: # if letter not T put it in new string
            fixed_string += i
    return fixed_string # returns the fixed string without T

def amino_acid_translation(threecharseq):
    '''expects a three character string as a parameter and returns
    the corresponding single character AminoAcid'''
    # This funciton is already completed correctly
    translator = { "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
                        "AGA":"R", "AGG":"R", "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
                        "GAC":"D", "GAU":"D",
                        "AAC":"N", "AAU":"N",
                        "UGC":"C", "UGU":"C",
                        "GAA":"E", "GAG":"E",
                        "CAA":"Q", "CAG":"Q",
                        "GGA":"G", "GGC":"G", "GGU":"G", "GGG":"G",
                        "CAC":"H", "CAU":"H",
                        "AUA":"I", "AUC":"I", "AUU":"I",
                        "UUA":"L", "UUG":"L", "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L",
                        "AAA":"K", "AAG":"K",
                        "AUG":"M",
                        "UUC":"F", "UUU":"F",
                        "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
                        "AGC":"S", "AGU":"S", "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
                        "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T",
                        "UGG":"W",
                        "UAC":"Y", "UAU":"Y",
                        "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
                        "UAA":"*", "UAG":"*", "UGA":"*" }
    if threecharseq in translator.keys():
        return translator[threecharseq] # Returns the RNA sequence letter
    else:
        return "?" # Returns ? if letter incorrect

def amino_acid(sequence):
    '''uses mRNA(sequence) and divides it into substrings of length 3,
    translates each nucleotide triple into it's corresponding Amino Acid
    using aminoAcidTranslation(threecharseq)'''
    first_letter = 0 # Sets the x in [x,z] to zero
    old_number = 3 # Sets the z in [x,z] to 3
    amino_acid = "" # Starts a new string
    length = len(sequence) // 3 # Calculates length of string and shrinks it to a number divisible by 3

    for i in range(length): # Steps through string divisible by 3
        amino_acid += amino_acid_translation(sequence[first_letter:old_number]) # calls function and takes the return and puts it in new sting
        first_letter += 3 # Sets the x in [x,z] to x+3
        old_number += 3 # Sets the z in [x,z] to z+3
    return amino_acid # returns the new string of RNA
#-------------------------------------------------------------------------------
testit(all_nucleotide("CGTAGGCAT")==True)
testit(all_nucleotide("CGTAFLCAT")==False)

sequence = raw_input('Please input your DNA string') #asks for DNA sequence
print all_nucleotide(sequence) # Calls all nucleotide funtion
print ''
print num_times(sequence, 'C') # Calls num_times function and the string can be changed
print ''
print complement_strand(sequence) # Calls complete_strand function
print''
print mRNA(sequence) # Calls mRNA function
print ''
fixed_string = mRNA(sequence) # Sets the output of mRNA and sets it to fixed_string
print amino_acid(fixed_string)
# Be sure to change the filename of this file to your yourusernames-L2.py