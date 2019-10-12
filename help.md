# Documentation
## Contents
* [Variables](#Variables)
  * [Pre-defined static variables](#Pre\-defined-static-variables)
  * [Operators](#Operators)
  * [Basic if-else syntax](#Basic-if\-else-syntax)
* [Loops](#Loops)
  * [While](#While)
  * [For](#For)
* [Functions](#Functions)
  * [User-defined functions](#User\-defined-functions)
  * [Built-in functions](#Built\-in-functions)
    * [Program functions](#Program-functions)
    * [Screen functions](#Screen-functions)
    * [Time functions](#Time-functions)
    * [Value type functions](#Value-type-functions)
    * [Type functions](#Type-functions)

## Basic syntax
Multiple statements can be written inline like so: `1+2;Func();etc()`
They can also be separated by a new line:
```
1+2
Func()
etc()
```
Or combined:
```
1+2;Func()
Etc();
```

Multiline statements don't work directly in the interpreter. you neeed to write them in a file. They only work if they are separated by a semicolon: `func a() => Print("sample"); Print(" text\n");`

## Variables
set var name = \<expression\>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
creates/sets a variable

### Pre-defined static variables
NaN - Is bassicly just 0
True, False = 1, 0

### Operators
+, -, *, /, ^
and, or, >, <, ==, !=

### Basic if-else syntax
```
if **expression** then
    **do stuff**
elif **expression** then 
    **do other stuff** 
else
    **do even more stuff**
end
```
Inline: if **expression** then **do stuff** elif **expression** then **do other stuff** else **do even more stuff** end

It can also be directly assigned to variables: set **var name** = if **condition** then **return value** else **return value**

## Loops
### While
```
while **expression** then
    **do stuff**
end
```
### For
```
for **var_name** = **start_value** to **max_value** step **value (is like i = i + value)** then 
    **do stuff**
end
```
## Functions
### User-defined functions
func **name**(**arguments\***) => **expressions**  - creates a function
They can also be **anonymous**:
set **foo** = func(**a, b**) => **a+b**

Multi-line:
```
func **name**(**arguments**) => (or newline)
    **expressions**
end
```

### Built-in functions
#### Program functions
* Exit() - Exits program with error code 0.
#### Screen functions
* Print(**value**) - Prints stuff
* PrintRet(**value**) - Returns the printed stuff without printing it to the screen. Makes sense right?
* Input(**prompt**) - Yes.
* InputInt(**prompt**) - Same as Input() but accepts only integers (TODO: Print only numbers)
* Clear() or Cls() - Clears the screen

#### Time functions
* Sleep(amount) or Delay(amount) - Wait x number of seconds 

#### Value type functions
* isNum(**value**) - Checks to see if value is a number
* isString(**value**) - Checks to see if value is a string
* isList(**value**) - Checks to see if value is a list
* isFunc(**value**) - Checks to see if value is a function

#### Type functions
##### List functions
* Append(**list, value**) - Appends a value to a list
* Pop(**list, index**) - Removes a value from a list at a specified index
* Extend(**list1, list2**) - Adds 2 lists together
* ClearList(**list**) - Clears a list
