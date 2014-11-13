nameparts
=========
[![Build Status](https://secure.travis-ci.org/polera/nameparts.png)](http://travis-ci.org/polera/nameparts)

nameparts is a Python module that I wrote to address a problem splitting full names into individual
parts (first, middle, last, etc.)

You can use it like this:

      >>> from nameparts import Name
      >>> n = Name("Thurston Howel III")
      >>> n.first_name
      'Thurston'
      >>> n.last_name
      'Howel'
      >>> n.as_dict
      {'first_name': 'Thurston', 'last_name': 'Howel', \
        'middle_name': None, 'suffix': None, 'generation': 'III', \
        'salutation': None}
      >>> n = Name("Smith, John Paul")
      >>> n.first_name
      'John'
      >>> n.last_name
      'Smith'
      >>> n.middle_name
      'Paul'
      
If you suspect you may see more than one name in a given field (i.e. separated by a/k/a) you can use MultiName:

      >>> from nameparts import MultiName
      >>> names = MultiName("Bruce Wayne a/k/a Batman")
      >>> names
      [<Name: 'Bruce Wayne'>, <Name: 'Batman'>]
      >>> [n.as_dict for n in names]
      [{'last_name': 'Wayne', 'salutation': None, 'first_name': 'Bruce', 'suffix': None, 'generation': None, 'middle_name': None, 'aliases': None}, 
       {'last_name': '', 'salutation': None, 'first_name': 'Batman', 'suffix': None, 'generation': None, 'middle_name': None, 'aliases': None}]
       
MultiName automatically uses the string 'a/k/a' to split names, but you can provide an optional splitter argument to 
override that:

      >>> from nameparts import MultiName
      >>> names = MultiName("Tony Stark | Ironman | Stark, Tony", splitter="|")
      >>> names
      [<Name: 'Tony Stark'>, <Name: 'Ironman'>, <Name: 'Tony Stark'>]

Installing
----------
From source:

       python setup.py install

via pip:

       pip install nameparts

nameparts runs on CPython 2.6, 2.7, 3.2 and PyPy

License
-------
nameparts is released under the BSD license.

Comments/Questions/Improvements
-------------------------------
Any of the above are welcome.  Contact me at the email address in my profile.
