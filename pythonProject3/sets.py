rainbows_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(rainbows_colors)
print(type(rainbows_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 34, 56, 3, 3, 3]
text_tuple = ('dfg', 'jas', 'aas', 'hi', 'hi', 'hi')
set_number_list = set(number_list)
set_text_tuple = set(text_tuple)

set_number_list.add(893)
set_text_tuple.add('hello')
set_number_list.pop()
set_number_list.remove(3)
set_number_list.discard(34)
set_number_list.clear()
print(set_number_list)
print(set_text_tuple)