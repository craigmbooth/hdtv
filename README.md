Hierarchical Dictionary Tree View
=================================

I spend far too long working with nested dictionaries.  


The shortest Intro.
-------------------

Look at this.  You can look at stuff in dictionaries


    d = {"a": 1, "b": {"c": 2, "d": "aaa", "d2": (3, 4), "e": {1: [1, 2, 3]}}}
    import hdtv; hdtv.view(d)
    
A longer intro
----------------

I haven't found a good way yet to explore their structure.  Sure, for simple things ``pprint.pprint(dictionary)`` makes things readable, but the moment you insert a large list or DataFrame in there it becomes unusable.  What I really wanted was the equivalent of a line I could stick into Python code, similar to ``import pdb; pdb.set_trace()`` that would let me stop and inspect the contents of a deeply nested set of dictionaries.  This is a little GUI application to do just that.



Features that I want

   * I want to see an arbitrarily nested dictionary's keys in a tree
   * In a nested dictionary, I want to be able to collapse and expand keys.
   * For a value in a dictionary, I want to see a summary of the value, which for some things is just the value, but if the value is too large, a summary.
   * I want to explore deeply nested dictionaries
   * I want for circular references not to be an issue while browsing a circularly referenced dictionary
   * I want to deal gracefully with the objects I see every day, and be extensible to others
   * I want to be able to get at this thing with just a single line of code.
    
