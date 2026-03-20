#  UDS Diagnostic Automation Framework (Python)

A Python-based simulation framework for **UDS (Unified Diagnostic Services)** over CAN, designed for learning, testing, and interview demonstration.

---

##  Features

- UDS Services:
  - Read Data by Identifier (0x22)
  - Write Data by Identifier (0x2E)
  - Session Control (0x10)
  - Security Access (0x27)

- Mock ECU Simulation using virtual CAN
- Pytest-based automation testing
- CLI-based execution
- XML test reporting

---

## 🏗️ Project Structure

uds-diagnostics-framework/
│
├── core/
│ ├── uds_client.py
│ ├── can_interface.py
│
├── services/
│ ├── read_did.py
│ ├── write_did.py
│ ├── session_control.py
│ ├── security_access.py
│
├── ecu_simulator/
│ ├── mock_ecu.py
│
├── tests/
│ ├── conftest.py
│ ├── test_read_did.py
│ ├── test_scenario.py
│
├── reports/
│ ├── report.xml
│
├── main.py
├── requirements.txt
└── README.md


---

**Run Services**

 Read DID
 
python main.py --service read_did --did 0xF190

 Write DID
 
python main.py --service write_did --did 0xF190 --data 0xAA 0xBB

 Session Control
 
python main.py --service session --did 0x03

 **Run Tests**
 
pytest -v --junitxml=reports/report.xml

 XML report will be generated in:

reports/report.xml

**Key Concepts Implemented**

CAN communication using python-can

UDS protocol services

Thread-based ECU simulation

Security access with seed/key

Pytest fixtures and automation

Clean architecture (service-based design)

**Future Improvements**

ISO-TP integration (multi-frame support)

Real CAN hardware support

Advanced security algorithms

Logging & reporting dashboard
