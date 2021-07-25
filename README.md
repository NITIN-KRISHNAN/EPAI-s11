# Iterators - session 10

## Goal
Refactor the Polygons (sequence) type, into an iterable. You'll need to implement both an iterable, and an iterator.

## New functions

`Polygons.__iter__` - creates a new object of PolygonIterator everytime this function is called, making the iterator
non exhaustable and the class Polygons as a iterable

class PolygonIterator - Iterator class to track the next time that has to be given when the Polygons class iterable is
iterated through.

`PolygonIterator.__next__` -  returns the next item in the iterator

`PolygonIterator.__iter__` - returns the iterator itself making it exhaustible

### Test cases
test_polygon - validates the properties of polygon class

test_polygons - checks if the minimum number of sides is passed

test_iterable - checks if the polygons class is iterable

test_index - checks if the polygons class is indexable (subscribable)

test_polygons_functions - checks if the required functions are defined in polygons and polygons iterator

test_iterable_non_exhaustive - checks if the polygons iterator is exhaustible or not, i.e does it provide a new iterator
object when iter is called 

test_iterable_stop_exception - checks if StopIteration exception is raised when reaching end of iterable
### Test results
 pytest -v
============================= test session starts ==============================
platform darwin -- Python 3.8.1, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/Krish/Downloads/epai/EPAI-s11
plugins: Faker-4.1.3, anyio-3.2.1
collected 7 items                                                              

test_Polygon.py::test_polygon PASSED                                     [ 14%]
test_Polygon.py::test_polygons PASSED                                    [ 28%]
test_Polygon.py::test_iterable PASSED                                    [ 42%]
test_Polygon.py::test_index PASSED                                       [ 57%]
test_Polygon.py::test_polygons_functions PASSED                          [ 71%]
test_Polygon.py::test_iterable_non_exhaustive PASSED                     [ 85%]
test_Polygon.py::test_iterable_stop_exception PASSED                     [100%]

============================== 7 passed in 0.16s ===============================
