"""
# Copyright Nick Cheng, Brian Harrington, Danny Heap, 2013, 2014, 2015
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2015
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from regextree import RegexTree, StarTree, DotTree, BarTree, Leaf

# Do not change anything above this comment except for the copyright
# statement

# Student code below this comment.


def is_regex_single(target_str):
    '''(str)->bool
    This method takes a single str parameter to judge whether it
    follows the features of regex.
    REQ : No str with the bracket or empty str should be passed in
    >>> is_regex_single('2*')
    True
    >>> is_regex_single('333*')
    False
    >>> is_regex_single('2|1*')
    True
    '''
    if target_str == '':
        return False
    # define the base case while the length is 1
    if len(target_str) == 1:
        # the only element should be included when the length of the str is 1
        standard = ['0', '1', '2', 'e']
        # the elements should be contained without being repeated
        return standard.count(target_str) == 1
    # define the cases while the regex has a number and a star
    elif target_str.count('.') == 0 and target_str.count('|') == 0:
        # the last element of the str should only be star
        if target_str[-1] != '*':
            return False
        # nothing should be found between stars
        for index in range(1, len(target_str)):
            if target_str[index] != '*':
                return False
        # recurse and test the accuracy of the first element
        return is_regex_single(target_str[:1])
    # the cases with dot and bar
    else:
        # see whether it is BarTree or DotTree
        if target_str.count('|') == 1:
            # find the position of the operator
            operator_index = target_str.find('|')
        elif target_str.count('.') == 1:
            operator_index = target_str.find('.')
        else:
            # return False if it contains multiple operators
            return False
        # return False if the operators are not at the right position
        if operator_index == 0 or operator_index == len(target_str) - 1:
            return False
        # recurse the left and right part to the operator
        return is_regex_single(target_str[: operator_index]) and is_regex_single(target_str[operator_index + 1:])


def find_operator_index(target_str):
    '''(str) -> int
    The returns the position of the operator not within the bracket
    REQ : This function only receives the regex without the outer bracket
    >>> find_operator_index('(2.3*)|(0.e)')
    6
    >>> find_operator_index('2.(0|(0.e))')
    1
    '''
    # start the level of bracket from 0
    inner_bracket = 0
    # initialize the operator_index as None for the convenience of the
    # comparison in later functions
    operator_index = None
    # iterate the str
    for index in range(len(target_str)):
        # see whether it contains bracket inside
        if target_str[index] == '(':
            inner_bracket += 1
        if target_str[index] == ')':
            inner_bracket -= 1
        if inner_bracket == 0:
            # find the index of the operator at the most outside level
            if target_str[index] == '.' or target_str[index] == '|':
                operator_index = index
    # return the index
    return operator_index


def is_regex(target_str):
    '''(str) -> bool
    This method takes a regex str with parenthesis bracket and test whether the
    str are valid regex expression
    >>> is_regex('((1.(0|2)*).0)')
    True
    >>> is_regex('2*3')
    False
    '''
    if target_str == '':
        return False
    # define the base case by putting the single ones into helper
    if target_str.count('(') == 0 and target_str.count(')') == 0:
        if target_str.count('.') != 0 or target_str.count('|') != 0:
            return False
        return is_regex_single(target_str)
    else:
        # if the last letter is not ) or *, return false immediately
        if target_str[-1] != ')' and target_str[-1] != '*':
            return False
        # if the last letter is *
        if target_str[-1] == '*':
            # initiate the star from the last
            index = len(target_str) - 1
            # iterate up to be the one next to the non-Star element
            while target_str[index] == '*':
                index -= 1
            # if there are something else between stars and the bracket,
            # return false
            if target_str[index] != ')':
                return False
            # truncate the str
            target_str = target_str[1:index]
        # if the last letter is not star
        else:
            # truncate the target_str, reducing the brackets
            target_str = target_str[1:len(target_str) - 1]
        # receive the index of the operator in between
        operator_index = find_operator_index(target_str)
        # if there is no operator index or it is at the first or the end
        if operator_index is None or operator_index == 0 or operator_index\
           == len(target_str) - 1:
            # return false
            return False
        # get whether both sides are valid regex
        return is_regex(target_str[:operator_index]) and is_regex(target_str[operator_index + 1:])


def get_permutations(target_str):
    '''(str) -> list of str
    This function receives a str and returns all of its permutations
    >>> get_permutations('1.2')
    ['1.2', '.12', '.21', '12.', '21.', '2.1']
    >>> get_permutations('e*')
    ['e*', '*e']
    '''
    # define the base case where the length of the str is 1
    if len(target_str) == 1:
        # return the content in a list
        return [target_str]
    # define the cases when the length of str is longer than 1
    else:
        # get the permutation from the previous str
        last_permutation = get_permutations(target_str[1:])
        # define the empty list to receive the permutations
        final_return = []
        # iterate the permutations from the lsat round
        for element in last_permutation:
            # iterate each position between the letters
            for index in range(len(element) + 1):
                # append the results to the empty list
                final_return.append(element[:index] + target_str[0]
                                    + element[index:])
        return final_return


def all_regex_permutations(target_str):
    '''(str) -> list of str
    This function receives the regex expression and returns the list of regex
    which are the permutation of the parameter.
    >>> all_regex_permutations('2().e')
    {'(2.e)', '(e.2)'}
    >>> all_regex_permutations('')
    set()
    '''
    # define an empty set
    final_return = set()
    # receive the permutations from last rounds
    permutations = get_permutations(target_str)
    # iterate the elements in the permutations
    for element in permutations:
        # if the element is a valid regex
        if is_regex(element):
            # add into the empty list
            final_return.add(element)
    # return the empty list
    return final_return


def regex_match(r, s):
    '''(RegexTree, str) -> bool
    This function receives a regex tree and a str and sees if the tree matches
    the str
    >>> regex_match(DotTree(Leaf('2'), Leaf('e')), 2)
    True
    >>> regex_match(BarTree(Leaf('2'), StarTree(Leaf('1'))), 21111)
    False
    '''
    # check if the tree is a leaf and define the base case
    if isinstance(r, Leaf):
        # check the symbol of the list
        if r.get_symbol() == 'e':
            return s == ''
        # see if s matches the symbol
        return s == r.get_symbol()
    # if the tree is a star tree
    elif isinstance(r, StarTree):
        # initiate the index of the star from the first position
        repeat_index = []
        index = 1
        # see how many possible times the branches of s repeat
        for index in range(1, len(s) + 1):
            if s[:index] * (len(s) // index) == s:
                # add the index where the branch of repetitions are up to
                repeat_index.append(index)
        # try each branch and see if they are valid for the child trees
        for index in repeat_index:
            # if the one with the least time of repetition can make it true
            if regex_match(r.get_child(), s[:index]):
                # return true
                return True
        # else return false
        return False
    # if r is a dot tree
    elif isinstance(r, DotTree):
        # split the trees by parts with different index
        for index in range(len(s) + 1):
            left_split = s[:index]
            # test whether each part can match the child trees
            left_return = regex_match(r.get_left_child(), left_split)
            right_split = s[index:]
            right_return = regex_match(r.get_right_child(), right_split)
            # return true if both parts of an index can match the child trees
            if left_return and right_return:
                return True
        # return false if the conditions are not sufficed
        return False
    # if r is a bar tree
    elif isinstance(r, BarTree):
        # see if the str matches either side of the child tree
        left_return = regex_match(r.get_left_child(), s)
        right_return = regex_match(r.get_right_child(), s)
        return left_return or right_return


def build_regex_tree(regex):
    '''(str) -> RegexTree
    This convert the valid regex expression to its tree root.
    REQ:Only the valid regex can be passed in or it will raise error
    >>> build_regex_tree('((0.1).2)')
    DotTree(DotTree(Leaf('0'), Leaf('1')), Leaf('2'))
    >>> build_regex_tree('(1.(0|2)*)')
    DotTree(Leaf('1'), StarTree(BarTree(Leaf('0'), Leaf('2'))))
    '''
    # define the base case while the length is 1
    if len(regex) == 1:
        return Leaf(regex)
    # define other cases
    else:
        # deal with the StarTree
        if regex[-1] == '*':
            # recurse the child of the StarTree
            inside = build_regex_tree(regex[:len(regex) - 1])
            # wrap the content into the StarTree
            return StarTree(inside)
        # deal with dot tree and bar tree
        elif regex[-1] == ')':
            # eliminate the brackets
            regex = regex[1:len(regex) - 1]
            # find the index of the operator
            operator_index = find_operator_index(regex)
            # find what the operator is
            operator = regex[operator_index]
            # get the trees in both side of the operator
            left_inside = build_regex_tree(regex[: operator_index])
            right_inside = build_regex_tree(regex[operator_index + 1:])
            # wrap the tree based on the operator
            if operator == '|':
                return BarTree(left_inside, right_inside)
            elif operator == '.':
                return DotTree(left_inside, right_inside)
