# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both _lists_ and _tuples_ are sequences of values of any type separated by commas. Both can be compared using relational operations like <, >. Syntactically _lists_ are enclosed with square brackets while _tuples_ are optionally enclosed in parentheses. Another difference is that _lists_ are mutable, as in their elements can be reassigned, whereas _tuples_ are immutable. We use _tuples_ as keys in dictionaries. Dictionaries use hash values to store and look up key-value pairs. Therefore keys have to be hashable and _lists_ won't work as keys since they are mutable. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> An element can only appear once in a _set_ as opposed to a _list_. We can be more succinct with _sets_. For example to find duplicates you can use sets since all elements of a _set_ are unique: if len(set(x)) is different than len(x) then there are duplicates in x. Performance with _sets_ are faster since an operation on an element is done only once.


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The _lambda operator_ is an anonymous function created at runtime. It is useful and more compact to use lambdas instead of defining functions when we are using a simple function only once. This small function can be used as an argument as seen in this example:  
  
cities = [('NYC', 'NY', '8.6'), ('LA', 'CA', '3.9'), ('DC', 'DC', '.7'), ('SF', 'CA', '.9')]  
sorted(cities, key=lambda population: population[2])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List Comprehension is a syntactic tool to create lists in one line as opposed to using something like like _for_ loops. It is made of brackets that contain an expression with a _for_ clause after it and an optional condition. For example to get doubles of multiples of four we can have:  
  
nums = {0,5,8,14,18,20,213}  
double_fours = [2 * x for x in nums if x % 4 == 0]  
  
Since Python allows line breaks with brackets/braces, double_fours can be rewritten to be more readable as:  
  
double_fours = [  
	2 * x   
	for x in nums   
	if x % 4 == 0  
]  
  
The equivalent with map and filter:  
  
map(lambda x: 2 * x, filter(lambda x: x % 4 == 0, nums))  
  
As for with dictionary comprehension, the syntax is similar:  
  
{x: 2 * x for x in nums if x % 4 == 0}  

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





