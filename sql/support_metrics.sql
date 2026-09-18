-- Support Metrics for Dashboard

-- 1. Repeatable pattern volume (last 30 days)
SELECT issue_type, COUNT(*) as volume, 
ROUND(COUNT(*)*100.0 / (SELECT COUNT(*) FROM tickets WHERE created_at > NOW()-30),2) as pct
FROM tickets 
WHERE created_at > NOW()-30
GROUP BY issue_type 
ORDER BY volume DESC;

-- 2. CSAT & SLA compliance
SELECT 
AVG(csat_score) as avg_csat,
SUM(CASE WHEN sla_breached = 0 THEN 1 ELSE 0 END)*100.0/COUNT(*) as sla_compliance
FROM tickets WHERE assignee = 'Sajid';

-- 3. Ticket deflection by KB
SELECT kb_article_id, COUNT(*) as deflected_tickets 
FROM ticket_kb_link 
GROUP BY kb_article_id;
