#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList([-1, -2, -3, -4])

my_list = MyList([-1, -2, -3.5, -3.4, -4.5])
my_list.print_sorted()
my_list.print_sorted()

my_list = MyList([-1.3, -2.6, -3.5, -3.4, -4.5])
my_list.print_sorted()