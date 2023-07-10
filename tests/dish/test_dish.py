from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    bacon = Ingredient("bacon")
    bacon_quantity = 7

    pizza = "Pizza"
    pizza_price = 10.99

    pastel = "Pastel"
    pastel_price = 3.50

    pizza_dish = Dish(pizza, pizza_price)
    pastel_dish = Dish(pastel, pastel_price)

    assert pizza_dish.name == pizza
    assert pizza_dish.__hash__() == pizza_dish.__hash__()
    assert pizza_dish.__hash__() != pastel_dish.__hash__()
    assert pizza_dish == pizza_dish
    assert repr(pizza_dish) == f"Dish('{pizza}', R${pizza_price:.2f})"

    with pytest.raises(TypeError):
        assert Dish(pizza, "1")
    with pytest.raises(ValueError):
        assert Dish(pizza, 0)

    pizza_dish.add_ingredient_dependency(bacon, bacon_quantity)
    assert pizza_dish.recipe.get(bacon) == bacon_quantity
    assert pizza_dish.get_ingredients() == {bacon}
    assert pizza_dish.get_restrictions() == bacon.restrictions