"""
File handling:- used to store data permanently in memory
operation on file:
1. open a file ==> f1 = open('abc.txt'), f1 is file pointer 
2. read/write
3. close a file ==> closes file and make sure that the changes in file has been properly saved 

==> with statement:- used to close the file, reducing risk of file corruption and resource leakage.

File Mode:-
1. r = read mode
2. w = write mode, if not exist then create it, and already existing text in the file gets over written with the new text
3. x = open file exclusive creation
4. a = open file in appending mode at the end of file without truncation, else create a new file if does not exist
5. b = binary mode
6. + = file opened for updating 


File Exception Handling:- python provides four main keywords for handling exceptions such as:
try:
      # Code 
except SomeException:
      # Code 
else:
     # Code 
finally:
    # Code 

here,
1. try: Runs the risky code that might cause an error.
2. except: Catches and handles the error if one occurs.
3. else: Executes only if no exception occurs in try.
4. finally: Runs regardless of what happens useful for cleanup tasks like closing files.

"""

try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")




"""
CSV(Comma Seperated Files):- file format is the most common import and export format for spreadsheets and databases.
-> use of data frames(lib easy to store and transport data) to import csv files in python, use of pandas
1. head() = used to show first 5 rows
2. tails() = used to show last 5 rows 
3. shape() = no of rows, columns
4. columns() = used to show columns name


csv reader() ==> python function used to read data from csv file row by row, result provided in csv format only.
csv DictReader() ==> you can access data by index, here header is used as key autom., we can even use it for validation


Data frames:- to store data in tabular form, used in pandas, can store diff types of data.
1. manually:- data placed in manually 
2. imported csv files used
3. data can be read by loacting to a particular path also

in-built functions:-
1. df.head()
2. df.tail()
3. df.columns => df.particularcolumnname  or/ df[['columnname1','columnname2']]
4. df.size
5. df.dtypes
6. df.values
7. df.index => (start,stop,step)index shown
ex.
   df.loc[], df.iloc[]        # shows row by index value

# PEP 305(CSV file API) ==> defines an API for reading and writing CSV files. It is accompanied by a corresponding module which implements the API.
"""



"""
Json:- Java Script object notation, seamless integration with js, lightweight file(easy to read)
key value pairs, easy to parse

JSON.parse(myJson)
After parsing the json file we can easily access the contents inside the files 
parse(conversion of json data to python, raw data-> understand its structure-> break/ access its components->python working with it)
==> parsing is done as:
parsed = JSON.parse(myJson);
parsed["myObj]["shopItem2"][2]["a"]      # this is to access a value
"""




"""
Validating external Input Data:- checking whether that incoming data is in the correct format, type, range, and structure before your program uses it.

Types of validation:
1. simple user validation:- validating before using it as number
2. Type validation:- isinstance() used: check if value belongs to a particular type
3. Range Validation:- checking for valid range, ex marks
4. String Validation:- ex. username can not be empty, strip() used to remove space from begning and end.
5. Validating JSON data:- first loading data then parsing json data and then validating json data(check req fields, check types, check value/range, accept/reject).

Data processing pipeline ==> includes reading structured files, parsing datasets, validating external input.
"""


"""
Catching Exception:-
1. specific exceptions: makes code to respond to different exception types differently. Makes code safer and easier to debug.
2. multiple exceptions: catch multiple exceptions in a signle block if we need to handle them in same way.
3. catch all handlers and their risk
4. raise an exception: use of raise keyword to raise an exception.

Exception diff types:
1. ZeroDivisionError
2. NameError 
3. TypeError
Standard exception names are built-in identifiers (not reserved keywords).


-> try-except
-> catching a specific exception
-> multiple exceptions
-> try-except-else
-> try-except-finally
-> using with ==> finally(closing stmnt) not req
-> catching the exception object
-> raise used to create your own exception
-> custom exception creating own exception class
-> exception handling with json
"""

"""
debug:- 
1. console
2. api
3. browser devl tools


spark = used to read large csv files


cli 
- create file-based tool module in util
- create app using cli for util modules
"""