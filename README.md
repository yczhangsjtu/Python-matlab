Python-matlab
=============

A python version of simple implementation of matlab. Used for familiarizing with pylab.

For simplicity some functions are not exactly matlab functions. And there are some problems with 3-d plotting.

The basic implementation tricks are as follows:

1. Use regular expression to parse the matlab commands

   Currently only supporting these formats:

   i.   func( args ): use a map to transform func to corresponding python function, combine it again with "(%s)"%args, eval() it

   ii.  var = func( args ): Same to the previous one, and then use globals().update to assign the result to the variable

   iii. math expression: Evaluate directly

   iv.  var = math expression: Evaluate and use globals().update to assign result to variable
   
   v.   command: map it to a python expression and eval()

2. If the python function contains prefix "pylab.", then invoke draw function to draw the current figure on the canvas

3. The text area is a Tkinter text widget. Several text processing techniques are used to make it perform like a command line.
   Many special key callback functions are redirected.

Currently supported commands:

disp

linspace

logspace

outer

ones

size

abs

sin

cos

sqrt

log

log2

log10

power

arccos

arcsin

arctanh

poly

roots

polyint

polyder

polyadd

polysub

polymul

polydiv

polyval

poly1d

polyfit

array

range

arange

array2string

set_printoptions

get_printoptions

equal

not_equal

greater_equal

less_equal

greater

less

str_len

add

multiply

mod

capitalize

center

count

encode

decode

endswith

expandtabs

find

index

isalnum

isalpha

isdigit

islower

isspace

istitle

isupper

join

ljust

lower

lstrip

spartition

replace

rfind

rindex

rjust

rpartition

rsplit

rstrip

split

splitlines

startswith

strip

swapcase

title

translate

upper

zfill

isnumeric

isdecimal

take

reshape

choose

repeat

put

swapaxes

transpose

partition

sort

argsort

argmax

argmin

searchsorted

resize

squeeze

diagonal

trace

ravel

eye

nonzero

shape

compress

clip

sum

product

sometrue

alltrue

any

all

cumsum

cumproduct

ptp

amax

amin

alen

prod

cumprod

ndim

rank

size

around

mean

std

var

finfo

iinfo

empty

quit

plot

subplot


