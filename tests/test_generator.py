from sofc_builder.generator import create_pure_zirconia

def test_create_pure_zirconia():
    atoms = create_pure_zirconia()
    
    # Verifica se o objeto retornado contém átomos
    assert len(atoms) > 0
    # Verifica se contém os elementos da zircônia (Zr e O)
    symbols = atoms.get_chemical_symbols()
    assert "Zr" in symbols
    assert "O" in symbols