<h1>Google Sentence auto complete project</h1>
<h3>By Yinon Tzomi, Amit Ein-Dor, Orel Aviad</h3>


<h1>Description</h1>
<p>
A program that provides an auto complete for an input by the user.</p>
<p>
The sentence suggestions are selected out of a directory of multiple files,
that can be divided into sub directories.
</p>
<p>
The program presents the 5 top suggestions, based on a score that calculated how 
similar the real sentence from the user's input.
</p>
<p>
The project was planned and mentored by Google employees.
</p>

<h1>The Algorithm</h1>
<h3> The program has two parts: </h3>
<h4>Offline</h4>
<p>The program reads the Archive and saves it in two data structure.<br>
The first data structure is a list of all sentences (and their details like row number and file name).<br>
The second data structure is a dictionary of word and the row numbers that containing this word.<br>
It means that the key is a string and the value is a set.<br>
The offline starts with output of: "Load files".</p>

<h4>Online</h3>
<p>
Now you need to see "Please insert your input..." on your terminal. <br>
When the user inserts some input, the program splits it to words. For each word
the program checks if the word exists in the dictionary of the words,
if so, the program takes the relevant lines from the dictionary
and makes the intersection of all the lines containing
all the words from the user input.<br>
If there is one mistake, the program will try to fix it. 
Then, the program will go over the lines from the intersection and tries to find
the complete user input in the lines.</p>

<h1>Space & Time complexity</h1>
<p>
The offline part goes over the Archive and saves each word 2 times, so it takes o(w) space and o(n) Time.
Where w is the number of words and n is the number of lines. <br>
The online part goes over the user input,
and for each word makes intersection for all the lines that containing this word.
Each intersection runs in O(min(old set, new set)) where old set is the intersections of all the lines until now,
and new set is the lines that containing the new word.
So it takes o(n(min(old set, new set))) where n is the length of the user input.
</p>

<h1>Execution</h1>
<ol>
<li>Run the main.py file using regular configuration.</li>
<li>Wait to message "Please insert your input..."</li>
<li>insert your input.</li>
<li>If you want to finish, type "finish".</li>
</ol>

<h1>Examples</h1>
<ol>
<li>
Load files...
Please insert your input...
</li>
<li>input: "understanding of how Kubernetes"<br>
    output: "0. understanding of how Kubernetes works. (Concepts 8)"<br> 
</li>
<li>input: "understanding of how Kubrnetes"<br> 
    output: "0. understanding of how Kubernetes works. (Concepts 8)"<br> 
</li>
<li> input: "understanding of how Kubernetegs"<br> 
     output: "0. understanding of how Kubernetes works. (Concepts 8)"<br> 
</li>
<li>
 input: "finish" <br>
 output: "by" <br>
</li>
</ol>