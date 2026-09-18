# Support Automation Toolkit | By Sajid Manzoor
Technical Support Engineer | VoIP & SaaS Support Automation

This toolkit is what I built at Global Management Services to cut 35% manual L1 effort by identifying repeatable patterns.

## 1. Repeatable Patterns Identified (40% of L1 Volume)
- SIP Registration Failures (401/403) - 18%
- One-Way Audio / RTP Packet Loss - 12%
- API Authentication Failures - 10%

## 2. Zendesk Automation
- Trigger: Auto-tag `voip_sip_failure` when subject contains "SIP 401, registration failed"
- Automation: Auto-assign to VoIP queue, set priority High, SLA 2hr
- Macro: "SIP 401 Fix" - 5 step diagnostic + Wireshark capture request
- Result: 28% ticket deflection

## 3. JIRA Service Management
- Automation Rule: When issue created with label `voip`, auto-link to Confluence playbook
- SLA: P1 <2hr, P2 <8hr, P3 <24hr - tracked in dashboard
- JQL: `project = SUPPORT AND status = "Escalated to Eng" AND component = VoIP`

## 4. Postman Automation
- Collection: `API Health Check Automation`
- Tests: Status code, response time <500ms, auth token validation
- Pre-request script for auto token refresh
- File: /postman/voip-api-health.json

## 5. Wireshark Filters Library
- SIP failures: `sip.Status-Code == 401 || sip.Status-Code == 403`
- One-way audio: `rtp && !rtcp`
- NAT issues: `stun || sip contains "Via"`

## 6. Python Log Parser
- Script to parse SIP logs and count error codes
- File: /scripts/sip_log_parser.py
- SQL query for CSAT & ticket metrics

## 7. Knowledge Base Articles (30+)
- KB001: How to fix SIP 401/403
- KB002: One-way audio troubleshooting - 7 steps
- KB003: NAT traversal checklist
- Link: [Confluence Playbook]

## Impact
- 35% reduction in manual L1 effort
- 28% ticket deflection via KB + macros
- 25% faster escalation to Engineering
- 95%+ CSAT maintained

Contact: sajidmanzoor7301@gmail.com | linkedin.com/in/sajidmanzoor730
