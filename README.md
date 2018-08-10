[![Build Status](https://travis-ci.com/agupta231/Python-Word-Definer.svg?branch=master)](https://travis-ci.com/agupta231/Python-Word-Definer)

# Python Word Definer
A super simple script that takes in a text file of words and outputs a file of the word and the
definition. This script is easily expandable and the configurable delimiters make it ideal for
services such as Quizlet. 

This script was built to help out my brother, who is currently studying for a test that requires him
to memorize a large quantity of words.

# Execution Directions
This script relies on the 3rd party API [Oxford Dictionaries](oxforddictionaries.com). It's a free
API, and not half bad.

First, create an account and get your private and public key. In `script.py`, replace the `app_id`
with your public key and the `app_secret` with your private key.

Afterwards, there are two main ways to actually run the script.

## Through Docker
This is definitely the recommended and easiest way to run this program. Firstly, create the docker
image by running `docker build -t agupta231/python-word-def .`. Then, every time you want to run the
program, (even if you edit the code or `words.txt`), simply run `docker run -v $(pwd):/app
agupta231/python-word-def`.

## Running it locally 
I'd recommend using a virtual environment like anaconda to somewhat isolate your environment. Follow
[these instructions](https://gist.github.com/agupta231/ae93aa5d7130500fbbf7910041a2bc59) to get set
up.

# A word about the 6 nested for loop and repeated single API calls
Listen up bud. I wrote this script in a total of 15 minutes, including the 5 minutes that it took me
to get the API keys. I know that if I had just done a batch call and data scrapped the output for
the word "definition", I could have done the whole thing in `O(n)` time. Or, I could have easily
parallelized the tasks so that I have multiple async requests going out to reduce the bottleneck
that are network calls.

You probably think that I'm an application-first, theory-second type of guy, or even a *shudder*
engineer. Well, give me the benefit of the doubt for like 90 seconds and let me defend my garbage
code:

1. I couldn't parallelize the code because the API that I was using doesn't allow for more than 1
call a second. You can actually see that put a time delay for this exact purpose... And I ain't
about to drop big bucks so that my brother can be even lazier: that's my thing.
2. At the current time of writing this code, the API didn't offer batch calls, so I was stuck doing
individual API calls for each word.
3. OK, the 6 for loops time. Let's address what is constant first. Regardless of how this program is
written, you have to iterate through the `n` words. Now, you can argue that instead of using the 6
for loops, you could data scrape the returned string and only look for the keyword "definition".
That is all good and dandy, and will take `Θ(l)` times, where `l` is the average number of lines
returned in the JSON string. Thus, the time complexity for that program will be a `Θ(n * l)`. 
Now, for my implementation. I am just iterating through the response, and I never access an element
more than once. Additionally, because I am accessing the elements through a dictionary (which works
based on hashes), the time to access is always constant. That means, that I only hit `Θ(m)`
elements, where m is the average number of definitions of words. That means the time complexity of
my program will be `Θ(n * m)` and as `m` < `l`, my will will be more efficient. *Psych!* I didn't
mention the time it takes to convert the JSON response into a Python dictionary. I'm gonna assume
that it is `Θ(l)`, and it is repeated for every word, which then means that my program's 
efficiency is `Θ(n * m + n * l) = Θ(n * (m + l))`. Damn, so close! However, this isn't a polynomial
difference than the optimal solution, and the fact that I spent the same amount of time writing this
explanation as I did writing the program makes me a happy camper.
4. The Try/Except... Alright, I got lazy, and if a word didn't play nice, I'd just catch the error
and tell my brother to stop watching youtube and look up the damn word.
