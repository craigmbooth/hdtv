Heirarchical Dictionary Tree View
=================================

I spend far too long working with nested dictionaries.  I haven't found a good way yet to explore their structure.  Sure, for simple things ``pprint.pprint(dictionary)`` makes things readable, but the moment you insert a large list or DataFrame in there it becomes unusable.  What I really wanted was the equivalent of a line I could stick into Python code, similar to ``import pdb; pdb.set_trace()`` that would let me stop and inspect the contents of a deeply nested set of dictionaries.  This is a little GUI application to do just that.


    d = {"a": 1, "b": {"c": 2, "d": "aaa", "d2": (3, 4), "e": {1: [1, 2, 3]}}}
    import hdtv; hdtv.view(d)
