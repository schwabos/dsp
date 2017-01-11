# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
history x - seeing the last x commands i used  
pwd - the full path of the current directory i'm in   
man [command] - info about the command   
top - shows everything going on with the computer  
clear - scrolls the screen up to clear what's being displayed  
q or control-Z - back to command line  
cal - displays calendar of that month  
say [string] - converts the text to speech  
screencapture [file name] - takes a screenshot and assigns file name  
grep [string] [file name] - search file for all instances of the string  
head [file name] - display the first 10ish lines of the file  

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
ls		lists directory contents of files and directories  
ls -a	All files  
ls -l	Long format listing  
ls -lh	Long format with readable file size  
ls -lah Long format with readable file size including entries starting with '.'  
ls -t	Newest files first (based on timestamp)  
ls -Glp Long format, suppressing group information, adding a '/' after each directory  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
ls -1	Displays each entry on a line.  
ls -m	Displays the names as a comma-separated list.  
ls -d	Displays only directories.  
ls -R	Displays subdirectories as well.  
ls -u	Displays files by the file access time.  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs repeat what you type with the command 'control -d'. You can control how many strings, x, appear on each line with 'xargs -n x'. I'm not totally sure the appropriate or suggested use of 'xargs'. I suppose it can be useful to break a long sentence or paragraph into x number of words per line to examine it, in a more orderly fashion. 
