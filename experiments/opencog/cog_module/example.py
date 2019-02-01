try:
    from opencog.type_constructors import *
    from opencog.utilities import initialize_opencog
    from opencog.bindlink import bindlink, execute_atom
except RuntimeWarning as e:
    pass


atomspace = AtomSpace()
initialize_opencog(atomspace)

def check_nums(arg1, arg2, arg3):
    to_int = lambda x: int(float(x.name))
    if to_int(arg1) + to_int(arg2) == to_int(arg3):
        return TruthValue(1, 1)
    return TruthValue(0, 0)

def compute_prob(set_of_pairs):
    print("results")
    for item in set_of_pairs.out:
        # compute p(A, B)
        print(item)
    return set_of_pairs

var_x = VariableNode("X")
var_y = VariableNode("Y")
vardecl = VariableList(TypedVariableLink(var_x, TypeNode("NumberNode")), TypedVariableLink(var_y, TypeNode("NumberNode")))
ev = EvaluationLink(GroundedPredicateNode("py:check_nums"), ListLink(var_x, var_y, NumberNode("8")))
#print(str(ev))
g = BindLink(vardecl, AndLink(var_x, var_y, ev), ListLink(var_x, var_y))
eq = EqualLink(PlusLink(var_x, var_y), NumberNode("8"))
g2 = BindLink(vardecl, AndLink(var_x, var_y, eq), ListLink(var_x, var_y))
prob_link = ExecutionOutputLink(
        GroundedSchemaNode("py:compute_prob"),
        ListLink(g2))


print(str(g2))
print(prob_link)
NumberNode("4")
NumberNode("9")
NumberNode("1")
NumberNode("8")
NumberNode("0")
print("bindlink")
print(bindlink(atomspace, g2))
print('executionoutputlink')
print(execute_atom(atomspace, prob_link))

