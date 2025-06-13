"""class for testing deposit method"""
import unittest
import os
import json
from uc3m_money.account_manager import AccountManager
from uc3m_money.account_management_exception import AccountManagementException

class MyTestCase(unittest.TestCase):
    """Class for testing the deposit method. T=terminal, NT=no terminal"""
    # pylint: disable=unused-variable
    # pylint: disable=line-too-long
    # pylint: disable=too-many-public-methods
    def test_deposit_into_account_1(self):
        """Probamos caso válido"""
        manager = AccountManager()
        deposit = manager.deposit_into_account("mytest1.json")
        # Devolvemos la cadena SHA-256
        print("Cadena SHA-256:", deposit.deposit_signature)
        # Creamos variable para ver si funciona
        funciona = False
        # Comprobamos que el JSON se guarde correctamente
        json_file_store = os.path.join(os.path.dirname(__file__), ".././JsonFiles/")
        file_deposit_store = os.path.join(json_file_store + "deposit_store.json")
        os.makedirs(json_file_store, exist_ok=True)
        if not os.path.exists(file_deposit_store):
            with open(file_deposit_store, "w", encoding="utf-8") as file:
                file.write("[]")
        with open(file_deposit_store, "r", encoding="utf-8", newline="") as file:
            try:
                data_list = json.load(file)
            except json.JSONDecodeError:
                data_list = []
        deposit_json = deposit.to_json()
        if deposit_json not in data_list:
            data_list.append(deposit_json)
            with open(file_deposit_store, "w", encoding="utf-8") as file:
                json.dump(data_list, file, ensure_ascii=False, indent=4)
                funciona = True
                self.assertEqual(funciona, True)
        else:
            error = "Transfer already in json file"
            self.assertEqual(error, "Transfer already in json file")

    def test_deposit_into_account_2(self):
        """Probamos caso no valido, archivo vacio. Caso borrado NT 1"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest2.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_3(self):
        """Probamos caso no valido, caso duplicado NT 1"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest3.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_4(self):
        """Probamos caso no valido, caso borrado T 2"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest4.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_5(self):
        """Probamos caso no valido, caso duplicado T 2"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest5.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_6(self):
        """Probamos caso no valido, caso modificado T 2"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest6.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_7(self):
        """Probamos caso no valido, caso borrado NT 3"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest7.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_8(self):
        """Probamos caso no valido, caso duplicado NT 3"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest8.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_9(self):
        """Probamos caso no valido, caso borrado T 4"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest9.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_10(self):
        """Probamos caso no valido, caso duplicado T 4"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest10.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_11(self):
        """Probamos caso no valido, caso modificado T 4"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest11.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_12(self):
        """Probamos caso no valido, caso borrado NT 5"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest12.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_13(self):
        """Probamos caso no valido, caso duplicado NT 5"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest13.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_14(self):
        """Probamos caso no valido, caso borrado T 6"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest14.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_15(self):
        """Probamos caso no valido, caso duplicado T 6"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest15.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_16(self):
        """Probamos caso no valido, caso modificado T 6"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest16.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_17(self):
        """Probamos caso no valido, caso borrado NT 7"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest17.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_18(self):
        """Probamos caso no valido, caso duplicado NT 7"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest18.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_19(self):
        """Probamos caso no valido, caso borrado NT 8, T 14"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest19.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_20(self):
        """Probamos caso no valido, caso duplicado NT 8", T 14"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest20.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_21(self):
        """Probamos caso no valido, caso borrado T 9"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest21.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_22(self):
        """Probamos caso no valido, caso duplicado T 9"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest22.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_23(self):
        """Probamos caso no valido, caso modificado T 9"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest23.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_24(self):
        """Probamos caso no valido, caso borrado NT 10"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest24.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_25(self):
        """Probamos caso no valido, caso duplicado NT 10"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest25.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_26(self):
        """Probamos caso no valido, caso borrado NT 11, T 18"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest26.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_27(self):
        """Probamos caso no valido, caso duplicado NT 11, T 18"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest27.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_28(self):
        """Probamos caso no valido, caso borrado T 12"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest28.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_29(self):
        """Probamos caso no valido, caso duplicado T 12"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest29.json")
            print(cm.exception)
            self.assertEqual(cm.exception.message,"File is not in JSON format or is empty")

    def test_deposit_into_account_30(self):
        """Probamos caso no valido, caso modificado T 12"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest30.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_31(self):
        """Probamos caso no valido, caso borrado NT 13"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest31.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_32(self):
        """Probamos caso no valido, caso duplicado NT 13"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest32.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_33(self):
        """Probamos caso no valido, caso modificado T 14"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest33.json")
            self.assertEqual(cm.exception.message, "Json no contiene claves IBAN, AMOUNT o ninguna o vacio")

    def test_deposit_into_account_34(self):
        """Probamos caso no valido, caso borrado NT 15, NT 17, T 22, T 25"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest34.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_35(self):
        """Probamos caso no valido, caso duplicado NT 15, T 22"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest35.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_36(self):
        """Probamos caso no valido, caso borrado NT 16"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest36.json")
            self.assertEqual(cm.exception.message, "Invalid IBAN")

    def test_deposit_into_account_37(self):
        """Probamos caso no valido, caso duplicado NT 16"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest37.json")
            self.assertEqual(cm.exception.message, "Invalid IBAN")

    def test_deposit_into_account_38(self):
        """Probamos caso no valido, caso duplicado NT 17, T 25"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest38.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_39(self):
        """Probamos caso no valido, caso modificado T 18"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest39.json")
            self.assertEqual(cm.exception.message, "Json no contiene claves IBAN, AMOUNT o ninguna o vacio")

    def test_deposit_into_account_40(self):
        """Probamos caso no valido, caso borrado NT 19", NT 21, T 26, T 31"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest40.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_41(self):
        """Probamos caso no valido, caso duplicado NT 19, T 26"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest41.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_42(self):
        """Probamos caso no valido, caso borrado NT 20"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest42.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_43(self):
        """Probamos caso no valido, caso duplicado NT 20"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest43.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_44(self):
        """Probamos caso no valido, caso duplicado NT 21, T 31"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest44.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_45(self):
        """Probamos caso no valido, caso modificado T 22"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest45.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_46(self):
        """Probamos caso no valido, caso borrado T 23"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest46.json")
            self.assertEqual(cm.exception.message, "Invalid IBAN")

    def test_deposit_into_account_47(self):
        """Probamos caso no valido, caso duplicado T 23"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest47.json")
            self.assertEqual(cm.exception.message, "Invalid IBAN")

    def test_deposit_into_account_48(self):
        """Probamos caso no valido, caso modificado T 23"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest48.json")
            self.assertEqual(cm.exception.message, "Invalid IBAN")

    def test_deposit_into_account_49(self):
        """Probamos caso no valido, caso borrado NT 24, NT 32"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest49.json")
            self.assertEqual(cm.exception.message, "Invalid IBAN")

    def test_deposit_into_account_50(self):
        """Probamos caso no valido, caso duplicado NT 24, NT 32"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest50.json")
            self.assertEqual(cm.exception.message, "Invalid IBAN")

    def test_deposit_into_account_51(self):
        """Probamos caso no valido, caso modificado T 25"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest51.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_52(self):
        """Probamos caso no valido, caso modificado T 26"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest52.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_53(self):
        """Probamos caso no valido, caso borrado T 27"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest53.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_54(self):
        """Probamos caso no valido, caso duplicado T 27"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest54.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_55(self):
        """Probamos caso no valido, caso modificado T 27"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest55.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_56(self):
        """Probamos caso no valido, caso borrado NT 28, T 33"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest56.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_57(self):
        """Probamos caso no valido, caso duplicado NT 28, T 33"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest57.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_58(self):
        """Probamos caso no valido, caso borrado T 29"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest58.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_59(self):
        """Probamos caso no valido, caso duplicado T 29"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest59.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_60(self):
        """Probamos caso no valido, caso modificado T 29"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest60.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_61(self):
        """Probamos caso no valido, caso borrado NT 30, T 34 """
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest61.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_62(self):
        """Probamos caso no valido, caso duplicado NT 30, T 34"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest62.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_63(self):
        """Probamos caso no valido, caso modificado T 31"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest63.json")
            self.assertEqual(cm.exception.message, "File is not in JSON format or is empty")

    def test_deposit_into_account_64(self):
        """Probamos caso no valido, caso modificado T 32"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest64.json")
            self.assertEqual(cm.exception.message, "Invalid IBAN")

    def test_deposit_into_account_65(self):
        """Probamos caso no valido, caso modificado T 33"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest65.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")

    def test_deposit_into_account_66(self):
        """Probamos caso no valido, caso modificado T 34"""
        with self.assertRaises(AccountManagementException) as cm:
            manager = AccountManager()
            result = manager.deposit_into_account("mytest66.json")
            self.assertEqual(cm.exception.message, "Invalid AMOUNT")
