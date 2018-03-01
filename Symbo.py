"""
format Symbolab to a working format for copy and paste.

Here is an example to use:
343\left(\frac{1}{7}x^2\sin \left(7x\right)-\frac{2}{7}\left(-\frac{1}{7}x\cos \left(7x\right)+\frac{1}{49}\sin \left(7x\right)\right)\right)+C

Codes are simple enough:
\left( means (
\right) is )
\frac{} {} needs to change to {} / {}
"""
def QuickClean(line):
    line = line.replace("\\", '')
    line = line.replace('left(', '(')
    line = line.replace('right)', ')')
    line = line.replace('sin ', 'sin')
    line = line.replace('cos ', 'cos')
    return line

def FractalClean(line):
    while 'frac' in line:
        loc = line.index('frac')
        brL = line.index('{', loc+5)
        brR = line.index('}', brL)
        n1 = line[loc+5:brL-1]
        n2 = line[brL+1:brR]
        line = line[:loc] + n1 + '/' + n2 + line[brR+1:]
    return line


line = input("Enter the symbolab output: ")
line = QuickClean(line) #Call function to fix left and right brackets, remove \ chars, and fix sin/cos
line = FractalClean(line) #Fix division


print("""
Here is the formatted equation:
{}""".format(line))
input()
