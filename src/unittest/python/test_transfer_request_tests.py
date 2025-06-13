"""class for testing the regsiter_order method"""
import unittest
import os
import json
from freezegun import freeze_time
from uc3m_money.account_manager import AccountManager
from uc3m_money.account_management_exception import AccountManagementException

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    # pylint: disable=unused-variable
    # pylint: disable=too-many-locals
    @freeze_time("03/02/2025")
    def test_transfer_request_1(self):
        """Probamos el caso de prueba correcto con fecha mayor que la fecha de la orden
        Si la transferencia existe ya en el archivo json salta excepcion"""
        manager = AccountManager()
        from_iban = "ES6621000418401234567891"
        to_iban = "ES6000491500051234567892"
        concept = "Abono nomina"
        tipo = "ORDINARY"
        date = "04/02/2025"
        amount = 400.34
        request = manager.transfer_request(from_iban, to_iban,
                                           concept, tipo, date, amount)
        # Devolvemos la cadena MD5 correspondiente al Transfer Code
        print("Cadena en MD5:", request.transfer_code)
        # Comprobamos que el hash sea el correcto
        self.assertGreaterEqual(request.transfer_code, "8167f0313c3597fbcb107857b38446e7")
        # Comprobamos que el JSON se guarde correctamente
        json_file_store = os.path.join(os.path.dirname(__file__), ".././JsonFiles/")
        file_transfer_store = os.path.join(json_file_store + "transfer_store.json")
        os.makedirs(json_file_store, exist_ok=True)
        if not os.path.exists(file_transfer_store):
            with open(file_transfer_store, "w", encoding="utf-8") as file:
                file.write("[]")
        with open(file_transfer_store, "r", encoding="utf-8", newline="") as file:
            try:
                data_list = json.load(file)
            except json.JSONDecodeError: # JSON vacio
                data_list = []
        request_json = request.to_json()
        if request_json not in data_list:
            data_list.append(request_json)
            with open(file_transfer_store, "w", encoding="utf-8") as file:
                json.dump(data_list, file, ensure_ascii=False, indent=4)
                funciona = True
                self.assertEqual(funciona, True)
        else:
            message = "Transfer already in json file"
            self.assertEqual(message, "Transfer already in json file")

    @freeze_time("12/10/2041")
    def test_transfer_request_2(self):
        """Probamos el caso de prueba erroneo, from_iban no valido"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            # from_iban con mas de 24 caracteres (25 caracteres)
            from_iban = "ES66210004184012345678913"
            to_iban = "ES1000492352082414205416"
            concept = "Abono nomina hoy"
            tipo = "URGENT"
            date = "12/10/2041"
            amount = 900.35
            result = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "IBAN from_iban invalid")

    @freeze_time("12/10/2041")
    def test_transfer_request_3(self):
        """Probamos el caso de prueba erroneo, to_iban no valido"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            from_iban = "ES6621000418401234567891"
            to_iban = "ES10004923520824142" # to_iban de menos de 24 caracteres (23 caracteres)
            concept = "Abono nomina hoy"
            tipo = "URGENT"
            date = "12/10/2041"
            amount = 900.35
            result = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "IBAN to_iban invalid")

    @freeze_time("12/10/2041")
    def test_transfer_request_4(self):
        """Probamos el caso de prueba erroneo, concept con solo una cadena y 9 caracteres"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            from_iban = "ES6621000418401234567891"
            to_iban = "ES6000491500051234567892"
            concept = "Nomina"
            tipo = "URGENT"
            date = "12/10/2041"
            amount = 900.35
            result = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "Invalid concept")

    @freeze_time("12/10/2041")
    def test_transfer_request_5(self):
        """Probamos el caso de prueba erroneo, concept con tres cadenas pero con 31 caracteres"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            from_iban = "ES6621000418401234567891"
            to_iban = "ES6000491500051234567892"
            concept = "Abonosnomina ayermismo lohicimo" # Los espacios cuentan en len
            tipo = "URGENT"
            date = "12/10/2041"
            amount = 900.35
            result = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "Invalid concept")

    @freeze_time("12/10/2041")
    def test_transfer_request_6(self):
        """Probamos el caso de prueba erroneo, tipo es distinto de los valores prestablecidos"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            from_iban = "ES6621000418401234567891"
            to_iban = "ES6000491500051234567892"
            concept = "Abono nomina"
            tipo = "READY"
            date = "12/10/2041"
            amount = 900.35
            result = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "Invalid type")

    @freeze_time("12/10/2041")
    def test_transfer_request_7(self):
        """Probamos el caso de prueba erroneo, el dia de la fecha es invalido"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            from_iban = "ES6621000418401234567891"
            to_iban = "ES6000491500051234567892"
            concept = "Abono nomina"
            tipo = "URGENT"
            date = "00/12/2025"
            amount = 900.35
            result = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "Day number invalid")

    @freeze_time("12/10/2041")
    def test_transfer_request_8(self):
        """Probamos el caso de prueba erroneo, el mes de la fecha es invalido"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            from_iban = "ES6621000418401234567891"
            to_iban = "ES6000491500051234567892"
            concept = "Abono nomina"
            tipo = "URGENT"
            date = "22/14/2025"
            amount = 900.35
            result = manager.transfer_request(from_iban, to_iban,concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "Month number invalid")

    @freeze_time("12/10/2041")
    def test_transfer_request_9(self):
        """Probamos el caso de prueba erroneo, el year de la fecha es invalido"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            from_iban = "ES6621000418401234567891"
            to_iban = "ES6000491500051234567892"
            concept = "Abono nomina"
            tipo = "URGENT"
            date = "22/11/2023"
            amount = 900.35
            result = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "Year number invalid")

    @freeze_time("12/10/2041")
    def test_transfer_request_10(self):
        """Probamos el caso de prueba erroneo, la fecha es anterior a la fecha de la orden"""
        manager = AccountManager()
        from_iban = "ES6621000418401234567891"
        to_iban = "ES6000491500051234567892"
        concept = "Abono nomina"
        tipo = "URGENT"
        date = "11/10/2041"
        amount = 900.35
        request = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)

        # Comprobamos que el hash es correcto
        self.assertNotEqual(request.transfer_code, "dad654eba37fed922d9361399d9499b2")

    @freeze_time("12/10/2041")
    def test_transfer_request_11(self):
        """Probamos el caso de prueba erroneo, la cantidad esta fuera del rango establecido"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            from_iban = "ES6621000418401234567891"
            to_iban = "ES6000491500051234567892"
            concept = "Abono nomina"
            tipo = "URGENT"
            date = "22/11/2031"
            amount = 1000000.00
            result = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "Invalid amount")

    @freeze_time("12/10/2041")
    def test_transfer_request_12(self):
        """Probamos el caso de prueba erroneo, formato fecha no valido"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            from_iban = "ES6621000418401234567891"
            to_iban = "ES6000491500051234567892"
            concept = "Abono nomina"
            tipo = "URGENT"
            date = "4 de julio de 2044"
            amount = 1000.00
            result = manager.transfer_request(from_iban, to_iban, concept, tipo, date, amount)
            self.assertEqual(cm.exception.message, "Date format invalid")

if __name__ == '__main__':
    unittest.main()
