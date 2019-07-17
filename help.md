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
if **expression** then **do stuff** elif **expression** then **do other stuff** else **do even more stuff**

## Loops
### While
while **expression** then **do stuff**

### For
for **var_name** = **start_value** to **max_value** step **value (is like i = i + value)** then **do stuff**

## Functions
### User-defined functions
func **name**(**arguments\***) => **expression**  - creates a function
They can also be **anonymous**:
set **foo** = func(**a, b**) => **a+b**

### Built-in functions
#### Program functions
* Exit(**code**) - Exits program with error code.
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