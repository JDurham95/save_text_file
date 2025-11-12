
# Write-Read-Append Microservice

## Microservice Description
The microservice will write, append, or read from text files depending on the given action.  The microservice reads 
from *file-service.txt* and obtains the users choice of action. The first line of *file-service.txt* will always be 
the users choice of action. Actions can be "a" for append, "w" for write, or "r" for read.  The second line in 
"file-service.txt" will always be the name of the file to write, read, or append.  For only the write and read action, 
the third line of *file-service.txt* will be the text to write or append. If the read action is used, the microservice
will read the text from the file of the given name and then write that text into *file-service.txt* so that it is 
available for the user. 

## UML Sequence Diagrams 
![MS2 UML Read Diagram.png](UML%20Diagrams/MS2%20UML%20Read%20Diagram.png)

![MS2 UML Append Diagram.png](UML%20Diagrams/MS2%20UML%20Append%20Diagram.png)

![MS2 UML Write Diagram.png](UML%20Diagrams/MS2%20UML%20Write%20Diagram.png)

## Communication Contract

### Parameters and Returns
**All Communication to and from the microservice is done through the "file-service.txt" in the Text Files directory**
* Request file: Text Files/file-service.txt 
* Response file: Text Files/file-service.txt 

**Request Parameter written to *file-service.txt*:**
* action: string action to be taken by the microservice 
* file name: string name of the text file the action is to be taken on
* text (optional): string text that is included if the user is using the *write* or *append* actions

**Parameter Requirements for action:**
* Written to the first line of *service-file.txt* 

**Parameter Requirements for file_name:**
* Written to the second line of *file-service.txt*
* Does not have to include *.txt* file extension. The microservice will append *.txt* if it is not present in the name

**Parameter Requirements for text:**
* Written to the third line of *file-service.txt*

**Return Value**
* read_text: if the *read* action is chosen by the user, the microservice will return the read text as a string in 
*  *file-service.txt* .
* If the user chose the *write* or *append* actions then nothing is returned. 

**Return Value Requirements**
* Read from the first line of *file-service.txt*

### Requesting read action from the microservice 

The requesting program will write "r" into the first line of *file-service.txt*, which is located in "Text Files"
directory. The requesting program will write the name of the file to be read into the second line of *file-service.txt*.
If the file to be read in the "Text Files" directory then the file name given written into line 2 of *file-service.txt*
needs to follow this format: "./Text Files/file_to_read.txt". It is optional for the user to use the *.txt* in the name
of the file to be read. If the extension is not included, then the microservice will append the file extension to the
name. The user will run *save_text_file.py* . The requesting program will wait while the microservice reads from the
file of the given name and writes that files contents into *file-service.txt*. The requesting program will read from
*file-service.txt* to get the contents of the read file and make it accessible to the user.

#### Example read action request with Python
```doctest
    import time
    
    service_file = "../Text Files/file-service.txt"

    action = "r"
    file_to_read = "./Text Files/test_read.txt"

    with open(service_file, "w") as f:
        f.write(action + "\n" + file_to_read)

    time.sleep(5)

    with open(service_file, "r") as f:
        content = f.readlines()

    print(content)
```

### Requesting append action from the microservice 
The requesting program will write the "a" into the first line of *file-service.txt*, which is located in the "Text
Files" directory. The requesting program will write the name of the file to be appended in the second line of
*file-service.txt*. If the file to be appended is in the "Text Files" then the file name format should be as follows:
"Text Files/file_to_append.txt". It is optional for the user to use the *.txt* in the name of the file to be appended. If the 
extension is not included, then the microservice will append the file extension to the name. The requesting program will
write the text to be appended into the third line of *file-service.txt*. The user will run *save_text_file.py*. The 
microservice will read from *file-service.txt* and append the third line text into the file name given in the second 
line. No new lines will be added by the microservice when appending so it is up to the user to include the appropriate 
"\n" characters to their preference. With the append action, the microservice will not return anything to the requesting 
program.  


#### Example append action request with Python

```doctest
    service_file = "../Text Files/file-service.txt"

    action = "a"
    file_to_append = "Text Files/test_append.txt"
    text_to_append = "enter text to append here "

    with open(service_file, "w") as f:
        f.write(action + "\n" + file_to_append + "\n" + text_to_append)
```

### Requesting write action from the microservice

The requesting program will write "w" into the first line of *file-service.txt* which is located in the "Text Files"
directory. The requesting program will write the name of the file to be written in to the second line of
*file-service.txt*. If the text file is to be written into the "Text Files directory then the file name needs to follow
this format: "Text Files/file_to_write.txt" It is optional for the user to use the *.txt* in the name of the file to be
written. If the extension is not included, then the microservice will append the file extension to the name. If a text
file with the given name already exists in the "Text Files" directory then its contents will be overwritten, otherwise a
new text file of the given name will be created. The requesting program will write the text to be written into the third
line of*file-service.txt*. The user will run *save_text_file.py*. The microservice will read the information from
*file-service.txt* and write (or over-write) the text file of the given name, with the contents of line 3 from
*file-service.txt*. All contents will be automatically written into the first line of the file be written into, so it
up to the user to add appropriate "\n" characters as needed. With the append action, the microservice will not return
anything to the requesting program.

#### Example write action request from the microservice 
```doctest

    service_file = "../Text Files/file-service.txt"

    action = "w"
    saved_file_name = "Text Files/test_write.txt"
    saved_file_text = "Input text to save in test_write.txt here"

    with open(service_file, "w") as f:
        f.write(action + "\n" + saved_file_name + "\n" + saved_file_text)
```

### Receiving the read contents from the read request 
The requesting program will wait at least one second after the request was made so that the microservice has time to
open the file of the given name and copy its contents into *file-service.txt*. The requesting program will be able to 
access the received data by reading from  *file-service.txt* which is located in the "Text Files" directory.


#### Example of receiving the data obtained by the read action in Python 

```doctest
    import time
    
    service_file = "../Text Files/file-service.txt"

    action = "r"
    file_to_read = "./Text Files/test_read.txt"

    with open(service_file, "w") as f:
        f.write(action + "\n" + file_to_read)

    time.sleep(5)

    with open(service_file, "r") as f:
        content = f.readlines()

    print(content)
```

