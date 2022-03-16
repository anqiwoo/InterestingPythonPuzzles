# -*- coding: utf-8 -*-

def combo_cal(n):
    '''
    Input: 
        n: a integer number representing the no. of sentences in a doc

    Output: 
        the no. of combinations that separating sentences into elements. 

    For example, if a doc contains three sentences, we can let the first sentence be the first element and let the second and third sentences be the second element. 
    In this way, when we call combo_cal(3), we get 4. The 4 here represents that:
        - 1: (1st sent) + (2nd sent & 3rd sent)
        - 2: (1st sent) + (2nd sent) + (3rd sent)
        - 3: (1st sent & 2nd sent) + (3rd sent)
        - 4: (1st sent & 2nd sent & 3rd sent)

    More examples: 
        - combo_call(1) = 1
        - combo_call(2) = 2
        - combo_call(3) = 4
        - combo_call(4) = 7

    如何解决这个问题！:这个问题是问，n个句子有多少种顺序语段划分的方式？
    - 那么，我们可以先看第一个句子有多少种选择：它有（n-1）种至少跟第二个句子（如果有的话）绑定在一起的选择，以及1种不跟第二个句子绑定在一起的选择；再看，第二个句子有多少种选择：如果第一个句子选择前述（n-1）种方法任意一个，第二个句子只有1种选择，即跟着第一个句子的选择走；如果第一个句子选择前述那1种不跟第二个句子绑定的选择，那么第二个句子就有一个选择分支，它可以选择（n-2）种跟下一个句子（如果有的话）绑定在一起的选择，它也可以选择1种不跟下一个句子绑定在一起的选择。
    - 如此类推，我们利用分步乘法和分类加法的排列组合知识，推出n个句子的顺序语段划分次数符合：f(n) = (n-1)*1 + 1*(n-1) = n-1 + f(n-1)。
    - 在下面程序设计方面，我们运用递归函数完成功能。
    '''
    assert n > 0 and type(n) == int, 'n should be a integer greater than 0.'
    if n == 1:
        return 1
    else:
        return n - 1 + combo_cal(n - 1)


n = 4
print(combo_cal(n))
