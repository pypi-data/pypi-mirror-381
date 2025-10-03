from haddock_restraints import Interactor, Air, restraint_bodies


def main():

    # Basic usage example
    binding_region_1 = Interactor(id=1, chain="A", active=[10, 11], passive=[])
    binding_region_1.set_passive_from_active()

    binding_region_2 = Interactor(id=2, chain="B", active=[2, 22], passive=[])
    binding_region_2.set_passive_from_active()

    binding_region_1.set_target(2)
    binding_region_2.set_target(1)

    air = Air(interactors=[binding_region_1, binding_region_2])

    tbl = air.gen_tbl()

    print(tbl)


if __name__ == "__main__":
    main()
