# FILE NAME - grade_converter.py

# NAME: Nicholas Sheppard
# DATE: 09/30/2025
# BRIEF DESCRIPTION:  This program will convert a student's grade percentage to a grade letter.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    grade_converter()

def grade_converter():
    print('===== Grade Converter =====')

    percent = int(input('Enter a numerical grade (1-100): '))

    if percent > 100:
        print('A+')
    elif percent >= 90:
        print('A')
    elif percent >= 80:
        print('B')
    elif percent >= 70:
        print('C')
    elif percent >= 65:
        print('D')
    else:
        print('F')

main()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

Make sure you don't reverse the 'if elseif else' statements. Otherwise it will always
give an unexpected result. For instance, if you calculate the letter grade of D first, it'll
check to see if the number is >= 65. The issue is that it will produce a D for ALL numbers over
65, then stop executing the code.





'''
