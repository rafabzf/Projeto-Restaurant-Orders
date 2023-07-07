from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    farinha = Ingredient('farinha')
    ovo = Ingredient('ovo')

    assert farinha.__hash__() == farinha.__hash__()
    assert farinha.__hash__() != ovo.__hash__()
    assert farinha == farinha
    assert repr(farinha) == "Ingredient('farinha')"
    assert farinha.name == 'farinha'
    assert farinha.restrictions == {Restriction.GLUTEN}
