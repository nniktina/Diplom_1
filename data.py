import sys
import random
import string
import ingredient_types

bun_test_data = [["Флюоресцентная булка R2-D3", 988.025],
                 ["Краторная булка N-200i", 1255],
                 ["     ", 988.025],
                 [None, 988.025],
                 ["Флюоресцентная булка R2-D3", -988.025],
                 ["Краторная булка N-200i", 0],
                 ["Флюоресцентная булка R2-D3", sys.float_info.max],
                 ["Краторная булка N-200i", sys.float_info.min],
                 ["Краторная булка N-200i", 1.4E-45],
                 ["Флюоресцентная булка R2-D3", 3.40282347E38],
                 ["Краторная булка N-200i " + ''.join(random.choices(string.ascii_letters, k=77)), 100],
                 ["@&%$*()", 0]]

ingredient_test_data = [
    [ingredient_types.INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337],
    [ingredient_types.INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.5]]
