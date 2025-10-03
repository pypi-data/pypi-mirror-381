# Constitution

• One spec file per target site.
• All selectors, filters, and params belong in /specs/.
• All baselines belong in /baselines/.
• All screenshots, HTML snapshots, and logs must be produced for every /baseline and /test.
• The critical path (Navigation → Search → Results → Extraction) must always be preserved.
• All generated artifacts must follow template schemas from /templates/.
• Assistants must never write outside /specs/, /baselines/, /logs/, /framework/, or /docs/.
• Push/Pull operations must always sync entire site context (spec + baseline + logs), never partial.
