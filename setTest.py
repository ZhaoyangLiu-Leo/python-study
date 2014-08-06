#set test
ins = set(['John', 'Bob', 'Alice', 'Peter'])

print ins


def get_rid_of(ins_set, starting_letter):
    remove_set = set([])
    for ins in ins_set:
        if ins[0] == starting_letter:
            remove_set.add(ins)
    ins_set.difference_update(remove_set)


get_rid_of(ins, 'A')
print ins
