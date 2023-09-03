# Modules:
# Any file containing logically organized Python code can be used as a module.
# A module generally contains any of the defined functions, classes and variables.
# A module can also include executable code.
# Any Python source file can be used as a module by using an import statement in some other Python source file.

# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Create a Module:
# To create a module just save the code you want in a file with the file extension .py
# function in a module.
# def greeting(name):
#     print("Hello, " + name)
#
#
# variable in a module.
# person1 = {
#     "name": "John",
#     "age": 36,
#     "country": "Norway"
# }

# Use a Module:
# Now we can use the module we just created, by using the import statement.
# Import the module named mymodule.

# import mymodule

# mymodule.greeting("Jonathan")
# a = mymodule.person1["age"]
# print(a)


# Re-naming a Module:
# You can create an alias when you import a module, by using the 'as' keyword.
# Create an alias for mymodule called mx:

# import mymodule as mx

# a = mx.person1["age"]
# print(a)


# Import From Module:
# You can choose to import only parts from a module, by using the 'from' keyword

# from mymodule import person1

# print (person1["age"])

# When using a function from a module, use the syntax: module_name.function_name


# Packages:
# A package is a collection of modules present in a folder. The name of the package is the name of the folder itself.
# A package generally contains an empty file named '__init__.py ' in the same folder,
# which is required to treat the folder as a package.
