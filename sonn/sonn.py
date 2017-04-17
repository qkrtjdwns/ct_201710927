Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> wn= turtle.Screen()
>>> t1=turtle.Turtle
>>> t1=turtle.Turtle()
>>> t1.shape('turtle')
>>> wn.addshape('son.gif')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    wn.addshape('son.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1133, in register_shape
    shape = Shape("image", self._image(name))
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 479, in _image
    return TK.PhotoImage(file=filename)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3539, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3495, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "son.gif": no such file or directory
>>> t1.shape('\\400T6Bwwson')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t1.shape('\\400T6Bwwson')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named \400T6Bwwson
>>> t1.shape('C:\Users\400T6B\son')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> t1.shapeC:\Users\400T6B\son
SyntaxError: unexpected character after line continuation character
>>> t1.shapeC:\\Users\\400T6B\\son
SyntaxError: unexpected character after line continuation character
>>> t1.shape('C:\\Users\\400T6B\\son')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\son')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\son
>>> t1.shape('C:\\Users\\400T6B\\son.gif')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\son.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\son.gif
>>> t1.shape('C:\\Users\\400T6B\\son.gif')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\son.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\son.gif
>>> t1.shape('C:\\Users\\400T6B\\son')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\son')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\son
>>> t1.shape('C:\\Users\\400T6B\\son')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\son')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\son
>>> t1.shape('C:\\Users\\400T6B\\.son')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\.son')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\.son
>>> t1.shape('C:\\Users\\400T6B\\son.gif')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\son.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\son.gif
>>> t1.shape('C:\\Users\\400T6B\\rocketship.gif')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\rocketship.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\rocketship.gif
>>> t1.shape('C:\\Users\\400T6B\\rocketship.gif')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\rocketship.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\rocketship.gif
>>> t1.addshape('C:\\Users\\400T6B\\rocketship.gif')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t1.addshape('C:\\Users\\400T6B\\rocketship.gif')
AttributeError: 'Turtle' object has no attribute 'addshape'
>>> wn.addshape('C:\\Users\\400T6B\\rocketship.gif')
>>> wn.addshape('C:\\Users\\400T6B\\rocketship.gif')
>>> wn.addshape('C:\\Users\\400T6B\\son.gif')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    wn.addshape('C:\\Users\\400T6B\\son.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1133, in register_shape
    shape = Shape("image", self._image(name))
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 479, in _image
    return TK.PhotoImage(file=filename)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3539, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3495, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "C:\Users\400T6B\son.gif": no such file or directory
>>> wn.addshape('C:\\Users\\400T6B\\rocketship.gif')
>>> wn.addshape('C:\\Users\\400T6B\\rocketship.gif')
>>> 
>>> 
>>> 
>>> wn.addshape('C:\\Users\\400T6B\\rocketship.gif')
\
>>> wn.addshape('C:\\Users\\400T6B\\rocketship.gif')
>>> t1.shape('C:\\Users\\400T6B\\rocketship.gif')
>>> wn.addshape('C:\\Users\\400T6B\\son.gif')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    wn.addshape('C:\\Users\\400T6B\\son.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1133, in register_shape
    shape = Shape("image", self._image(name))
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 479, in _image
    return TK.PhotoImage(file=filename)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3539, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3495, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "C:\Users\400T6B\son.gif": no such file or directory
>>> wn.addshape('C:\\Users\\400T6B\\sonn.gif')
>>> t1.shape('C:\\Users\\400T6B\\sonn.gif')
>>> t1.shape('C:\\Users\\400T6B\\sonn.gif')
>>> t1.fd(100)
>>> 
