# Python for Network Engineers Challenge Lab #1 Solution
# Revision May 22 2018

# Shebang for Linux:
#!/usr/bin/env python
# Define the first function devices:
def devices():
	routers = ['router1', 'router2', 'router3']
	print routers
# Define the second function security:
def security():
	credentials = {'router1':'passw0rd1', 'router2': 'passw0rd1', 'router3': 'passw0rd1'}
	print credentials
#  Define the third function combined that uses the first two functions:
def combined():
	devices()
	security()
# Define the entry point:
if __name__ == "__main__":
	print "The routers are:"
	devices()

	print "The credentials are:"
	security()

	print "All data is"
	combined()


