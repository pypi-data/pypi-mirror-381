# """
# v2 - sub parsers etc.
# """
#
# from __future__ import annotations
#
# import argparse
# import asyncio
# import os
# import sys
# from pathlib import Path
#
# import pyperclip
#
# from amherst.actions import print_file
# from amherst.actions.emailer import send_invoice_email
# from amherst.actions.invoice_number import next_inv_num
# from amherst.actions.payment_status import get_payment_status, invoice_num_from_path
# from amherst.models.commence_adaptors import CategoryName
#
#
# def shipper_cli():
#     args = parse_ship_args()
#     import_and_set_env(args)  # BEFORE IMPORTING SHIPPER
#     from amherst.ui_runner import shipper  # AFTER SETTING ENVIRONMENT
#
#     asyncio.run(shipper(args.category, args.record_name))
#
#
# def parse_ship_args():
#     arg_parser = argparse.ArgumentParser()
#     arg_parser.add_argument('category', type=CategoryName, choices=list(CategoryName))
#     arg_parser.add_argument('record_name', type=str)
#     arg_parser.add_argument('--sandbox', action='store_true', help='Run in sandbox mode')
#     args = arg_parser.parse_args()
#     cat = CategoryName.Trial if 'trial' in args.category else CategoryName(args.category.title())
#     args.category = cat
#     return args
#
#
# def import_and_set_env(args):
#     from amherst.set_env import set_amherstpr_env
#
#     set_amherstpr_env(sandbox=args.sandbox)
#
#
# def file_printer_cli():
#     parser = argparse.ArgumentParser(description='Print a file using the default printer.')
#     parser.add_argument('file_path', type=str, help='Path to the file to print')
#     args = parser.parse_args()
#     file_path = args.file_path
#     if not os.path.exists(file_path):
#         print(f'File not found: {file_path}')
#         sys.exit(1)
#     print_file(file_path)
#
#
# def send_invoice_email_cli():
#     parser = argparse.ArgumentParser(description='Send an invoice email with attachment.')
#     parser.add_argument('invoice', type=Path, help='Path to the invoice PDF')
#     parser.add_argument('address', type=str, help='Recipient email address')
#     args = parser.parse_args()
#     asyncio.run(send_invoice_email(args.invoice, args.address))
#
#
# def payment_status_cli():
#     parser = argparse.ArgumentParser(description='Check invoice payment status')
#     parser.add_argument('invoice_number', type=str, help='Invoice number to check')
#     parser.add_argument('accounts_spreadsheet', type=Path, help='Path to accounts spreadsheet', nargs='?')
#     args = parser.parse_args()
#     inv_num = invoice_num_from_path(args.invoice_number)
#     accs_file = args.accounts_spreadsheet or Path(r'R:\ACCOUNTS\ye2025\ac2425.xls')
#     print(get_payment_status(inv_num, accs_file))
#
#
# def next_invoice_cli():
#     res = next_inv_num()
#     pyperclip.copy(res)
#     print(f'next available invoice number is {res} and is copied to clipboard')
#     sys.exit(0)
#
#
# def main():
#     parser = argparse.ArgumentParser(description='Amherst CLI')
#     subparsers = parser.add_subparsers(dest='command', required=True)
#
#     # Shipper subcommand
#     shipper_parser = subparsers.add_parser('shipper')
#     shipper_parser.add_argument('category', type=str)
#     shipper_parser.add_argument('record_name', type=str)
#     shipper_parser.add_argument('--sandbox', action='store_true')
#
#     # Print file subcommand
#     print_parser = subparsers.add_parser('print_file')
#     print_parser.add_argument('file_path', type=str)
#
#     # Add other subcommands as needed...
#
#     args = parser.parse_args()
#
#     if args.command == 'shipper':
#         shipper_cli(args)
#     elif args.command == 'print_file':
#         file_printer_cli(args)
#
# if __name__ == "__main__":
#     main()