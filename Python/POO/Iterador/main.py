mytuple = ("apple", "banana", "cherry")
myiter = iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))

# create a iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.


class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 6:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# GPT explain
"""
An iterator in Python is an object that allows you to iterate over a sequence of elements, such as a list, tuple, 
or any other iterable data type. Iterators are fundamental in Python for looping and data traversal.


Iterable:

An object capable of returning its elements one at a time.
Common iterable objects include lists, tuples, dictionaries, and strings.


Iterator:
An object that represents a stream of data.
It must have two methods: __iter__() and __next__().
The __iter__() method returns the iterator object itself.
The __next__() method returns the next value from the iterator.
When there are no more items to return, __next__() should raise the StopIteration exception.
"""