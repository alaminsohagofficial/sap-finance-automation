import json
import requests

def send_butterfly_settlement_notification():
    # payloads/butterfly_final_settlement.json থেকে ডাটা পড়া
    with open('payloads/butterfly_final_settlement.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    dealer = data['dealer_profile']['dealer_name']
    code = data['dealer_profile']['dealer_code']
    invoice = data['dealer_profile']['invoice_ref']
    pdf_url = data['audit_links']['s3_ledger_pdf']

    # অটোমেটেড এসএমএস টেক্সট
    sms_message = (
        f"Dear Partner ({dealer} - {code}), Invoice {invoice} (298 pcs) is FULLY SETTLED. "
        f"Outstanding Balance: BDT 0.00 (Doc #5100030102). Download Ledger: {pdf_url} - Butterfly Marketing Ltd."
    )

    print("--- Updated Dispatch Message ---")
    print(sms_message)

if __name__ == "__main__":
    send_butterfly_settlement_notification()
