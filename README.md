# Support Automation Toolkit

A practical VoIP support-investigation toolkit that brings together SIP log parsing, API health-check definitions, support-metrics SQL examples and Wireshark display-filter references.

The goal is to make common investigation steps more repeatable and easier to hand over—not to diagnose or remediate a production call automatically.

## What is included

| Area | File | Purpose |
|---|---|---|
| SIP log analysis | `postman/sip_log_parser.py` | Count SIP response codes, flag a simple RTP/no-RTCP text pattern and export a CSV summary |
| API validation | `postman/voip-api-health.json` | Postman collection with registration, response-time, packet-loss and authentication assertions |
| Support reporting | `sql/support_metrics.sql` | Example SQL for issue volume, CSAT/SLA reporting and knowledge-base-linked tickets |
| Packet investigation | `wireshark/filters.txt` | Display-filter starting points for SIP, RTP/RTCP, STUN and HTTP errors |
| Project notes | `VOIP-SUPPORT-AUTOMATION.md` | Context and impact figures recorded in the original project notes |

## Investigation workflow

```text
Support symptom
      |
      v
Collect the relevant SIP / API / packet evidence
      |
      +--> Parse SIP response codes and export a CSV summary
      |
      +--> Run configured API assertions against a supplied endpoint
      |
      +--> Inspect SIP, RTP/RTCP and STUN traffic in Wireshark
      |
      +--> Query an available support database for reporting
      |
      v
Engineer reviews evidence, confirms root cause and documents next steps
```

## 1. SIP log parser

The Python script reads `sip.log` from the current working directory. It counts occurrences matching `SIP/2.0 NNN`, looks for lines matching the text pattern `RTP.*no RTCP`, and writes `sip_rca_report.csv`.

### Run

```bash
python -m pip install --upgrade pip
# Place an authorised, sanitised text log named sip.log in this directory
python postman/sip_log_parser.py
```

The CSV contains `SIP Code`, `Count` and a suggested `Action` column. The action is a basic routing hint:
- `401` / `403`: check authentication and the full registration exchange.
- `486`: review the call flow and relevant network / endpoint context.
- Other codes: review the complete trace.

**Important:** this is a text-pattern counter, not a complete SIP parser or root-cause engine. A SIP 401 may be a normal authentication challenge. The RTP/no-RTCP match is only a heuristic and does not prove one-way audio. Confirm findings with a full SIP ladder, packet capture, endpoint configuration and call context.

## 2. Postman API health checks

Import `postman/voip-api-health.json` into Postman. The collection defines checks for:
- SIP registration endpoint returns HTTP 200, responds in under 500 ms and reports `registered: true`.
- Call-quality endpoint reports packet loss below 5%.
- Authentication validation endpoint returns HTTP 200.

Before running it, configure the `base_url` collection variable for an authorised test environment and confirm that the endpoint paths and response fields match that API.

The committed collection is a test definition. No production endpoint, credentials, exported Postman run or passing live test result is included in this repository.

## 3. Wireshark filter reference

Open `wireshark/filters.txt` and use the relevant display-filter starting points while inspecting an authorised capture:
- SIP response codes such as 401, 403 and 486.
- RTP and RTCP traffic.
- STUN traffic for NAT traversal investigation.
- HTTP responses with status codes of 400 or higher.

Filters narrow the evidence to inspect; they do not establish the cause by themselves. Interpret them with the call flow, endpoints, network path and capture direction.

## 4. SQL support metrics

`sql/support_metrics.sql` contains example queries for:
- Issue volume by issue type over the last 30 days.
- Average CSAT and SLA compliance.
- Ticket counts linked to knowledge-base articles.

The queries assume tables and columns such as `tickets`, `ticket_kb_link`, `created_at`, `issue_type`, `csat_score` and `sla_breached`. A database schema, sample database and query execution output are not included. Adapt the names, SQL dialect and business definitions to the actual service-desk system before use.

## Evidence and limitations

The original `VOIP-SUPPORT-AUTOMATION.md` notes record figures including 40% repeatable L1 patterns, 35% lower manual L1 effort, 28% KB/macro deflection and 95%+ CSAT. The notes do not include a dated ticket export, sample size, baseline calculation, measurement window or independent test evidence. Treat these as reported project-note figures, not independently verified results from this repository.

This repository does not contain customer logs, production call recordings, credentials, a live VoIP endpoint, a support database, or an exported test run. The toolkit supports investigation and reporting; an engineer must validate evidence and approve any customer-impacting change.

## Technology

- Python 3
- Regular expressions and CSV
- Postman collection format v2.1
- SQL
- Wireshark display filters

## Repository structure

```text
support-automation-toolkit/
├── README.md
├── VOIP-SUPPORT-AUTOMATION.md
├── postman/
│   ├── sip_log_parser.py
│   └── voip-api-health.json
├── sql/
│   └── support_metrics.sql
└── wireshark/
    └── filters.txt
```

## Links

- [Portfolio case study](https://sajidmanzoor730.github.io/sajid-portfolio/voip-support-automation.html)
- [GitHub repository](https://github.com/sajidmanzoor730/support-automation-toolkit)

---

Built by **Sajid Manzoor** · Technical Support & Operations
