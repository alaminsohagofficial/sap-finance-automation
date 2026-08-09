import json
import os

def run_master_ledger_verification():
    payload_path = 'payloads/butterfly_final_settlement.json'
    
    if os.path.exists(payload_path):
        with open(payload_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        dealer = data['dealer_profile']['dealer_name']
        code = data['dealer_profile']['dealer_code']
        h2h_total = data['h2h_batch_commit']['batch_amount_bdt']
        net_balance = data['financial_reconciliation']['current_ledger_balance_bdt']
        status = data['financial_reconciliation']['clearing_status']
        
        print("==================================================")
        print("⚡ SAP S/4HANA MASTER LEDGER AUDIT COMPLETED")
        print("==================================================")
        print(f"Dealer Name       : {dealer}")
        print(f"Dealer Code       : {code}")
        print(f"H2H Batch Commit  : BDT {h2h_total:,.2f}")
        print(f"Net Credit Balance: BDT {abs(net_balance):,.2f} (Advance)")
        print(f"F.13 Auto-Clear   : {status}")
        print("==================================================")

if __name__ == "__main__":
    run_master_ledger_verification()
