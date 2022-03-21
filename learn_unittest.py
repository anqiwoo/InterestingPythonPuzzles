'''
unit test单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
    - 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
    - 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
    - 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
    - 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。


可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
'''

import unittest


class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if not isinstance(self.score, int):
            raise ValueError('Score must be an integer!')
        if self.score < 0 or self.score > 100:
            raise ValueError('Score must be between 0 and 100!')
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        else:
            return 'C'


class TestStudent(unittest.TestCase):
    '''
    编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
    以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()。
    '''

    def setUp(self):
        '''
        可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
        '''
        print('Setting up...')

    def tearDown(self):
        '''
        可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
        '''
        print('Tearing down...')

    def test_90_to_100(self):
        s1 = Student('Adam', 100)
        s2 = Student('Alice', 90)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_80_to_90(self):
        s1 = Student('Bob', 89)
        s2 = Student('Billy', 80)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_80(self):
        s1 = Student('Cindy', 79)
        s2 = Student('Candy', 0)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Lisa', 111)
        s2 = Student('Jenny', -1)
        s3 = Student('Vicky', 'hhh')
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
        with self.assertRaises(ValueError):
            s3.get_grade()


'''
一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码:
if __name__ == '__main__':
    unittest.main()
这样就可以把XX.py当做正常的python脚本运行：
$ python XX.py

或者直接在命令行里
$ python -m unittest XX.py
'''
if __name__ == '__main__':
    unittest.main()
