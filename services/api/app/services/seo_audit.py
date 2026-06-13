"""SEO audit service.

Runs technical/on-page checks for a URL and returns a list of findings. This is
a scaffold with a couple of illustrative checks; extend with real crawling.
"""

from dataclasses import dataclass, field


@dataclass
class AuditFinding:
    check: str
    severity: str  # "info" | "warning" | "error"
    message: str


@dataclass
class AuditReport:
    url: str
    findings: list[AuditFinding] = field(default_factory=list)


async def run_audit(url: str) -> AuditReport:
    """Run a basic SEO audit for a URL."""
    report = AuditReport(url=url)

    # Placeholder checks — replace with real crawling/analysis.
    report.findings.append(
        AuditFinding(
            check="title_tag",
            severity="info",
            message="Title tag length should be 50-60 characters.",
        )
    )
    report.findings.append(
        AuditFinding(
            check="meta_description",
            severity="info",
            message="Meta description should be 150-160 characters.",
        )
    )

    return report
