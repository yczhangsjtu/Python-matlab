################################################################################
"""
A Simple Python Implementation of Matlab

-------------------------------------------------------------------------------|
|         |                               |                                    |
|         |                               |                                    |
|    C    |                               |                                    |
|    O    |                               |                                    |
|    N    |                               |                                    |
|    T    |                               |                                    |
|    R    |                               |                                    |
|    O    |                               |                                    |
|    L    |                               |                                    |
|         |                               |                                    |
|    B    |        OUTPUT AREA            |        FIGURE SHOWN HERE           |
|    U    |                               |                                    |
|    T    |        (readonly textbox)     |        (canvas)                    |
|    T    |                               |                                    |
|    O    |                               |                                    |
|    N    |                               |                                    |
|    S    |                               |                                    |
|(buttons)|                               |                                    |
|(frame)  |                               |                                    |
|         |                               |                                    |
|         |                               |                                    |
-------------------------------------------------------------------------------|
"""
################################################################################
from __future__ import division
from Tkinter import *
import pylab
from numpy import *
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
from PIL import Image, ImageTk
import string
import re
################################################################################
####################### CONSTANTS ##############################################
################################################################################
#-------------------------------------------------------------------------------
# Information provided when first started
greeting = \
"""This is a simple python implementation of matlab.

"""
#-------------------------------------------------------------------------------
# Map matlab functions to python and numpy and pylab functions
funcmap = \
{\
    "disp":"printl",\
    "linspace":"linspace",\
    "logspace":"logspace",\
    "outer":"outer",\
    "ones":"ones",\
    "size":"size",\
    "abs":"abs",\
    "sin":"sin",\
    "cos":"cos",\
    "sqrt":"sqrt",\
    "log":"log",\
    "log2":"log2",\
    "log10":"log10",\
    "power":"power",\
    "arccos":"arccos",\
    "arcsin":"arcsin",\
    "arctanh":"arctanh",\
    "poly":"poly",\
    "roots":"roots",\
    "polyint":"polyint",\
    "polyder":"polyder",\
    "polyadd":"polyadd",\
    "polysub":"polysub",\
    "polymul":"polymul",\
    "polydiv":"polydiv",\
    "polyval":"polyval",\
    "poly1d":"poly1d",\
    "polyfit":"polyfit",\
    "array":"array",\
    "range":"range",\
    "arange":"arange",\
    "array2string":"array2string",\
    "set_printoptions":"set_printoptions",\
    "get_printoptions":"get_printoptions",\
    "equal":"equal",\
    "not_equal":"not_equal",\
    "greater_equal":"greater_equal",\
    "less_equal":"less_equal",\
    "greater":"greater",\
    "less":"less",\
    "str_len":"char.str_len",\
    "add":"add",\
    "multiply":"multiply",\
    "mod":"mod",\
    "capitalize":"char.capitalize",\
    "center":"char.center",\
    "count":"char.count",\
    "encode":"char.encode",\
    "decode":"char.decode",\
    "endswith":"char.endswith",\
    "expandtabs":"char.expandtabs",\
    "find":"char.find",\
    "index":"char.index",\
    "isalnum":"char.isalnum",\
    "isalpha":"char.isalpha",\
    "isdigit":"char.isdigit",\
    "islower":"char.islower",\
    "isspace":"char.isspace",\
    "istitle":"char.istitle",\
    "isupper":"char.isupper",\
    "join":"char.join",\
    "ljust":"char.ljust",\
    "lower":"char.lower",\
    "lstrip":"char.lstrip",\
    "spartition":"char.partition",\
    "replace":"char.replace",\
    "rfind":"char.rfind",\
    "rindex":"char.rindex",\
    "rjust":"char.rjust",\
    "rpartition":"char.rpartition",\
    "rsplit":"char.rsplit",\
    "rstrip":"char.rstrip",\
    "split":"char.split",\
    "splitlines":"char.splitlines",\
    "startswith":"char.startswith",\
    "strip":"char.strip",\
    "swapcase":"char.swapcase",\
    "title":"char.title",\
    "translate":"char.translate",\
    "upper":"char.upper",\
    "zfill":"char.zfill",\
    "isnumeric":"char.isnumeric",\
    "isdecimal":"char.isdecimal",\
    "take":"take",\
    "reshape":"reshape",\
    "choose":"choose",\
    "repeat":"repeat",\
    "put":"put",\
    "swapaxes":"swapaxes",\
    "transpose":"transpose",\
    "partition":"partition",\
    "sort":"sort",\
    "argsort":"argsort",\
    "argmax":"argmax",\
    "argmin":"argmin",\
    "searchsorted":"searchsorted",\
    "resize":"resize",\
    "squeeze":"squeeze",\
    "diagonal":"diagonal",\
    "trace":"trace",\
    "ravel":"ravel",\
    "eye":"eye",\
    "nonzero":"nonzero",\
    "shape":"shape",\
    "compress":"compress",\
    "clip":"clip",\
    "sum":"sum",\
    "product":"product",\
    "sometrue":"sometrue",\
    "alltrue":"alltrue",\
    "any":"any",\
    "all":"all",\
    "cumsum":"cumsum",\
    "cumproduct":"cumproduct",\
    "ptp":"ptp",\
    "amax":"amax",\
    "amin":"amin",\
    "alen":"alen",\
    "prod":"prod",\
    "cumprod":"cumprod",\
    "ndim":"ndim",\
    "rank":"rank",\
    "size":"size",\
    "around":"around",\
    "mean":"mean",\
    "std":"std",\
    "var":"var",\
    "finfo":"finfo",\
    "iinfo":"iinfo",\
    "empty":"empty",\
    "quit":"quit",\
    "plot":"pylab.plot",\
    "subplot":"pylab.subplot",\
}
cmdmap = \
{\
    "quit":"quit()",\
    "cl":"clear()",\
    "get_printoptions":"get_printoptions()",\
}
#-------------------------------------------------------------------------------
# Regular expressions to parse the matlab command
#-------------------------------------------------------------------------------
# Some often used regular expressions
varletters = r"_%s%s"%(string.ascii_letters,string.digits)
varbletters = r"_%s"%(string.ascii_letters) # Digit cannot start a variable name
varname = r"[%s][%s]*"%(varbletters,varletters)
operators = r"\+\-\*\/\^\(\)"
# Match invoking function
# func(arguments)
refunc = r"^(%s)\((.*)\);?$"%varname
# Match assign return value of a function to variable
# var = func(arguments)
reassignfunc = r"^(%s)\s*=\s*(%s)\((.*)\);?$"%(varname, varname)
# Match commands consisting of only white characters
rewhite = r"^[%s]+$"%(string.whitespace)
# Match commands or variable names with no ()
# variable / function
rename = r"^(%s);?$"%(varname)
# Match a math expression
rearithm = r"^([%s%s]+);?$"%(varletters,operators)
# Match assign math expression to variable
reassignarithm = r"^(%s)\s*=\s*([%s%s]+);?$"%(varname,varletters,operators)
################################################################################
####################### STATE VARIABLES ########################################
################################################################################
history = []
phist = 0
cmdstart = "1,0"
ans = None
################################################################################
####################### OTHER FUNCTIONS ########################################
################################################################################
def gotoEnd(): # Move cursor to the end
    out.mark_set(INSERT,END)

def output(s): # Print something in the text area
    out.insert(END,s)
    out.see(END) # Make sure end is seen

def clear(): # Clear the text area
    out.delete(1.0,END)

def printl(s): # Print a line in the text area
    output("%s\n"%s)

def printPrompt(): # Print prompt
    global cmdstart
    output(">> ")
    # Move the mark of "fixed" area to the end of the prompt
    cmdstart = out.index(END+"-1c")
    gotoEnd()

def ready(): # Work to do when entering ready state
    printPrompt()

# Compare which index is smaller
# Indices are like 1.5 or 3.2, meaning the third row and second column
# a.b < c.d iff a < c or a==c and b<d
def indexSmaller(i1, i2):
    y1,x1 = i1.split(".")
    y2,x2 = i2.split(".")
    if int(y1) < int(y2):
        return True
    elif int(y1) == int(y2):
        if int(x1) < int(x2):
            return True
        else:
            return False
    else:
        return False

# Compare which index is smaller
# Indices are like 1.5 or 3.2, meaning the third row and second column
# a.b <= c.d iff a <= c or a==c and b<d
def indexSmallerEqual(i1, i2):
    y1,x1 = i1.split(".")
    y2,x2 = i2.split(".")
    if int(y1) < int(y2):
        return True
    elif int(y1) == int(y2):
        if int(x1) <= int(x2):
            return True
        else:
            return False
    else:
        return False

def getCommand(): # Get the command(text after the prompt) from text area
    return out.get(cmdstart,out.index(END+"-1c"))

def delchar(): # Delete one character at the end of the text area
    out.delete(END+"-2c",END+"-1c")

def keyPress(event): # When any key is pressed
    # If the cursor is in the fixed area, go to the end
    # Note that we can't always let the cursor go to the end, or one would be
    # unable to insert something in the middle of the command line
    if indexSmaller(out.index(INSERT),cmdstart):
        gotoEnd()

def returnPress(event): # When pressing enter
    cmd = getCommand() # Get the command line
    process(cmd) # Process command
    ready() # Enter ready state
    return "break" # Prevent the text area from calling its own callback

def backPress(event): # When backspace pressed
    if indexSmallerEqual(out.index(INSERT),cmdstart):
        if indexSmaller(out.index(INSERT),cmdstart):
            gotoEnd() # Go to end of the text area
        return "break"

def deleteCommand(): # Delete until prompt ">>"
    while getCommand() != "":
        delchar()

def upPress(event): # When up arrow is pressed
    global phist # Pointer to history command
    if phist > 0: # Decrement pointer by one until 0
        phist -= 1
    if len(history) > 0: # Put the current history command in the text area
        deleteCommand() # Delete the current command first
        if phist < len(history):
            cmdline = history[phist]
        output(cmdline) # Print the command line to the text area
    return "break"

def downPress(event): # When up arrow is pressed, just similar to upPress
    global phist
    if phist < len(history):
        phist += 1
    if len(history) > 0:
        deleteCommand()
        if phist < len(history):
            cmdline = history[phist]
            output(cmdline)
    return "break"

def leftClick(event): # When left mouse clicked
    pass

def fig2img(fig): # Transform a pylab figure to a PIL image
    fig.canvas.draw()
    w,h = fig.canvas.get_width_height()
    buf = fromstring(fig.canvas.tostring_argb(),dtype=uint8)
    buf.shape = (w, h, 4)
    buf = roll(buf,3,axis=2)
    return Image.fromstring("RGBA",(w,h),buf.tostring())

def draw(): # Plot the current figure on the canvas
    global img # Global it so that it won't be collected when this function ends
    # Transform figure to PIL image, resize it to 500x500, and transform to Tk
    # photo image
    img = ImageTk.PhotoImage(fig2img(pylab.gcf()).resize((500,500)))
    # Draw the image
    cvs.create_image(250,250,image=img)

def process(cmd): # Process command line
    global history,phist # Need to alter the command history
    global ans # The result of the previous command
    printl("") # Change line first
    if cmd == "": return # If command line is empty, do nothing

    # Go through all the command patterns and parse the command line with those
    # patterns. If match, process the command using that pattern

    # func(args)
    g = re.match(refunc,cmd) # Do the regular expression match
    if g: # Match succeed, g is not None
        try: # In case the function name does not exist
            pfunc = funcmap[g.group(1)] # Transform matlab cmd to python
        except Exception as inst: # Print error message on error
            printl("Error in: %s"%cmd)
            printl("%s: No such function"%g.group(1))
            printl(inst)
            return
        # Assemble the python command
        if g.group(2): # There are arguments
            pcmd = "%s(%s)"%(pfunc,g.group(2)) # Parse arguments
        else:
            pcmd = "%s()"%(pfunc) # Called with no arguments
        try:
            ans = eval(pcmd) # Evaluate python command and keep the result
            # If there is pylab, draw the current figure to the canvas
            if pfunc[:6] == "pylab.": 
                draw()
            else: # Or just print the result (unless None or ';' is used)
                if ans is not None and cmd[-1]!=";": printl(ans)
        except Exception as inst:
            printl("Error in: %s"%cmd)
            printl("Translated python: %s"%pcmd)
            printl(inst)
        history.append(cmd) # Record command
        phist = len(history) # Pointer point to the end of history list
        return

    # x = func(args)
    g = re.match(reassignfunc,cmd)
    if g:
        var = g.group(1)
        try:
            pfunc = funcmap[g.group(2)]
        except Exception as inst:
            printl("Error in: %s"%cmd)
            printl("%s: No such function"%g.group(2))
            printl(inst)
        if g.group(3):
            pcmd = "%s(%s)"%(pfunc,g.group(3))
        else:
            pcmd = "%s()"%(pfunc)
        try:
            ans = eval(pcmd)
            globals().update([[var,ans]]) # Assignment of variable
            if pfunc[:6] == "pylab.":
                draw()
            else:
                if ans is not None and cmd[-1]!=";": printl(ans)
        except Exception as inst:
            printl("Error in: %s"%cmd)
            printl("Translated python: %s"%pcmd)
            printl(inst)
        history.append(cmd)
        phist = len(history)
        return
    # Match a single name
    g = re.match(rename,cmd)
    if g:
        var = g.group(1)
        if var in cmdmap:
            try:
                pfunc = cmdmap[var]
                ans = eval(pfunc)
                if pfunc[:6] == "pylab.":
                    draw()
                else:
                    if ans is not None and cmd[-1]!=";": printl(ans)
            except Exception as inst:
                printl("Error in: %s"%cmd)
                printl(inst)
                return
        else: # Try to evaluate as variable
            try:
                ans = eval(var)
                if ans is not None and cmd[-1]!=";": printl(ans)
            except Exception as inst:
                printl("Error in: %s"%cmd)
                printl(inst)
        return

    # Match math expression
    g = re.match(rearithm,cmd)
    if g:
        e = g.group(1)
        try:
            ans = eval(e)
            if ans is not None and cmd[-1]!=";": printl(ans)
        except Exception as inst:
            printl("Error in: %s"%cmd)
            printl(inst)
        return

    # Match assignment of math expression
    g = re.match(reassignarithm,cmd)
    if g:
        var = g.group(1)
        e = g.group(2)
        try:
            ans = eval(e)
            globals().update([[var,ans]])
            if ans is not None and cmd[-1]!=";": printl(ans)
        except Exception as inst:
            printl("Error in: %s"%cmd)
            printl(inst)
        return

    # Match white space
    g = re.match(rewhite,cmd)
    if g:
        return

    # No match, print error message
    printl("Error in: %s"%cmd)

################################################################################
####################### TKINTER OBJECTS ########################################
################################################################################
#----------------------Root-----------------------------------------------------
root = Tk()
# root.columnconfigure(3)
# root.rowconfigure(2)
#----------------------BUTTONS--------------------------------------------------
bts = Frame(root)
bts.grid(row=0,column=0)
bns = []
bns.append(Button(bts,text="Button1"))
bns[-1].grid(row=len(bns),column=0)
bns.append(Button(bts,text="Button2"))
bns[-1].grid(row=len(bns),column=0)
bns.append(Button(bts,text="Button3"))
bns[-1].grid(row=len(bns),column=0)
bns.append(Button(bts,text="Button4"))
bns[-1].grid(row=len(bns),column=0)
#----------------------TEXT BOXES-----------------------------------------------
out = Text(root,width=50,height=30)
out.grid(row=0,column=1,sticky=E+W+S+N)
out.bind("<Key>",keyPress)
out.bind("<Return>",returnPress)
out.bind("<BackSpace>",backPress)
out.bind("<Up>",upPress)
out.bind("<Down>",downPress)
out.bind("<Button-1>",leftClick)
#----------------------Canvases-------------------------------------------------
cvs = Canvas(root,width=500,height=500)
cvs.grid(row=0,column=2)
################################################################################
####################### INITIALIZATIONS ########################################
################################################################################
output(greeting)
ready()
root.mainloop()
