# BITS
Coding done as a part of BITS MTech in Data Science Programme - Data Structures and Algorithms Design
Assignment 1 – PS10 - [Dosa Plaza]

## Problem Statement
Alexa owns a Dosa Plaza and she manages it in her own way. While in a normal plaza, a customer is served by following the first-come, first-served rule, Alexa simply minimizes the average waiting time of her customers by deciding who is served first, regardless of how sooner or later a person comes.
Different kinds of dosas take different amounts of baking time. Also, once she starts baking a dosa, she cannot bake another dosa until the first dosa is completely baked. Let's say we have three customers who come at time t=0, t=1, & t=2 respectively, and the time needed to bake their dosa is 3, 9, & 6 respectively. If Alexa applies a first-come, first-served rule, then the waiting time of three customers is 3, 11, & 16 respectively.

The average waiting time in this case is (3 + 11 + 16) / 3 = 10. This is not an optimized solution.
After serving the first customer at time t=3, Alexa can choose to serve the third customer. In that case, the waiting time will be 3, 7, & 17 respectively.
In this case, the average waiting time is (3 + 7 + 17) / 3 = 9.
Help Alexa achieve the minimum average waiting time. For the sake of simplicity, just find the integer part of the minimum average waiting time.
### Requirements
1. Implement the above problem statement as a Heap using linked list implementation in Python 3.7
2. Read the input from a file inputPS10.txt
First Come First Serve
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
Waiting time
Dosa 1
C0
3-0=3
Dosa 2
C1
12-1=11
Dosa 3
C2
18-2=16
Min. Avg. waiting time
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
Waiting time
Dosa 1
C0
3-0=3
Dosa 2
C1
18-1=17
Dosa 3
C2
9-2=7
3. You will output your answers to a file outputPS10.txt
4. Perform an analysis for the features above and give the running time in terms of input size: n.
### Input Format
• The first line contains an integer N, which is the number of customers.
• In the next N lines, the ith line contains two space separated numbers Ti and Li. Ti is the time
when ith customer order a dosa, and Li is the time required to bake that dosa.
• The ith customer is not the customer arriving at the ith arrival time.
3 03 19 26
### Output Format
• Display the integer part of the minimum average waiting time.
• Display the order in which the customer is served.
Min average waiting time: 9
Dosas served in the following order: Customer 0, Customer 2, Customer 1
Note that the input/output data shown here is only for understanding and testing, the actual file used for evaluation will be different.
Constraints
• 1 ≤ N ≤ 105
• 0 ≤ Ti ≤ 109
• 1 ≤ Li ≤ 109
Note
• The waiting time is calculated as the difference between the time a customer orders dosa (the time at which they enter the shop) and the time she is served.
• The cook does not know about the future orders, he is only told which dosa to cook next.

## 2. Deliverables
1. Word document designPS10_<group id>.docx detailing your design and time complexity of the algorithm.
2. [Group id]_Contribution.xlsx mentioning the contribution of each student in terms of percentage of work done. Download the Contribution.xlsx template from the link shared in the Assignment Announcement.
3. inputPS10.txt file used for testing
4. outputPS10.txt file generated while testing
5. .py file containing the python code. Create a single *.py file for code. Do not fragment your
code into multiple files
Zip all of the above files including the design document and contribution file in a folder with the name:
[Group id]_A1_PS10_DosaPlaza.zip and submit the zipped file.
Group Id should be given as Gxxx where xxx is your group number. For example, if your group
is 26, then you will enter G026 as your group id.
## 3. Instructions
1. It is compulsory to make use of the data structure(s) / algorithms mentioned in the problem statement.
2. Ensure that all data structure insert and delete operations throw appropriate messages when their capacity is empty or full. Also ensure basic error handling is implemented.
3. For the purposes of testing, you may implement some functions to print the data structures or other test data. But all such functions must be commented before submission.
4. Make sure that your read, understand, and follow all the instructions
5. Ensure that the input, prompt and output file guidelines are adhered to. Deviations from the
mentioned formats will not be entertained.
6. The input, prompt and output samples shown here are only a representation of the syntax to
be used. Actual files used to evaluate the submissions will be different. Hence, do not hard
code any values into the code.
7. Run time analysis is to be provided in asymptotic notations and not timestamp based runtimes
in sec or milliseconds.
8. Please note that the design document must include
a. The data structure model you chose with justifications
b. Details of each operations with the time complexity and reasons why the chosen
operations are efficient for the given representation
c. One alternate way of modelling the problem with the cost implications.
9. Writing good technical report and well document code is an art. Your report cannot exceed 4
pages. Your code must be modular and quite well documented.

### Instructions for use of Python:
1. Implement the above problem statement using Python 3.7.
2. Use only native data types like lists and tuples in Python, do not use dictionaries provided in
Python. Use of external libraries like graph, numpy, pandas library etc. is not allowed. The purpose of the assignment is for you to learn how these data structures are constructed and how they work internally.
3. Create a single *.py file for code. Do not fragment your code into multiple files.
4. Do not submit a Jupyter Notebook (no *.ipynb). These submissions will not be evaluated.
5. Read the input file and create the output file in the root folder itself along with your .py file. Do
not create separate folders for input and output files.
## 4. Deadline
1. The strict deadline for submission of the assignment is Wednesday, 22nd Dec, 2021.
2. The deadline has been set considering extra days from the regular duration in order to
accommodate any challenges you might face. No further extensions will be entertained.
3. Late submissions will not be evaluated.
## 5. How to submit
1. This is a group assignment.
2. Each group has to make one submission (only one, no resubmission) of solutions.
3. Each group should zip all the deliverables in one zip file and name the zipped file as mentioned
above.
4. Assignments should be submitted via Canvas > Assignment section. Assignment submitted
via other means like email etc. will not be graded.
## 6. Evaluation
1. The assignment carries 12 Marks.
2. Grading will depend on
a. Fully executable code with all functionality working as expected
b. Well-structured and commented code
c. Accuracy of the run time analysis and design document.
3. Every bug in the functionality will have negative marking.
4. Marks will be deducted if your program fails to read the input file used for evaluation due to
change / deviation from the required syntax.

5. Use of only native data types and avoiding libraries like numpy, graph and pandas will get additional marks.
6. Plagiarism will not be tolerated. Copy / Paste’s from web resources / or your friends’ submission will attract severe penalty to the extent of awarding 0 marks. We will not measure the extent of such blatant copy pastes and details of who copied from whom and such details while awarding the penalties. It’s the responsibility of the team to solve and protect your original work.
7. Source code files which contain compilation errors will get at most 25% of the value of that question.
## 7. Readings
Text book: Algorithms Design: Foundations, Analysis and Internet Examples Michael T. Goodrich, Roberto Tamassia, 2006, Wiley (Students Edition). Chapters: 2.4
