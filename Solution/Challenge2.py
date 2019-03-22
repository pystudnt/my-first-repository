# Python for Network Engineers Challenge  Lab #2 Solution 
# Revision May 22 2018

# The comments starting at line 10 describe the breaks.

#Copyright (C) 2013 Matt Oswalt (http://keepingitclassless.net/)
#Obviously humorous and meant to be taken as such.

#<<<<<<< HEAD
class CCIE:
    '''A class to describe a CCIE-certified engineer'''
# def wrongly spelled out as definition in the following line
    def __init__(self):
        self.name = ''
        self.salary = ''
        self.iq = ''
        self.homeless = True
# indenting broken in the following line
    def setName(self, name=''):
        self.name = name


thisCCIE = CCIE()
thisCCIE.setName(raw_input('Please enter your name.'))

answer = raw_input("Can you use a GUI? (yes/no/huh)")

# Only one = in the following line
if answer == 'no':
# Single and double quotes used in the following line
    print "That's awkward."
    thisCCIE.homeless = True
# elif incorrectly changed to else
elif answer == 'yes':
    print "Congratulations! You're a networking expert!"
    thisCCIE.salary = 1000000000
    thisCCIE.iq = 42
# quote removed after following line
elif answer == "hello?":
    print "I see that you are in management. Go fire some CCIEs or something."
#=======
# import spelled wrong as imported
import webbrowser

answer = raw_input("Can you use a GUI? (yes/no/huh/hello)")

if answer == 'no':
	webbrowser.open_new('http://www.opendaylight.org/')
elif answer == 'yes':
	print "Congratulations! You're a networking expert!"
elif answer == "hello":
	print "I see that you are in management. Go fire some CCIEs or something."
#>>>>>>> a2cf24d6c37bf7143e5e2766a0470322ca56bb99
# colon removed after following line
elif answer == "huh":
    print "What's a goooey ?"
    thisCCIE.homeless = True

