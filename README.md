                                            Why Python?!!!

Readability and Simplicity: Python's syntax emphasizes readability and is easy to understand.

Cross-Platform comptability: Python is available on multiple plratforms, including Windows Macos and Linux.

Ease of learning : which is python simple consistent syntax allows beginners to learn programming concepts quickly.

Support for object-oriented and functional programming and moree ....

                                How to print text and variables using print:

printing text:
    print("Hello, world!")
console: Hello, world!

or we identify a variable and then print it :

    age = 25
    print(age)
console: 25

also we can print text and variables together :

    name : "Moussa"
    age : 25
    print("My name is", name, "and I'm", age, "y.o")
console: My name is Moussa and I'm 25 y.o

Formatting with f-strings (Python 3.6+):

while we use formatting with print we start with (f"") and we use curly brackets{}.

    name = "Moussa" 
    age = 25
    print(f"My name is {name} and I'm {age} years old.")
console: My name is Moussa and I'm 25 years old.

an other way of formatting. we use ("{}".format())
    
    printf("My name is {} and I'm {} years old.".format(name, age))
console: My name is Moussa and I'm 25 years old.

concatenating strings and variables :
your write like this print(""+variable+""+variable), but intigers should be changed to string format by doing this:
"str(int)"
    name = Moussa
    age = 25
    print("My name is " +name+ "and I'm" +str(age) "years old.")
and the console will show this : My name is Moussa and I'm 25 years old.

Or you can use the var "age" to be a string like this 
    age = '25' instead of age = 25
    print("My age is "+age) 
    console: My age is 25

N.B: printf() function automatically adds newline character at the end by default, I would want to print without a newline, I can use end 
parameter:
example : print("hello, world" end=" ")

Creating strings:
strings can be created while using either single quotes (''), or double quotes (""),
example:  single_quoted = 'Hello world' 
          double_quoted = "Hello world"

Multi line strings:
is using triple quotes ''' ''' and it is used to create multilines .
example: print('''hello,
                world''')
        console: hello,
                world

string concatenating:
where strings can be concatenated using the "+" operator.
    greeting = "hello"
    name = "Moussa"
    message = greeting + name
    printf(message)
    console: hello Moussa

string Replication:
strings can be replicated using the * operator.
repeated = " " * 10
example: print("hello " * 5)
    console: hello hello hello 

string Methods: strings have many built-in methods for manipulation, such as 
    upper() : printf(name.upper()) = MOUSSA
    lower() : prinf(name.upper()) moussa
    capitalize() : printf(name.capitalize()) = Moussa
    replace() : printf(name.replace("moussa", "Moussa")) = Moussa Sabbar
    split() : fruits = "apple orange , berries" , printf(fruits.split())
    console: ['apple', 'orange', 'berries'] 
    the split method is changing the variable to an array
    we can alsodo this :print(fruits.split() [1])
    console: orange

string length: this function is used to know how many char are in a string : len(var_name)
    print(len(name))
    console: # 6

Indexing and slicing strings:

indexing : is accessing characters in a str 
    languag = "Python"
    first_char = language[0] # 'P'
    last_char =  language[] # 'n'

slicing : allows you to extract a portion of a string.
    phrase = "Python is fun"
    slice = phrase[:] = # Python is fun 
    second_slice = phrase[1:7] = # ython is
    third_slice = phrase[:6] = # Python 
 
 the func is print(phrase[:])
 console : Python is fun
