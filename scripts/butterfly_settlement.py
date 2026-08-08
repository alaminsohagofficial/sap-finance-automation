import json
import os

def run_settlement_clearance():
    # Load and verify JSON payload
    payload_path = 'payloads/butterfly_final_settlement.json'
    
    if os.path.exists(payload_path):
        with open(payload_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        dealer = data['dealer_profile']['dealer_name']
        code = data['dealer_profile']['dealer_code']
        total_amount = data['sap_accounting_status']['total_reconciled_bdt']
        status = data['sap_accounting_status']['clearing_status']
        
        print("==================================================")
        print("⚡ SAP ERP SETTLEMENT EXECUTION SUCCESSFUL")
        print("==================================================")
        print(f"Dealer Name  : {dealer}")
        print(f"Dealer Code  : {code}")
        print(f"Total Amount : BDT {total_amount:,.2f}")
        print(f"Clear Status : {status}")
        print("==================================================")
    else:
        print(f"❌ Error: {payload_path} not found!")

if __name__ == "__main__":
    run_settlement_clearance()
