# CSC226 Final Project

## Instructions

Exclamation Marks indicate action items; you should remove these emoji as you complete/update the items which 
  they accompany. (This means that your final README should have no ❗️in it!)

**Author(s)**: Besher Kitaz

**Google Doc Link**: https://docs.google.com/document/d/1ww0ajH0ahH8wBKCp3uY6fe_THjE8BJZ_3iYgnOO8ovg/edit?tab=t.0#heading=h.qg98s23ap4mh

---

## References 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update as you go.

https://chatgpt.com/share/6751289c-9bc0-8007-b8de-4d4a6f444842
https://chatgpt.com/share/675abf08-0a00-8007-a85f-7f71731440e6  
https://chatgpt.com/share/675abf31-9958-8007-b3e8-ca73e45ddd0d
https://chatgpt.com/share/675abf44-5140-8007-8a86-09035ae0249c
https://chatgpt.com/share/675abf59-5dc4-8007-be13-86767bc921b7
https://www.sqlite.org/docs.html
---

## Milestone 1:

`Berea Registration System`

`Use a web interface to sign up for courses, backed with Flask framework`

`
    - Dictionaries (RQ12)
    - Classes and Objects (RQ14)
    - Lists (RQ10)
    - Selection (RQ7)
    - Iteration (RQ8)
    - Functions (RQ5 and RQ4)
`


![crc.png](image%2Fcrc.png)

```
    Branch 1 name: kitazb
    Branch 2 name: kitazb_working_on_testing
    Branch 3 name: CRN_reference_page
```
---

## Milestone 2: 

```
    I did a lot of work in the database handling, and tests. I was a little behind, but I made it up in the next
    weeks. I am worried about the tests and how to integrate them with the database. I am hopeful that I will be 
    able to handle the many to many relationship model in a good way, and also handle the requests and responses 
    accordingly. 
```

---

## Milestone 3: Virtual Check-In

The project is now `70%` Complete

**Confidence**:

```
I feel really confident. Most of the tasks are done, and I only need to clean the code, and add a few 
things for the request and response handling, along with some testing. 
```

---

## Milestone 4: Final Code, Presentation, Demo

Program description:

It is a registration system, where you select your name, as a student, to open your page, view your current
courses (if any), and to add new courses. After you add a course through the crn (which you should find
in the database), you should also type your PIN, which you will get from your professor. Once done and everything
is correct, the course will be added to the database and you will receive a confirmation page.


Why did I choose this as the final project? 

I selected this project as I was a interested in web development, and I found it a way to learn more
about CURD operations between the request-response cycle and databases. The initial design was similar
to the final. However, there has been a lot of changes, especially in testing methods. 

As I progressed in the project, I learned many things about databases, Flask, and many-to-many relationships. It was
definitly challenging to link the tables together, and also to test the bases without affecting the rows.
This was the hardest part in the design. 

Next time, I will start working on the connection side (Flask) before the database, to ensure that my design
is sending and receiving the correct data so it does not affect the database badly.