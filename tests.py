from src.core.symmetrical_components import SymmetricalComponents


ia = (10, 0)
ib = (10, 0)
ic = (10, 0)

components = SymmetricalComponents().sequence_component(ia,ib,ic)

print(components)
