# Experimental design of cog.Module API for running opencog reasoning from pytorch nn.Module extension

from opencog.atomspace import AtomSpace, types, PtrValue, valueToPtrValue
from opencog.utilities import initialize_opencog, finalize_opencog
from opencog.type_constructors import *
from opencog.bindlink import execute_atom, satisfaction_link, bindlink

import torch
from torch.distributions import normal
from module import CogModule, get_cached_value, evaluate

class InputModule(CogModule):
    def __init__(self, atom, im):
        super().__init__(atom)
        self.im = im
    # def set_input(self, im) -- can be a method in cogModule
    # once called, id of the current input is increase to re-call forward() from execute(),
    # otherwise cached result can be returned... id trees can be automatically constructed by execute()...
    def forward(self):
        return self.im

class AttentionModule(CogModule):
    def __init__(self, atom):
        super().__init__(atom)
        self.x = normal.Normal(0.0, 1.0).sample()
    def forward(self, xs):
        #print("xs=", xs)
        return xs + self.x

atomspace = AtomSpace()
initialize_opencog(atomspace)

inp = InputModule(ConceptNode("image"), torch.tensor([1.]))
InheritanceLink(ConceptNode("red"), ConceptNode("color"))
InheritanceLink(ConceptNode("green"), ConceptNode("color"))
net1 = AttentionModule(ConceptNode("red"))
net2 = AttentionModule(ConceptNode("green"))


# direct execution proceeds as usual
print(net1(inp()))

# execution from Atomese
prog1 = net1.execute(inp.execute())
print(prog1)
print(get_cached_value(execute_atom(atomspace, prog1)))

prog2 = net2.execute(inp.execute())
print(get_cached_value(execute_atom(atomspace, prog2)))

bl = BindLink(
    #TypedVariableNode(VariableNode("$X"), TypeNode("ConceptNode")),
    VariableNode("$X"),
    AndLink(
        InheritanceLink(VariableNode("$X"), ConceptNode("color")),
        evaluate(VariableNode("$X"), inp.execute()) #inp.Exec() == cogModule.Execute(ConceptNode("image"))
    ),
    VariableNode("$X")
)
bindlink(atomspace, bl)
