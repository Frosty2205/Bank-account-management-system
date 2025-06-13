"""Module """
import re
import os
import json
from uc3m_money.transfer_request import TransferRequest
from uc3m_money.account_deposit import AccountDeposit
from uc3m_money.account_management_exception import AccountManagementException

class AccountManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_iban(iban: str):
        """
        Esta función valida si el IBAN es correcto mediante una expresión regular
        Solo acepta IBAN españoles
        """
        # Comprobación formato IBAN español
        pattern = r"ES\d{2}\d{20}$"
        if not re.match(pattern, iban):
            return False
        # Obtener dígitos de control
        checksum_iban = int(iban[2:4])
        # Convertir IBAN en versión numérica para cálculo mod 97. Mueve ES(1428) y dos 0 al final
        iban_ordenado = iban[4:] + "1428" + "00"
        iban_num = int(iban_ordenado)
        # Calcula checksum real
        checksum_real = 98 - (iban_num % 97)
        # Compara y si son iguales el IBAN es correcto
        return checksum_iban == checksum_real

    @staticmethod
    # Disable too many arguments and positional arguments error
    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
    def transfer_request(from_iban: str, to_iban: str,
                         concept: str, tipo: str, date: str, amount: float):
        """Funcion de transfer"""
        from_iban_test = AccountManager.validate_iban(from_iban)
        to_iban_test = AccountManager.validate_iban(to_iban)
        patron = r"^(\d{2})\/(\d{2})\/(\d{4})$"
        if not re.match(patron, date):
            raise AccountManagementException("Date format invalid")
        day, month, year = map(int, date.split('/'))
        if not 1 <= day <= 31:
            raise AccountManagementException("Day number invalid")
        if not 1 <= month <= 12:
            raise AccountManagementException("Month number invalid")
        if not 2025 <= year <= 2050:
            raise AccountManagementException("Year number invalid")
        cantidad = str(amount)
        decimales = len(cantidad.split('.')[1]) if '.' in cantidad else 0
        if from_iban_test is False:
            raise AccountManagementException("IBAN from_iban invalid")
        if to_iban_test is False:
            raise AccountManagementException("IBAN to_iban invalid")
        if len(concept.split()) < 2 or len(concept) < 10 or len(concept) > 30:
            raise AccountManagementException("Invalid concept")
        if  tipo not in ("INMEDIATE", "ORDINARY", "URGENT"):
            raise AccountManagementException("Invalid type")
        if decimales != 2 or 10000.00 < amount < 10.00:
            raise AccountManagementException("Invalid amount")
        return TransferRequest(from_iban, to_iban, concept, tipo, date, amount)

    @staticmethod
    def deposit_into_account(input_file):
        """Función para el deposit"""
        # pylint: disable=line-too-long
        try:
            dir_actual = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(dir_actual, "..", "..", "..",
                                     "unittest", "JsonExamples", input_file)
            json_path = os.path.normpath(json_path)
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            if not all(key in data for key in ["IBAN","AMOUNT"]):
                raise AccountManagementException("Json no contiene claves IBAN, AMOUNT o ninguna o vacio")
            iban_test = AccountManager.validate_iban(data["IBAN"])
            if not iban_test:
                raise AccountManagementException("Invalid IBAN")
            patron = r"^EUR\d{4}\.\d{2}$"
            if not re.match(patron, data["AMOUNT"]):
                raise AccountManagementException("Invalid AMOUNT")
            return AccountDeposit(data["IBAN"],data["AMOUNT"])
        except FileNotFoundError as exc:
            raise AccountManagementException("File could not be found") from exc
        except json.JSONDecodeError as exc:
            raise AccountManagementException("File is not in JSON format or is empty") from exc

    @staticmethod
    def calculate_balance(iban_number):
        """Función para el saldo"""
        iban_test = AccountManager.validate_iban(iban_number)
        suma = 0
        claves = 0
        if not iban_test:
            raise AccountManagementException("Invalid IBAN")
        try:
            dir_actual = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(dir_actual, "..", "..", "..",
                                     "unittest", "python", "transactions.json")
            json_path = os.path.normpath(json_path)
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for item in data:
                claves += 1
                if item["IBAN"] == iban_number:
                    suma += float(item["amount"])
            if suma == 0:
                raise AccountManagementException("IBAN not in transactions.json")
            return suma
        except FileNotFoundError as exc:
            raise AccountManagementException("File could not be found") from exc
        except json.JSONDecodeError as exc:
            raise AccountManagementException("File is not in JSON format or JSON is empty") from exc
