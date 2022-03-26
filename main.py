from doubleLinkedList import DoubleLinkedList

inst_dll = DoubleLinkedList()

inst_dll.prepend_node(1)
inst_dll.prepend_node(2)
inst_dll.prepend_node(3)
inst_dll.append_node(4)
inst_dll.append_node(5)
inst_dll.show_double_linked_list()
print("gets")
print(inst_dll.get_node(1).value)
print(inst_dll.get_node(4).value)


print('\n')
print(inst_dll.update(3))
print(inst_dll.insert(4,16))
inst_dll.shift_by_index(3)
inst_dll.show_double_linked_list()
inst_dll.reverse()
inst_dll.show_double_linked_list()

