# Prompt — Technical SEO Audit

**Agent:** [technical-seo-audit](../agents/technical-seo-audit.md) · **Output:** `../data/audits/` + summary to `../data/reports/`

---

```
[Shared preamble — see prompts/README.md]

TASK: Run a technical SEO audit of {{scope: e.g. "the URLs in ../data/audits/crawl.csv" | "stateguard.com.au /services/* pages"}}.

INPUT DATA: {{path to crawl export / PageSpeed data / log file}}

Audit these dimensions and report ONLY real, evidenced issues:
- Indexability: robots.txt, meta robots, canonicals, noindex, sitemap coverage
- Crawlability: broken links, redirect chains/loops, orphan pages, crawl depth
- Performance / Core Web Vitals: LCP, CLS, INP, image weight, caching
- Structured data: validity + GAPS ONLY — do NOT flag schema that already exists
  (Organization, WebSite, Service, FAQPage, LocalBusiness, Breadcrumb are present via Yoast — see client-profile §5)
- Architecture: nested URL convention, internal linking (3/6/9 already implemented), duplicates, AU/US spelling
- Mobile/responsive + alt-text basics

RESPECT KNOWN CONSTRAINTS: no staging, tight ~15GB disk, do NOT suggest enabling the LiteSpeed Crawler.

OUTPUT: a findings table to ../data/audits/{{filename}}.md with columns:
ID | Severity (Critical/High/Medium/Low) | Issue | Affected URLs | Evidence (source + how observed) | Recommended fix | Rationale
Then a short executive summary to ../data/reports/{{date}}-tech-audit-summary.md.

Recommendations only — a human implements fixes off-system.
```
