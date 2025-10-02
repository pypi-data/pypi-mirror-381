ERROR_KNOWLEDGE_BASE = {
    # ============================================================================
    # TYPE ERRORS
    # ============================================================================
    "TypeError: unsupported operand type(s)": {
        "explanation": "You're trying to perform an operation between incompatible types (e.g., adding a number and a string, or multiplying a string and a float).",
        "fix": "Convert one type to match the other. For example: str(number) + string or int(string) + number.",
        "example": "age = 25\nprint('Age: ' + str(age))  # Convert int to str\n# or\nresult = int('10') + 5  # Convert str to int"
    },
    
    "TypeError: 'NoneType' object": {
        "explanation": "You're trying to use a variable or function result that is None (null). This often happens when a function doesn't return anything or a variable wasn't initialized properly.",
        "fix": "Check if the value is None before using it, or ensure the function returns a value.",
        "example": "result = my_function()\nif result is not None:\n    result.method()\nelse:\n    print('Function returned None')"
    },
    
    "TypeError: object NoneType can't be used in 'await' expression": {
        "explanation": "You're using 'await' on a non-async function or a function that returns None. This commonly happens when mixing synchronous libraries (like requests) with async code.",
        "fix": "Use async-compatible libraries (e.g., aiohttp instead of requests) or ensure the function is async and returns an awaitable.",
        "example": "import aiohttp\n\nasync def fetch(url):\n    async with aiohttp.ClientSession() as session:\n        async with session.get(url) as resp:\n            return await resp.text()"
    },
    
    "TypeError: 'int' object is not callable": {
        "explanation": "You're trying to call a variable as if it were a function, but it's actually an integer. This often happens when you accidentally overwrite a function name with a variable.",
        "fix": "Check if you accidentally used parentheses on a variable, or if you overwrote a function name.",
        "example": "# Wrong: sum = 5; result = sum([1,2,3])\n# Right: total = 5; result = sum([1,2,3])"
    },
    
    "TypeError: 'str' object is not callable": {
        "explanation": "You're trying to call a string as if it were a function. You may have accidentally overwritten a function name with a string.",
        "fix": "Check variable names - you might have overwritten a built-in function or method name.",
        "example": "# Wrong: list = 'hello'; result = list([1,2,3])\n# Right: my_list = 'hello'; result = list([1,2,3])"
    },
    
    "TypeError: 'list' object is not callable": {
        "explanation": "You're trying to call a list as a function. You likely overwrote a function name with a list.",
        "fix": "Use a different variable name that doesn't conflict with function names.",
        "example": "# Wrong: dict = [1,2,3]; result = dict()\n# Right: my_list = [1,2,3]; result = dict()"
    },
    
    "TypeError: can only concatenate": {
        "explanation": "You're trying to concatenate (join) incompatible types. Strings can only be concatenated with other strings, lists with lists, etc.",
        "fix": "Convert the value to the correct type before concatenating.",
        "example": "name = 'Alice'\nage = 30\nprint(name + ' is ' + str(age))  # Convert int to str"
    },
    
    "TypeError: 'float' object cannot be interpreted as an integer": {
        "explanation": "You're using a float where an integer is required (e.g., in range(), list indexing, or string repetition).",
        "fix": "Convert the float to an integer using int().",
        "example": "x = 3.7\nfor i in range(int(x)):\n    print(i)"
    },
    
    "TypeError: argument of type 'NoneType' is not iterable": {
        "explanation": "You're trying to iterate over or check membership in None. A function likely returned None instead of a list/dict.",
        "fix": "Check that the variable is not None before iterating.",
        "example": "result = my_function()\nif result is not None:\n    for item in result:\n        print(item)"
    },
    
    "TypeError: 'type' object is not subscriptable": {
        "explanation": "You're trying to use square brackets on a type itself rather than an instance. Common with type hints in older Python versions.",
        "fix": "Use typing module for type hints, or create an instance of the type first.",
        "example": "from typing import List\n# Wrong: def func() -> list[int]\n# Right: def func() -> List[int]"
    },
    
    # ============================================================================
    # VALUE ERRORS
    # ============================================================================
    "ValueError: invalid literal for int()": {
        "explanation": "You're trying to convert a string to an integer, but the string doesn't contain a valid number.",
        "fix": "Validate the input before converting, or use try-except to handle invalid values.",
        "example": "user_input = input('Enter a number: ')\ntry:\n    num = int(user_input)\nexcept ValueError:\n    print('Please enter a valid number')"
    },
    
    "ValueError: not enough values to unpack": {
        "explanation": "You're trying to unpack a sequence into variables, but there aren't enough values in the sequence.",
        "fix": "Ensure the number of variables matches the number of values, or use * to capture remaining values.",
        "example": "# If tuple has 2 items:\na, b = my_tuple  # Not: a, b, c = my_tuple\n# Or use: a, b, *rest = my_tuple"
    },
    
    "ValueError: too many values to unpack": {
        "explanation": "You're trying to unpack a sequence into variables, but there are too many values in the sequence.",
        "fix": "Add more variables to capture all values, or use * to capture extras.",
        "example": "a, b, *rest = [1, 2, 3, 4, 5]  # rest = [3,4,5]"
    },
    
    "ValueError: substring not found": {
        "explanation": "You used str.index() to find a substring, but it doesn't exist in the string.",
        "fix": "Use str.find() which returns -1 if not found, or check with 'in' first.",
        "example": "text = 'hello world'\nif 'xyz' in text:\n    pos = text.index('xyz')\n# Or: pos = text.find('xyz')  # Returns -1 if not found"
    },
    
    "ValueError: math domain error": {
        "explanation": "You're performing a mathematical operation that's mathematically invalid (e.g., square root of negative number, log of zero).",
        "fix": "Check the input values before performing the operation.",
        "example": "import math\nx = -4\nif x >= 0:\n    result = math.sqrt(x)\nelse:\n    print('Cannot take square root of negative number')"
    },
    
    "ValueError: invalid literal for float()": {
        "explanation": "You're trying to convert a string to a float, but the string doesn't contain a valid number.",
        "fix": "Validate and clean the input string before converting.",
        "example": "try:\n    value = float(user_input.strip())\nexcept ValueError:\n    print('Invalid number format')"
    },
    
    "ValueError: empty range for randrange()": {
        "explanation": "You're calling random.randrange() with invalid arguments that result in an empty range.",
        "fix": "Ensure start < stop for randrange(start, stop).",
        "example": "import random\n# Wrong: random.randrange(10, 5)\n# Right: random.randrange(5, 10)"
    },
    
    # ============================================================================
    # KEY/ATTRIBUTE ERRORS
    # ============================================================================
    "KeyError": {
        "explanation": "You're trying to access a dictionary key that doesn't exist.",
        "fix": "Use .get() method with a default value, or check if the key exists with 'in' operator.",
        "example": "data = {'name': 'Alice', 'age': 30}\n# Safe:\nphone = data.get('phone', 'Not provided')\n# Or check first:\nif 'phone' in data:\n    phone = data['phone']"
    },
    
    "AttributeError": {
        "explanation": "You're trying to access an attribute or method that doesn't exist on the object.",
        "fix": "Check the object type and available methods/attributes using dir() or type(). Verify spelling and that the object is what you expect.",
        "example": "obj = 'hello'\nprint(type(obj))  # <class 'str'>\nprint(dir(obj))   # Shows all available methods\n# Use: obj.upper() not obj.Upper()"
    },
    
    "AttributeError: 'NoneType' object has no attribute": {
        "explanation": "You're trying to access an attribute/method on None. A function likely returned None instead of an object.",
        "fix": "Check if the value is None before accessing its attributes.",
        "example": "result = my_function()\nif result is not None:\n    value = result.attribute\nelse:\n    print('Function returned None')"
    },
    
    "AttributeError: module has no attribute": {
        "explanation": "You're trying to access something that doesn't exist in the module. Could be a typo or using the wrong import.",
        "fix": "Check the spelling, verify the module version, or check the correct import path.",
        "example": "# Wrong: from math import logarithm\n# Right: from math import log\n# Check: print(dir(math))"
    },
    
    "AttributeError: 'str' object has no attribute 'append'": {
        "explanation": "You're trying to use a list method on a string. Strings are immutable and don't have append().",
        "fix": "For strings, use concatenation or convert to a list first.",
        "example": "# Wrong: my_string.append('x')\n# Right: my_string += 'x'\n# Or: chars = list(my_string); chars.append('x')"
    },
    
    # ============================================================================
    # INDEX ERRORS
    # ============================================================================
    "IndexError: list index out of range": {
        "explanation": "You're trying to access a list element at an index that doesn't exist (the list is too short).",
        "fix": "Check the list length before accessing, or use try-except to handle the error.",
        "example": "my_list = [1, 2, 3]\nif len(my_list) > 5:\n    value = my_list[5]\nelse:\n    print(f'List only has {len(my_list)} items')"
    },
    
    "IndexError: string index out of range": {
        "explanation": "You're trying to access a character at an index that exceeds the string length.",
        "fix": "Check the string length before accessing.",
        "example": "text = 'hello'\nif len(text) > 10:\n    char = text[10]\nelse:\n    print(f'String only has {len(text)} characters')"
    },
    
    "IndexError: tuple index out of range": {
        "explanation": "You're trying to access a tuple element at an index that doesn't exist.",
        "fix": "Check the tuple length or use try-except.",
        "example": "my_tuple = (1, 2, 3)\ntry:\n    value = my_tuple[5]\nexcept IndexError:\n    print('Index too large')"
    },
    
    # ============================================================================
    # IMPORT ERRORS
    # ============================================================================
    "ImportError": {
        "explanation": "Python cannot find or import the module you're trying to use.",
        "fix": "Install the required package using pip, check the module name spelling, or verify the module is in your Python path.",
        "example": "# Install missing package:\npip install package_name\n# Or check spelling:\n# Wrong: import numpie\n# Right: import numpy"
    },
    
    "ModuleNotFoundError": {
        "explanation": "The module you're trying to import doesn't exist or isn't installed.",
        "fix": "Install the package using pip, check if you're in the right virtual environment, or verify the module name.",
        "example": "# Install: pip install requests\n# Check venv: pip list\n# Verify name: pip search package_name"
    },
    
    "ImportError: cannot import name": {
        "explanation": "The specific name you're trying to import doesn't exist in the module. Could be wrong name or outdated module version.",
        "fix": "Check the documentation for correct import names, or update the package.",
        "example": "# Check available names:\nimport module\nprint(dir(module))\n# Or update: pip install --upgrade package_name"
    },
    
    "ImportError: No module named": {
        "explanation": "Python can't find the module you're trying to import. It may not be installed or in the wrong directory.",
        "fix": "Install the module or check your PYTHONPATH.",
        "example": "pip install module_name\n# Or add to path:\nimport sys\nsys.path.append('/path/to/module')"
    },
    
    # ============================================================================
    # NAME ERRORS
    # ============================================================================
    "NameError: name '...' is not defined": {
        "explanation": "You're using a variable or function name that hasn't been defined yet, is out of scope, or has a typo.",
        "fix": "Define the variable before using it, check for typos, or ensure it's in the correct scope.",
        "example": "# Define first:\nmy_var = 10\nprint(my_var)\n# Not: print(my_var); my_var = 10"
    },
    
    "NameError: global name '...' is not defined": {
        "explanation": "You're trying to access a global variable that doesn't exist.",
        "fix": "Define the global variable or check the variable name.",
        "example": "# Define global:\nGLOBAL_VAR = 100\n\ndef func():\n    print(GLOBAL_VAR)"
    },
    
    # ============================================================================
    # INDENTATION ERRORS
    # ============================================================================
    "IndentationError": {
        "explanation": "Your code has inconsistent or incorrect indentation. Python requires consistent indentation (usually 4 spaces).",
        "fix": "Use consistent indentation throughout your code (all tabs or all spaces, preferably 4 spaces).",
        "example": "# Correct:\nif condition:\n    do_something()\n    do_another_thing()\nelse:\n    do_else()"
    },
    
    "IndentationError: expected an indented block": {
        "explanation": "Python expected indented code after a colon (:) but found none.",
        "fix": "Add indented code after if/for/while/def/class statements.",
        "example": "if x > 5:\n    print('Greater')  # Must be indented\n# Or use pass:\nif x > 5:\n    pass  # Placeholder"
    },
    
    "IndentationError: unindent does not match any outer indentation level": {
        "explanation": "Your indentation levels don't align properly. You might be mixing tabs and spaces.",
        "fix": "Use consistent indentation (4 spaces recommended). Convert all tabs to spaces.",
        "example": "# Configure your editor to use spaces\n# In VS Code: 'Convert Indentation to Spaces'"
    },
    
    # ============================================================================
    # SYNTAX ERRORS
    # ============================================================================
    "SyntaxError: invalid syntax": {
        "explanation": "Your code has a syntax error - something is written in a way Python doesn't understand.",
        "fix": "Check for missing colons, parentheses, quotes, or commas. Look at the line number indicated in the error.",
        "example": "# Wrong: if x == 5\n# Right: if x == 5:\n\n# Wrong: print 'hello'\n# Right: print('hello')"
    },
    
    "SyntaxError: EOL while scanning string literal": {
        "explanation": "You started a string but didn't close it with a matching quote before the line ended.",
        "fix": "Add the missing closing quote.",
        "example": "# Wrong: text = 'hello\n# Right: text = 'hello'\n# Or multiline:\ntext = '''hello\nworld'''"
    },
    
    "SyntaxError: unexpected EOF while parsing": {
        "explanation": "Python reached the end of the file but expected more code (unclosed brackets, parentheses, or blocks).",
        "fix": "Check for unclosed brackets (), [], {} or incomplete function/class definitions.",
        "example": "# Wrong:\nmy_list = [1, 2, 3\n# Right:\nmy_list = [1, 2, 3]"
    },
    
    "SyntaxError: invalid character": {
        "explanation": "Your code contains a character that Python doesn't recognize. Often from copying code from websites.",
        "fix": "Retype the problematic characters. Watch for smart quotes vs regular quotes.",
        "example": "# Wrong: print('hello')  # Smart quotes\n# Right: print('hello')  # Regular quotes"
    },
    
    "SyntaxError: positional argument follows keyword argument": {
        "explanation": "In a function call, you put a positional argument after a keyword argument, which is not allowed.",
        "fix": "Put all positional arguments before keyword arguments.",
        "example": "# Wrong: func(name='Alice', 30)\n# Right: func(30, name='Alice')\n# Or: func(age=30, name='Alice')"
    },
    
    "SyntaxError: keyword can't be an expression": {
        "explanation": "You're trying to use an expression as a keyword argument name.",
        "fix": "Keyword arguments must be simple names, not expressions.",
        "example": "# Wrong: func(**{'my-key': 'value'})\n# Right: func(my_key='value')\n# Or: func(**{'my_key': 'value'})"
    },
    
    # ============================================================================
    # FILE ERRORS
    # ============================================================================
    "FileNotFoundError": {
        "explanation": "Python cannot find the file you're trying to open or access.",
        "fix": "Check the file path is correct, the file exists, and you have permission to access it. Use absolute paths or verify relative paths.",
        "example": "import os\nfilepath = 'data.txt'\nif os.path.exists(filepath):\n    with open(filepath, 'r') as f:\n        content = f.read()\nelse:\n    print(f'File {filepath} not found')"
    },
    
    "FileNotFoundError: [Errno 2]": {
        "explanation": "The file or directory you're trying to access doesn't exist at the specified path.",
        "fix": "Use os.path.exists() to check first, or use absolute paths.",
        "example": "import os\nabspath = os.path.abspath('file.txt')\nprint(f'Looking for: {abspath}')\nif os.path.exists(abspath):\n    # File exists"
    },
    
    "PermissionError": {
        "explanation": "You don't have permission to access the file or directory.",
        "fix": "Check file permissions, run with appropriate privileges, or ensure the file isn't open in another program.",
        "example": "# Check permissions:\nimport os\nif os.access('file.txt', os.W_OK):\n    # File is writable\n    with open('file.txt', 'w') as f:\n        f.write('data')"
    },
    
    "IsADirectoryError": {
        "explanation": "You're trying to open a directory as if it were a file.",
        "fix": "Check if it's a directory first, or specify a file within the directory.",
        "example": "import os\npath = 'mydir'\nif os.path.isdir(path):\n    # It's a directory, list files\n    files = os.listdir(path)\nelse:\n    with open(path) as f:\n        content = f.read()"
    },
    
    "UnicodeDecodeError": {
        "explanation": "The file contains characters that can't be decoded with the current encoding.",
        "fix": "Specify the correct encoding or use 'utf-8' with error handling.",
        "example": "# Try UTF-8:\nwith open('file.txt', 'r', encoding='utf-8') as f:\n    content = f.read()\n# Or ignore errors:\nwith open('file.txt', 'r', errors='ignore') as f:\n    content = f.read()"
    },
    
    # ============================================================================
    # MATH/ARITHMETIC ERRORS
    # ============================================================================
    "ZeroDivisionError": {
        "explanation": "You're trying to divide a number by zero, which is mathematically undefined.",
        "fix": "Check if the divisor is zero before performing division.",
        "example": "divisor = 0\nif divisor != 0:\n    result = numerator / divisor\nelse:\n    print('Cannot divide by zero')\n    result = None"
    },
    
    "OverflowError": {
        "explanation": "The result of a calculation is too large to be represented.",
        "fix": "Use smaller numbers, or use the decimal module for precise calculations.",
        "example": "from decimal import Decimal\n# Instead of: result = 10 ** 10000\nresult = Decimal(10) ** 1000"
    },
    
    "FloatingPointError": {
        "explanation": "A floating-point operation failed (usually division by zero in special contexts).",
        "fix": "Check for zero divisors or use try-except.",
        "example": "import numpy as np\nnp.seterr(divide='ignore')  # Ignore division warnings"
    },
    
    # ============================================================================
    # RECURSION ERRORS
    # ============================================================================
    "RecursionError: maximum recursion depth exceeded": {
        "explanation": "Your recursive function is calling itself too many times without reaching a base case.",
        "fix": "Add or fix the base case in your recursive function, or consider using iteration instead.",
        "example": "def factorial(n):\n    if n <= 1:  # Base case!\n        return 1\n    return n * factorial(n - 1)\n\n# Or increase limit:\nimport sys\nsys.setrecursionlimit(10000)"
    },
    
    # ============================================================================
    # ASYNC/AWAIT ERRORS
    # ============================================================================
    "RuntimeError: This event loop is already running": {
        "explanation": "You're trying to run an event loop that's already running. This often happens in Jupyter notebooks or when nesting asyncio.run() calls.",
        "fix": "Use 'await' directly if already in an async context, or use nest_asyncio in Jupyter.",
        "example": "# In Jupyter:\nimport nest_asyncio\nnest_asyncio.apply()\nawait my_async_function()\n\n# Or in normal code:\nimport asyncio\nasyncio.run(my_async_function())"
    },
    
    "RuntimeError: cannot reuse already awaited coroutine": {
        "explanation": "You're trying to await the same coroutine object twice.",
        "fix": "Call the async function again to create a new coroutine.",
        "example": "# Wrong:\ncoro = my_async_func()\nawait coro\nawait coro  # Error!\n\n# Right:\nawait my_async_func()\nawait my_async_func()  # Creates new coroutine"
    },
    
    "SyntaxError: 'await' outside async function": {
        "explanation": "You're using 'await' in a regular function instead of an async function.",
        "fix": "Add 'async' keyword to the function definition.",
        "example": "# Wrong:\ndef my_func():\n    await something()\n\n# Right:\nasync def my_func():\n    await something()"
    },
    
    "TypeError: object ... can't be used in 'await' expression": {
        "explanation": "You're trying to await something that's not awaitable (not a coroutine, task, or future).",
        "fix": "Make sure you're awaiting an async function, not a regular function.",
        "example": "# Wrong:\nawait regular_function()\n\n# Right:\nawait async_function()\n\n# Or make it async:\nasync def async_function():\n    return 'result'"
    },
    
    # ============================================================================
    # ASSERTION ERRORS
    # ============================================================================
    "AssertionError": {
        "explanation": "An assert statement failed - the condition was False when it should have been True.",
        "fix": "Check why the condition is False. Assert is used for debugging assumptions.",
        "example": "x = 5\nassert x > 10, f'Expected x > 10, got {x}'\n# Better: Use if statements for user validation"
    },
    
    # ============================================================================
    # STOP ITERATION
    # ============================================================================
    "StopIteration": {
        "explanation": "An iterator has no more items. Usually this is caught internally, but can appear if you call next() manually.",
        "fix": "Use a for loop or check with a default value.",
        "example": "my_iter = iter([1, 2, 3])\n# Instead of: next(my_iter)\n# Use: next(my_iter, None)  # Returns None when done\n# Or: for item in my_iter:\n#         print(item)"
    },
    
    # ============================================================================
    # MEMORY ERRORS
    # ============================================================================
    "MemoryError": {
        "explanation": "Python ran out of memory trying to allocate space for your data.",
        "fix": "Process data in smaller chunks, use generators, or optimize your algorithm.",
        "example": "# Instead of loading everything:\n# data = [x**2 for x in range(10000000)]\n\n# Use generator:\ndata = (x**2 for x in range(10000000))\nfor item in data:\n    process(item)"
    },
    
    # ============================================================================
    # OS ERRORS
    # ============================================================================
    "OSError": {
        "explanation": "An operating system error occurred (file operations, network, etc.).",
        "fix": "Check file permissions, disk space, network connectivity, or system resources.",
        "example": "try:\n    with open('file.txt', 'w') as f:\n        f.write('data')\nexcept OSError as e:\n    print(f'OS error: {e}')"
    },
    
    "ConnectionError": {
        "explanation": "A network connection error occurred (connection refused, network unreachable, etc.).",
        "fix": "Check network connectivity, firewall settings, and that the server is running.",
        "example": "import requests\ntry:\n    response = requests.get(url, timeout=5)\nexcept requests.ConnectionError:\n    print('Cannot connect to server')"
    },
    
    "TimeoutError": {
        "explanation": "An operation timed out waiting for a response.",
        "fix": "Increase the timeout value or check network/server performance.",
        "example": "import requests\ntry:\n    r = requests.get(url, timeout=30)  # 30 seconds\nexcept requests.Timeout:\n    print('Request timed out')"
    },
    
    # ============================================================================
    # KEYBOARD INTERRUPT
    # ============================================================================
    "KeyboardInterrupt": {
        "explanation": "The user pressed Ctrl+C to stop the program.",
        "fix": "This is usually intentional. You can catch it to clean up resources.",
        "example": "try:\n    while True:\n        do_work()\nexcept KeyboardInterrupt:\n    print('\\nStopped by user')\n    cleanup_resources()"
    },
    
    # ============================================================================
    # ENCODING ERRORS
    # ============================================================================
    "UnicodeEncodeError": {
        "explanation": "Python can't encode a character with the specified encoding (e.g., ASCII can't encode emoji).",
        "fix": "Use UTF-8 encoding or handle errors with 'ignore' or 'replace'.",
        "example": "text = 'Hello 😊'\n# Wrong: text.encode('ascii')\n# Right: text.encode('utf-8')\n# Or: text.encode('ascii', errors='ignore')"
    },
    
    "UnicodeDecodeError": {
        "explanation": "The bytes can't be decoded with the specified encoding.",
        "fix": "Use the correct encoding (usually utf-8) or handle errors.",
        "example": "with open('file.txt', 'r', encoding='utf-8', errors='ignore') as f:\n    content = f.read()"
    },
    
    # ============================================================================
    # JSON ERRORS
    # ============================================================================
    "json.JSONDecodeError": {
        "explanation": "The JSON string is malformed and can't be parsed.",
        "fix": "Check the JSON format, look for missing quotes, commas, or brackets.",
        "example": "import json\ntry:\n    data = json.loads(json_string)\nexcept json.JSONDecodeError as e:\n    print(f'Invalid JSON at line {e.lineno}: {e.msg}')"
    },
    
    # ============================================================================
    # PICKLE ERRORS
    # ============================================================================
    "pickle.UnpicklingError": {
        "explanation": "The pickled data is corrupted or in the wrong format.",
        "fix": "Ensure the file is a valid pickle file and not corrupted.",
        "example": "import pickle\ntry:\n    with open('data.pkl', 'rb') as f:\n        data = pickle.load(f)\nexcept pickle.UnpicklingError:\n    print('Corrupted pickle file')"
    },
    
    # ============================================================================
    # ENVIRONMENT ERRORS
    # ============================================================================
    "EnvironmentError": {
        "explanation": "Base class for I/O related errors (now OSError in Python 3+).",
        "fix": "Check file paths, permissions, and system resources.",
        "example": "try:\n    operation()\nexcept EnvironmentError as e:\n    print(f'Environment error: {e}')"
    },
    
    # ============================================================================
    # REFERENCE ERRORS
    # ============================================================================
    "UnboundLocalError": {
        "explanation": "You're using a local variable before it's assigned a value. Often happens when you reference a global variable and then try to modify it locally.",
        "fix": "Use 'global' keyword for global variables, or assign the variable before using it.",
        "example": "count = 0\n\ndef increment():\n    global count  # Declare as global\n    count += 1\n\n# Or initialize first:\ndef func():\n    local_var = 0\n    local_var += 1"
    },
    
    # ============================================================================
    # LOOKUP ERRORS
    # ============================================================================
    "LookupError": {
        "explanation": "Base class for lookup errors (KeyError, IndexError inherit from this).",
        "fix": "Check that the key/index exists before accessing.",
        "example": "try:\n    value = data[key]\nexcept LookupError:\n    print('Key or index not found')"
    },
    
    # ============================================================================
    # RUNTIME ERRORS
    # ============================================================================
    "RuntimeError": {
        "explanation": "A generic runtime error that doesn't fit into other categories.",
        "fix": "Read the error message carefully for specific details.",
        "example": "# Context-specific, check error message\ntry:\n    risky_operation()\nexcept RuntimeError as e:\n    print(f'Runtime error: {e}')"
    },
    
    "NotImplementedError": {
        "explanation": "A method or function is defined but not implemented yet (often in abstract base classes).",
        "fix": "Implement the method, or use a different class that has it implemented.",
        "example": "class Base:\n    def method(self):\n        raise NotImplementedError('Subclass must implement')\n\nclass Child(Base):\n    def method(self):\n        return 'Implemented!'"
    },
    
    # ============================================================================
    # BUFFER ERRORS
    # ============================================================================
    "BufferError": {
        "explanation": "An operation on a buffer object failed.",
        "fix": "Ensure the buffer is not being used elsewhere when you try to modify it.",
        "example": "# Usually occurs with memoryview objects\nimport numpy as np\narr = np.array([1, 2, 3])\nmv = memoryview(arr)\n# Release memoryview before modifying array"
    },
    
    # ============================================================================
    # GENERATOR ERRORS
    # ============================================================================
    "GeneratorExit": {
        "explanation": "A generator or coroutine is being closed.",
        "fix": "This is usually intentional. Don't catch it unless you need cleanup.",
        "example": "def my_generator():\n    try:\n        yield 1\n        yield 2\n    except GeneratorExit:\n        print('Generator closing')\n        # Cleanup code here"
    },
    
    # ============================================================================
    # SYSTEM ERRORS
    # ============================================================================
    "SystemError": {
        "explanation": "Internal Python error. This is rare and might indicate a bug in Python or a C extension.",
        "fix": "Report to package maintainers or Python developers. Try updating Python or the library.",
        "example": "# This is rare - usually a bug\n# Update Python: python -m pip install --upgrade pip\n# Update packages: pip install --upgrade package_name"
    },
    
    "SystemExit": {
        "explanation": "The sys.exit() function was called to exit the program.",
        "fix": "This is usually intentional. Don't catch it unless you need to prevent exit.",
        "example": "import sys\ntry:\n    sys.exit(0)\nexcept SystemExit:\n    print('Program tried to exit')\n    # Cleanup or prevent exit"
    },
    
    # ============================================================================
    # WARNING CATEGORIES (not exceptions but related)
    # ============================================================================
    "DeprecationWarning": {
        "explanation": "You're using a feature that's deprecated and will be removed in future versions.",
        "fix": "Update your code to use the new recommended approach.",
        "example": "# Check documentation for replacement\n# Use warnings to see details:\nimport warnings\nwarnings.filterwarnings('error', category=DeprecationWarning)"
    },
    
    # ============================================================================
    # CLASS/OBJECT ERRORS
    # ============================================================================
    "TypeError: __init__() missing required positional argument": {
        "explanation": "You're creating an object but didn't provide all required arguments to __init__.",
        "fix": "Provide all required arguments when creating the object.",
        "example": "class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n# Wrong: p = Person('Alice')\n# Right: p = Person('Alice', 30)"
    },
    
    "TypeError: __init__() got an unexpected keyword argument": {
        "explanation": "You provided a keyword argument that the __init__ method doesn't accept.",
        "fix": "Check the class definition for correct parameter names.",
        "example": "class Person:\n    def __init__(self, name, age):\n        pass\n\n# Wrong: p = Person(name='Alice', years=30)\n# Right: p = Person(name='Alice', age=30)"
    },
    
    "TypeError: 'method' object is not subscriptable": {
        "explanation": "You're trying to use square brackets on a method instead of calling it first.",
        "fix": "Add parentheses to call the method, then use square brackets.",
        "example": "my_list = [1, 2, 3]\n# Wrong: item = my_list.pop[0]\n# Right: item = my_list.pop(0)"
    },
    
    # ============================================================================
    # COMPARISON ERRORS
    # ============================================================================
    "TypeError: '<' not supported between instances": {
        "explanation": "You're trying to compare objects that can't be compared (e.g., string and integer).",
        "fix": "Convert objects to the same type before comparing, or use different logic.",
        "example": "# Wrong: if '5' < 10\n# Right: if int('5') < 10\n# Or: if '5' < '10'  # String comparison"
    },
    
    # ============================================================================
    # SLICE ERRORS
    # ============================================================================
    "TypeError: slice indices must be integers or None": {
        "explanation": "You're using a non-integer value in list slicing.",
        "fix": "Convert the slice index to an integer.",
        "example": "my_list = [1, 2, 3, 4, 5]\nx = 2.5\n# Wrong: result = my_list[0:x]\n# Right: result = my_list[0:int(x)]"
    },
    
    # ============================================================================
    # HASH ERRORS
    # ============================================================================
    "TypeError: unhashable type: 'list'": {
        "explanation": "You're trying to use a mutable object (list, dict, set) as a dictionary key or in a set. Only immutable objects can be hashed.",
        "fix": "Convert to an immutable type like tuple, or use a different data structure.",
        "example": "# Wrong: my_dict = {[1, 2]: 'value'}\n# Right: my_dict = {(1, 2): 'value'}\n\n# Wrong: my_set = {[1, 2], [3, 4]}\n# Right: my_set = {(1, 2), (3, 4)}"
    },
    
    "TypeError: unhashable type: 'dict'": {
        "explanation": "You're trying to use a dictionary as a dictionary key or add it to a set.",
        "fix": "Use tuples of items, or restructure your data.",
        "example": "# Wrong: my_dict = {{1: 2}: 'value'}\n# Right: my_dict = {tuple({1: 2}.items()): 'value'}"
    },
    
    # ============================================================================
    # COMPREHENSION ERRORS
    # ============================================================================
    "NameError: name comprehension variable is not defined": {
        "explanation": "You're trying to access a loop variable from a list comprehension outside of it.",
        "fix": "List comprehension variables are local to the comprehension.",
        "example": "# Wrong:\n[x**2 for x in range(10)]\nprint(x)  # x is not defined outside\n\n# Right:\nresult = [x**2 for x in range(10)]\nfor x in range(10):\n    print(x)  # Regular loop"
    },
    
    # ============================================================================
    # CONTEXT MANAGER ERRORS
    # ============================================================================
    "AttributeError: __enter__": {
        "explanation": "You're using 'with' statement on an object that doesn't support the context manager protocol.",
        "fix": "Use objects that support 'with' or implement __enter__ and __exit__ methods.",
        "example": "# Wrong: with my_list:\n# Right: with open('file.txt') as f:\n\n# Or create context manager:\nfrom contextlib import contextmanager\n@contextmanager\ndef my_context():\n    yield\n    # cleanup"
    },
    
    # ============================================================================
    # DECORATOR ERRORS
    # ============================================================================
    "TypeError: decorator() takes 0 positional arguments but 1 was given": {
        "explanation": "Your decorator is not properly structured to accept functions.",
        "fix": "Decorators should return a function that accepts a function.",
        "example": "# Wrong:\ndef my_decorator:\n    pass\n\n# Right:\ndef my_decorator(func):\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs)\n    return wrapper"
    },
    
    # ============================================================================
    # MULTI-THREADING/PROCESSING ERRORS
    # ============================================================================
    "RuntimeError: can't start new thread": {
        "explanation": "The system can't create more threads (resource limit reached).",
        "fix": "Reduce the number of concurrent threads, or use a thread pool.",
        "example": "from concurrent.futures import ThreadPoolExecutor\n\nwith ThreadPoolExecutor(max_workers=10) as executor:\n    results = executor.map(my_function, data)"
    },
    
    "BrokenPipeError": {
        "explanation": "Trying to write to a pipe/socket that's been closed on the other end.",
        "fix": "Check if the connection is still open before writing.",
        "example": "try:\n    socket.send(data)\nexcept BrokenPipeError:\n    print('Connection closed')\n    reconnect()"
    },
    
    # ============================================================================
    # DATABASE ERRORS (common with sqlite3, psycopg2, etc.)
    # ============================================================================
    "sqlite3.OperationalError": {
        "explanation": "A database operation failed (table doesn't exist, database locked, etc.).",
        "fix": "Check that tables exist, database isn't locked, and SQL syntax is correct.",
        "example": "import sqlite3\ntry:\n    cursor.execute('SELECT * FROM table')\nexcept sqlite3.OperationalError as e:\n    print(f'Database error: {e}')\n    # Create table if missing"
    },
    
    # ============================================================================
    # PANDAS ERRORS (if pandas is used)
    # ============================================================================
    "pandas.errors.ParserError": {
        "explanation": "Pandas couldn't parse the CSV/file properly.",
        "fix": "Check file format, delimiter, and encoding.",
        "example": "import pandas as pd\ntry:\n    df = pd.read_csv('file.csv', encoding='utf-8', on_bad_lines='skip')\nexcept pd.errors.ParserError:\n    df = pd.read_csv('file.csv', sep='\\t')  # Try tab delimiter"
    },
    
    "KeyError in pandas": {
        "explanation": "You're trying to access a column that doesn't exist in the DataFrame.",
        "fix": "Check column names with df.columns, watch for typos.",
        "example": "import pandas as pd\ndf = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})\nprint(df.columns)  # See available columns\n# Wrong: df['C']\n# Right: df['A']"
    },
}


def get_error_info(error_type, error_message):
    """
    Get explanation and fix for a given error.
    
    Args:
        error_type: Type of the exception (e.g., 'TypeError')
        error_message: Full error message
        
    Returns:
        Dictionary with explanation, fix, and example
    """
    # Try exact match first
    full_error = f"{error_type}: {error_message}"
    
    # Check for exact pattern matches
    for pattern, info in ERROR_KNOWLEDGE_BASE.items():
        if pattern in full_error:
            return info
    
    # Try matching just the error type with partial message
    for pattern, info in ERROR_KNOWLEDGE_BASE.items():
        if error_type in pattern and any(keyword in error_message.lower() for keyword in pattern.lower().split() if keyword not in ['error', ':', 'the', 'a', 'an']):
            return info
    
    # Try matching just the error type
    for pattern, info in ERROR_KNOWLEDGE_BASE.items():
        if error_type == pattern.split(':')[0].strip():
            return info
    
    # Check for module-specific errors
    if '.' in error_type:
        module_error = error_type.split('.')[-1]
        for pattern, info in ERROR_KNOWLEDGE_BASE.items():
            if module_error in pattern:
                return info
    
    # Generic fallback based on error type
    generic_explanations = {
        'Error': 'An error occurred during program execution.',
        'Warning': 'A warning was issued - the code ran but something might be wrong.',
        'Exception': 'An exception was raised during program execution.',
    }
    
    explanation = generic_explanations.get(
        error_type.replace('Error', '').replace('Exception', '').replace('Warning', ''),
        f"A {error_type} occurred."
    )
    
    # Generic fallback
    return {
        "explanation": f"{explanation} {error_type}: {error_message}",
        "fix": "Review the error message and stack trace carefully. Check the line number indicated and verify the values of variables involved. Common solutions include: checking data types, validating inputs, ensuring variables are defined before use, and checking for typos in variable/function names.",
        "example": "# Add debugging:\nprint(f'Debug: variable = {variable}')\nprint(f'Debug: type = {type(variable)}')\n\n# Or use try-except:\ntry:\n    risky_operation()\nexcept Exception as e:\n    print(f'Error details: {e}')\n    import traceback\n    traceback.print_exc()"
    }