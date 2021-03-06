################################################################################
"""
A Simple Python Implementation of Matlab

----------------------------------------------------------------------
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|        OUTPUT AREA            |        FIGURE SHOWN HERE           |
|                               |                                    |
|        (readonly textbox)     |        (canvas)                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
|                               |                                    |
----------------------------------------------------------------------
"""
################################################################################
from __future__ import division
from Tkinter import *
import pylab
from numpy import *
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.image as mpimg
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
Type "help" for any help.
"""
#-------------------------------------------------------------------------------
# Help information
HelpInfo = \
"""
Currently supported commands:

    abs add alen all alltrue amax amin any arange arccos arcsin arctanh argmax
    argmin argsort around array array2string capitalize center choose clf clip
    compress concatenate copyto cos count count_nonzero cumprod cumproduct
    cumsum decode diagonal disp empty encode endswith equal expandtabs eye find
    finfo frombuffer fromfile fromstring get_printoptions greater greater_equal
    iinfo imread imshow index isalnum isalpha isdecimal isdigit islower
    isnumeric isspace istitle isupper join len less less_equal linspace ljust
    log log10 log2 logspace lower lstrip mean mod multiply ndim nonzero
    not_equal ones outer partition plot plot_surface poly poly1d polyadd polyder
    polydiv polyfit polyint polymul polysub polyval power prod product ptp put
    quit range rank ravel repeat replace reshape resize rfind rindex rjust roots
    rpartition rsplit rstrip script searchsorted set_printoptions shape sin size
    size sometrue sort spartition split splitlines sqrt squeeze startswith std
    strip str_len subplot sum swapaxes swapcase take title trace translate
    transpose upper var zeros zfill

For help of specific command, type: help commandname
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
    "fromstring":"fromstring",\
    "fromfile":"fromfile",\
    "frombuffer":"frombuffer",\
    "zeros":"zeros",\
    "count_nonzero":"count_nonzero",\
    "copyto":"copyto",\
    "concatenate":"concatenate",\
    "script":"script",\
    "quit":"exit",\
    "imread":"mpimg.imread",\
    "imshow":"pylab.imshow",\
    "plot":"pylab.plot",\
    "len":"len",\
    "clf":"pylab.clf",\
    "subplot":"pylab.subplot",\
    "plot_surface":"ax.plot_surface",\
}
cmdmap = \
{\
    "quit":"exit",\
    "cl":"clear",\
    "get_printoptions":"get_printoptions",\
    "end":"end",\
    "help":"help",\
}
#-------------------------------------------------------------------------------
# Regular expressions to parse the matlab command
#-------------------------------------------------------------------------------
# Some often used regular expressions
varletters = r"_%s%s\[\]"%(string.ascii_letters,string.digits)
varbletters = r"_%s"%(string.ascii_letters) # Digit cannot start a variable name
varname = r"[%s][%s]*"%(varbletters,varletters)
operators = r"\+\-\*\/\^\(\)\s"
whites = r"[%s]*"%(string.whitespace)
# Match invoking function
# func(arguments)
refunc = r"^%s(%s)\((.*)\);?$"%(whites,varname)
# Match assign return value of a function to variable
# var = func(arguments)
reassignfunc = r"^%s(%s)\s*=\s*(%s)\((.*)\);?$"%(whites,varname, varname)
# Match commands consisting of only white characters
rewhite = r"^[%s]+$"%(string.whitespace)
# Match commands or variable names with no ()
# variable / function
rename = r"^%s(%s);?$"%(whites,varname)
# Match a math expression
rearithm = r"^%s([%s%s]+);?$"%(whites,varletters,operators)
# Match assign math expression to variable
reassignarithm =\
r"^%s(%s)\s*=\s*([%s%s]+);?$"%(whites,varname,varletters,operators)
# Match command argus
recommand =\
r"^%s(%s)\s+%s([%s][%s\s]+[%s])%s;?$"\
%(whites,varname,whites,varletters,varletters,varletters,whites)
# Match for loop
reforloop = r"^%sfor\s+(%s)\s*=(.*)$"%(whites,varname)
# Match if
reif = r"^%sif\s+(.*)\s+then%s$"%(whites,whites)
################################################################################
####################### STATE VARIABLES ########################################
################################################################################
history = []
phist = 0
cmdstart = "1,0"
ans = None
ax = None
cand = []
pcand = 0
# Depth of loop/if ..
depth = 0
# script buffer
scriptBuf = ""
toGlobalVars = []
################################################################################
####################### OTHER FUNCTIONS ########################################
################################################################################
def exit():
    saveHistory("history.m")
    quit()

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
    if depth == 0:
        output(">> ")
    else:
        output("---%s"%("----"*depth))
    # Move the mark of "fixed" area to the end of the prompt
    cmdstart = out.index(END+"-1c")
    gotoEnd()

def ready(): # Work to do when entering ready state
    printPrompt()

def help(cmdname = None): # loop up help file of some command
    if not cmdname:
        printl(HelpInfo)
        return
    try:
        with open("%s.hp"%cmdname) as f:
            printl(f.read())
    except Exception as inst:
        printl("No help information for '%s'."%cmdname)

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

# Open script file and execute
def script(filename):
    with open(filename) as f:
        cmds = f.readlines()
        for c in cmds:
            if c[-1] == "\n": c = c[:-1]
            process(c)

def getCommand(): # Get the command(text after the prompt) from text area
    return out.get(cmdstart,out.index(END+"-1c"))

def delchar(): # Delete one character at the end of the text area
    out.delete(END+"-2c",END+"-1c")

def keyPress(event): # When any key is pressed
    # These are used in tab completion, erased whichever key is pressed
    global cand, pcand
    # If the cursor is in the fixed area, go to the end
    # Note that we can't always let the cursor go to the end, or one would be
    # unable to insert something in the middle of the command line
    if indexSmaller(out.index(INSERT),cmdstart):
        gotoEnd()
    cand = []
    pcand = -1

def isEndCommand(s):
    g = re.match("^%send?%s$"%(whites,whites),s)
    if g:
        return True
    else:
        return False

def returnPress(event): # When pressing enter
    # These are used in tab completion, erased whichever key is pressed
    global cand, pcand
    cand = []
    pcand = -1
    cmd = getCommand() # Get the command line
    # If the command is "end", unintend it for elegacy
    if isEndCommand(cmd) and depth > 0:
        for i in range(7):
            delchar()
        output("end")
    printl("")
    process(cmd) # Process command
    ready() # Enter ready state
    return "break" # Prevent the text area from calling its own callback

def backPress(event): # When backspace pressed
    # These are used in tab completion, erased whichever key is pressed
    global cand, pcand
    cand = []
    pcand = -1
    if indexSmallerEqual(out.index(INSERT),cmdstart):
        if indexSmaller(out.index(INSERT),cmdstart):
            gotoEnd() # Go to end of the text area
        return "break"

def deleteCommand(): # Delete until prompt ">>"
    while getCommand() != "":
        delchar()

def upPress(event): # When up arrow is pressed
    # These are used in tab completion, erased whichever key is pressed
    global cand, pcand
    cand = []
    pcand = -1
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
    # These are used in tab completion, erased whichever key is pressed
    global cand, pcand
    cand = []
    pcand = -1
    global phist
    if phist < len(history):
        phist += 1
    if len(history) > 0:
        deleteCommand()
        if phist < len(history):
            cmdline = history[phist]
            output(cmdline)
    return "break"

def tabPress(event): # When Tab is pressed, do completion
    global cand, pcand
    cmd = getCommand()
    if cmd == "": return "break"
    # pcand = -1 means there is no candidate list
    if pcand == -1:
        cand = [] # Build one
        # Search through all function names and commands and select those
        # with the current prefix
        for c in funcmap.keys():
            if c.startswith(cmd):
                cand.append(c)
        for c in cmdmap.keys():
            if c.startswith(cmd):
                cand.append(c)
        # Set pointer points to the first candidate
        pcand = 0
    else: # There is already one list, just increment the pointer
        if len(cand) > 0:
            pcand += 1
            if pcand >= len(cand):
                pcand = -1
    # Do the completion
    if pcand >= 0 and pcand < len(cand):
        deleteCommand()
        output(cand[pcand])
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
    global ax # Axes object
    # Transform figure to PIL image, resize it to 500x500, and transform to Tk
    # photo image
    img = ImageTk.PhotoImage(fig2img(pylab.gcf()).resize((500,500)))
    # Draw the image
    cvs.create_image(250,250,image=img)
    # If the command is subplot, then ans is an axes object now
    if str(type(ans)) == "<class 'matplotlib.axes.Axes3DSubplot'>":
        ax = ans

def readHistory(filename): # Read history from history file
    global history, phist
    try:
        with open(filename) as f:
            hists = f.readlines()
            for h in hists:
                if h[-1] == "\n": h = h[:-1] # Remove the last EOL
                history.append(h)
        phist = len(history)
        printl("Successfully read history file: %s\n"%filename)
    except:
        printl("Cannot find history file: %s"%filename)

def saveHistory(filename): # Save history
    with open(filename,"w") as f:
        for h in history:
            f.write("%s\n"%h)

def clearHistory():
    global history
    history = []

def logPythonScript(script):
    global scriptBuf
    scriptBuf += "%s%s\n"%("\t"*depth,script)

def clearTempScript():
    global scriptBuf, toGlobalVars
    scriptBuf = ""
    toGlobalVars = []

def end():
    global depth
    if depth > 0:
        depth -= 1
        if depth == 0: # The last end, start execute
            try:
                if len(toGlobalVars) > 0:
                    exec("global %s\n%s"%(" ".join(toGlobalVars),scriptBuf))
                else:
                    exec(scriptBuf)
            except Exception as inst:
                printl(inst)
    else:
        printl("Error in: end")
        printl("Nothing to end!")
        
# When using exec() to execute loops, the variables are treated as local
# so a list of variable names have to be maintained and before using
# exec() they are declared global first
def toGlobal(var):
    global toGlobalVars
    g = re.match("^([a-zA-Z0-9_]+).*$",var)
    if g:
        if not g.group(1) in toGlobalVars:
            toGlobalVars.append(g.group(1))

def process(cmd): # Process command line
    global history,phist # Need to alter the command history
    global ans # The result of the previous command
    global depth
    if cmd == "": return # If command line is empty, do nothing
    history.append(cmd) # Record command
    phist = len(history) # Pointer point to the end of history list

    # Go through all the command patterns and parse the command line with those
    # patterns. If match, process the command using that pattern


    if isEndCommand(cmd):
        end()
        return

    # Match for loop
    g = re.match(reforloop,cmd)
    if g:
        var = g.group(1)
        rge = g.group(2)
        if depth == 0:
            clearTempScript()
        logPythonScript("for %s in %s:"%(var,rge))
        depth += 1
        return

    # Match if
    g = re.match(reif,cmd)
    if g:
        e = g.group(1)
        if depth == 0:
            clearTempScript()
        logPythonScript("if %s:"%e)
        depth += 1
        return

    # Match command with arguments
    g = re.match(recommand,cmd)
    if g:
        try:
            pfunc = cmdmap[g.group(1)]
            argus = "\"%s\""%("\",\"".join(g.group(2).split(" ")))
        except Exception as inst:
            printl("Error in: %s"%cmd)
            printl("%s: No such command"%g.group(1))
            printl(inst)
            return
        pcmd = "%s(%s)"%(pfunc,argus)
        if depth == 0:
            try:
                ans = eval(pcmd)
                if ans is not None and cmd[-1]!=";": printl(ans)
            except Exception as inst:
                printl("Error in: %s"%cmd)
                printl("Translated python: %s"%pcmd)
                printl(inst)
        else: # Else, just remember the command, and execute it until end
            logPythonScript(pcmd)
        return

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
        if depth == 0: # Evaluate the command only when depth = 0
            try:
                ans = eval(pcmd) # Evaluate python command and keep the result
                # If there is pylab, draw the current figure to the canvas
                if pfunc[:6] == "pylab." or pfunc[:3] == "ax.": 
                    draw()
                else: # Or just print the result (unless None or ';' is used)
                    if ans is not None and cmd[-1]!=";": printl(ans)
            except Exception as inst:
                printl("Error in: %s"%cmd)
                printl("Translated python: %s"%pcmd)
                printl(inst)
        else: # Else, just remember the command, and execute it until end
            logPythonScript(pcmd)
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
            return
        if depth == 0:
            if g.group(3):
                pcmd = "global %s\n%s=%s(%s)"%(var,var,pfunc,g.group(3))
            else:
                pcmd = "global %s\n%s=%s()"%(var,var,pfunc)
            try:
                exec(pcmd)
                ans = eval(var)
                if pfunc[:6] == "pylab." or pfunc[:3] == "ax.":
                    draw()
                else:
                    if ans is not None and cmd[-1]!=";": printl(ans)
            except Exception as inst:
                printl("Error in: %s"%cmd)
                printl("Translated python: %s"%pcmd)
                printl(inst)
        else:
            if g.group(3):
                pcmd = "%s=%s(%s)"%(var,var,pfunc,g.group(3))
            else:
                pcmd = "%s=%s()"%(var,var,pfunc)
            toGlobal(var)
            logPythonScript(pcmd)
        return

    # Match a single name
    g = re.match(rename,cmd)
    if g:
        var = g.group(1)
        pcmd = var
        if var in cmdmap:
            if depth == 0:
                try:
                    pfunc = cmdmap[var]
                    ans = eval("%s()"%pfunc)
                    if pfunc[:6] == "pylab." or pfunc[:3] == "ax.":
                        draw()
                    else:
                        if ans is not None and cmd[-1]!=";": printl(ans)
                except Exception as inst:
                    printl("Error in: %s"%pcmd)
                    printl(inst)
                    return
            else:
                logPythonScript(pcmd)
        else: # Try to evaluate as variable
            if depth == 0:
                try:
                    ans = eval(var)
                    if ans is not None and cmd[-1]!=";": printl(ans)
                except Exception as inst:
                    printl("Error in: %s"%pcmd)
                    printl(inst)
            else:
                logPythonScript(pcmd)
        return

    # Match math expression
    g = re.match(rearithm,cmd)
    if g:
        e = g.group(1)
        if depth == 0:
            try:
                ans = eval(e)
                if ans is not None and cmd[-1]!=";": printl(ans)
            except Exception as inst:
                printl("Error in: %s"%cmd)
                printl(inst)
        else:
            logPythonScript(e)
        return

    # Match assignment of math expression
    g = re.match(reassignarithm,cmd)
    if g:
        var = g.group(1)
        e = g.group(2)
        if depth == 0:
            pcmd = "global %s\n%s=%s"%(var,var,e)
            try:
                exec(pcmd)
                ans = eval(var)
                if ans is not None and cmd[-1]!=";": printl(ans)
            except Exception as inst:
                printl("Error in: %s"%cmd)
                printl(inst)
        else:
            pcmd = "%s=%s"%(var,e)
            toGlobal(var)
            logPythonScript(pcmd)
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
#----------------------TEXT BOXES-----------------------------------------------
out = Text(root,width=80,height=40)
out.grid(row=0,column=0,sticky=E+W+S+N)
out.bind("<Key>",keyPress)
out.bind("<Return>",returnPress)
out.bind("<BackSpace>",backPress)
out.bind("<Up>",upPress)
out.bind("<Down>",downPress)
out.bind("<Tab>",tabPress)
out.bind("<Button-1>",leftClick)
#----------------------Canvases-------------------------------------------------
cvs = Canvas(root,width=500,height=500)
cvs.grid(row=0,column=1)
################################################################################
####################### INITIALIZATIONS ########################################
################################################################################
output(greeting)
readHistory("history.m")
ready()
root.mainloop()
