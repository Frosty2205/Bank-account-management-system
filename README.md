# Bank Account Management System

This project does a representation of how banks works by the creation of simple operations as transactions, balance or deposit. The codebase follows clean coding practices and includes unit tests to ensure correctness.

## 📄 Description

Instead of interacting with the user via terminal input, this program takes a file as an argument. The file must contain first a line with the text (## Script) and then in the next line among one or three commands per line. The interpreter reads each line, parses the command and its arguments, and executes it as a separate process.

## ✅ Features

- Transaction between two IBAN
- Desposits of a specific IBAN
- Balance of a specific IBAN

## 🛠️ Tecnologies Used

- **Python**: Core programming language
- **Pylint**: For code quality and static analysis
- **Pybuilder**: For build automation and dependency management
- **Unittest**: For writting and running test cases
  
## 📂 Project Structure

```text
bank_account_management_system/
├── scr/
│  ├── main/
│  │  ├── python/
│  │  │  ├── uc3m_money/
│  │  │  │  ├── __init__.py
│  │  │  │  ├── account_deposit.py
│  │  │  │  ├── account_management_exception.py
│  │  │  │  ├── account_manager.py
│  │  │  │  └── transfer_request.py
│  │  │  └── __init__.py
│  │  └── __init__.py
│  ├── unittest/
│  │  ├── JsonExamples/
│  │  │  ├── mytest1.json
│  │  │  ├── mytest2.json
│  │  │  └── ...
│  │  ├── JsonFiles/
│  │  │  ├── calculate_balance.json
│  │  │  ├── deposit_store.json
│  │  │  └── transfer_store.json
│  │  ├── python/
│  │  │  ├── __init__.py
│  │  │  ├── test_calculate_balance_tests.py
│  │  │  ├── test_deposit_into_account_tests.py
│  │  │  ├── test_transfer_request_tests.py
│  │  │  └── transactions.json
│  │  └── __init__.py
│  └── __init__.py
├── .gitignore
├── README.md
├── build.py
├── pylintrc
├── pyproject.toml
├── requirements.txt
└── setup.py
```
## 🚀 Getting Started

### Requirements

- Python 3.12+
- All dependencies listed in requirements.txt

Install them using:
```bash
pip install -r requirements.txt
```
## ✅ Running the proyect

This proyect runs by running the tests using PyBuilder:

```bash
pyb
```

To clean your test use:

```bash
pyb clean
```
## 🔧 Future improvements
- Implement databases in order to mantain information
- Implement process to create accounts

## 👨‍💻 Author

Daniel López-Antona Pesquera - Computer Engineering Student

## 📄 License

This proyect is licensed under the [MIT License](https://github.com/Frosty2205/Bank-account-management-system/blob/main/LICENSE.md)
