# haddock-restraints-py

This repository contains the bindings of the
[`haddock-restraints`](https://github.com/haddocking/haddock-restraints) code
so that it can be used as a python library.

```
pip install haddock-restraints
```

```python
from haddock_restraints import Interactor, Air

# Define binding regions
binding_region_1 = Interactor(id=1, chain="A", active=[10, 11], passive=[])
binding_region_2 = Interactor(id=2, chain="B", active=[2, 22], passive=[])

# Define the relation between the regions
binding_region_1.set_target(2)
binding_region_2.set_target(1)

# Set passive residues from active residues
binding_region_1.set_passive_from_active()

# Generate AIR table
air = Air(interactors=[binding_region_1, binding_region_2])
tbl = air.gen_tbl()

# Print the restraints
print(tbl)
```

🚧 🚧 🚧

