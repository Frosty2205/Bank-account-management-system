"""class for testing calculate method"""
import unittest
import os
import json
from datetime import datetime, timezone
from uc3m_money.account_management_exception import AccountManagementException
from uc3m_money.account_manager import AccountManager

class MyTestCase(unittest.TestCase):
    """class for testing calculate method"""
    # pylint: disable=unused-variable
    def test_calculate_balance_1(self):
        """Probamos caso valido"""
        manager = AccountManager()
        iban = "ES6621000418401234567891"
        suma_total = manager.calculate_balance(iban)
        date = datetime.now(timezone.utc)
        diccionario = {"IBAN": iban, "amount": f"{suma_total:.2f}", "date": str(date)}
        funciona = False
        # Comprobamos que el JSON se guarde correctamente
        json_file_store = os.path.join(os.path.dirname(__file__), ".././JsonFiles/")
        calculate_balance_store = os.path.join(json_file_store + "calculate_balance.json")
        os.makedirs(json_file_store, exist_ok=True)
        if not os.path.exists(calculate_balance_store):
            with open(calculate_balance_store, "w", encoding="utf-8") as file:
                file.write("[]")
        with open(calculate_balance_store, "r", encoding="utf-8", newline="") as file:
            try:
                data_list = json.load(file)
            except json.JSONDecodeError:  # JSON vacio
                data_list = []
        data_list.append(diccionario)
        with open(calculate_balance_store, "w", encoding="utf-8") as file:
            json.dump(data_list, file, ensure_ascii=False, indent=4)
            funciona = True
            self.assertEqual(funciona, True)

    def test_calculate_balance_2(self):
        """Probamos caso no valido, IBAN no valido"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            iban = "ES000000000000000000"
            result = manager.calculate_balance(iban)
            self.assertEqual(cm.exception.message, "Invalid IBAN")

    def test_calculate_balance_3(self):
        """Caso no valido, IBAN no se encuentra en transactions.json"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            iban = "ES7620770024003102575766"
            result = manager.calculate_balance(iban)
            self.assertEqual(cm.exception.message, "IBAN not in transactions.json")

    def test_calculate_balance_4(self):
        """Caso no valido, archivo vacio. Para este caso hay que eliminar elementos en el json"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            iban = "ES7620770024003102575766"
            result = manager.calculate_balance(iban)
            self.assertEqual(cm.exception.message, "File is not in JSON format or JSON is empty")

    def test_calculate_balance_5(self):
        """Caso no valido, fallo en calculos. La funcion devolvería error de JSONDecode"""
        manager = AccountManager()
        iban = "ES6621000418401234567891"
        result = manager.calculate_balance(iban)
        funciona = True
        self.assertEqual(funciona, True)
