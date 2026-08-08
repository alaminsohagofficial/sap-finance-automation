# Technical System Specification
**Project:** SAP ERP & H2H Banking API Integration for Automated DZ Collection Clearing  
**Target System:** Butterfly Marketing Limited ERP (SAP S/4HANA / ECC 6.0)  
**Document Version:** 1.0.0  
**Target Audience:** SAP ABAP Developers, Middleware/API Developers, System Administrators  
**Date:** August 09, 2026  

---

## 1. Architectural Overview

এই আর্কিটেকচারের উদ্দেশ্য হলো টিএসও/ডিলার অ্যাপ (TSO App) এবং কর্পোরেট পার্টনার ব্যাংকগুলোর (DBBL, Dhaka Bank, City Bank) মধ্যকার লেনদেনকে Host-to-Host (H2H) Webhook API-এর মাধ্যমে সরাসরি এসএপি (SAP) ডাটাবেজে যুক্ত করা, যাতে কোনো প্রকার ম্যানুয়াল ইন্টারভেনশন ছাড়াই `DZ` ক্লিয়ারিং ডকুমেন্ট তৈরি হয়।

```text
[Dealer App / Gateway] ──(1. Payment Event)──> [Partner Bank H2H Server]
                                                         │
                                               (2. Encrypted Webhook)
                                                         ▼
[SAP Financial Ledger] <──(4. Post DZ Doc)── [SAP API Listener / PO]
