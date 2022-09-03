def testListDivide():

    assert listDivide([1,2,3,4,5]) == 2
    assert listDivide([2,4,6,8,10]) == 5
    assert listDivide([30, 54, 63,98, 100], divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1,2,3,4,5], 1) == 5
    
def listdivide(numbers, divide=2):  
    counter = 0
    for number in numbers:
        if number % divide == 0:
            counter += 1

    return counter
    
class ListDivideException():
    pass

