import uuid
from opencog.atomspace import AtomSpace
from opencog.utilities import initialize_opencog, finalize_opencog
from opencog.neuralnet import PtrValue, valueToPtrValue
from opencog.atomspace import types
from opencog.type_constructors import *
from opencog.bindlink import execute_atom


def unpack_args(*atoms):
    return (unpack_arg(atom) for atom in atoms)


def unpack_arg(atom):
    value = valueToPtrValue(atom.get_value(atom))
    result = value.value()
    return result


def callPythonMethod(atom_callable, atom_method_name, args):
    val = atom_callable.get_value(atom_callable)
    obj = valueToPtrValue(val).value()
    result_atom = atom_callable.atomspace.add_node(types.ConceptNode, "tmp-result-" + str(uuid.uuid1()))
    args = args.out # args is ListLink
    result = getattr(obj, atom_method_name.name)(*unpack_args(*args))
    result_atom.set_value(result_atom, PtrValue(result))
    return result_atom


def prod(arg1, arg2):
    return arg1 * arg2


def main():
   atomspace = AtomSpace()
   initialize_opencog(atomspace)
   ConceptNode("arg1").set_value(ConceptNode("arg1"), PtrValue(55))
   ConceptNode("arg2").set_value(ConceptNode("arg2"), PtrValue(5))
   callable_atom = ConceptNode("prod")
   callable_atom.set_value(callable_atom, PtrValue(prod))
   exec_link = ExecutionOutputLink(
                 GroundedSchemaNode("py:callPythonMethod"),
                 ListLink(callable_atom,
                          ConceptNode("__call__"),
                          ListLink(ConceptNode("arg1"), ConceptNode("arg2"))))
   result = execute_atom(atomspace, exec_link)
   print("55 * 5 = {0}".format(valueToPtrValue(result.get_value(result)).value()))

if __name__ == '__main__':
   main()
