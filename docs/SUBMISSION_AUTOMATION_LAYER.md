# Submission Automation Layer

**Purpose:** For every Guest Post, Citation, PR, and Directory opportunity, automate **everything up to the final submission** — find the submission URL + contact, generate the required content, draft the outreach, assemble a submission package, store it in Airtable, and advance status — so a human's only job is the **final submit**.

**Last updated:** 2026-06-11 · Owner: Off-Page SEO Director

> ## ⛔ The automation boundary (unchanged guardrail)
> The system prepares and advances opportunities **up to and including `Ready For Submission`**, then **STOPS**. It **never** submits a form, sends a pitch, creates an account, or publishes. A **human** performs the actual submission and only then is `Submitted` set. `Approved` / `Published` / `Rejected` are tracked from the human-reported result. *(Same boundary as [AUTOMATION_CONTROLLER.md](AUTOMATION_CONTROLLER.md) and the project guardrails.)*
>
> **Contact data:** only **publicly listed editorial/submission** contacts (e.g. a publication's "submit" page, a directory's listing form). Never scrape or guess private personal emails.

---

## 1. Scope → tables

| Opportunity type | Airtable table | ID |
|------------------|----------------|----|
| Guest Post Opportunity | Guest Post Pipeline | `tblKNJ8lUadwMHbSB` |
| Citation Opportunity | Citation Opportunities | `tblvYbZDlBC9XFJ2l` |
| PR Opportunity | Digital PR Opportunities | `tblXWELOOfh0xMR8i` |
| Directory Opportunity | Citation Opportunities *(directories)* / Link Opportunities | `tblvYbZDlBC9XFJ2l` / `tbls5HJYFizVeLIrt` |

---

## 2. Submission Status lifecycle (the 8 stages)

```
   ── SYSTEM PREPARES (automated, recommendations only) ──┐         ── HUMAN ──┐   ── TRACK ──
   Discovered → Qualified → Content Created → Ready For Submission │ → Submitted │ → Approved → Published
                                                                   │             │ ↘ Rejected
   ────────────────────────────────────────────────────── boundary ┘             └────────────
```

| Stage | Who | What happens |
|-------|-----|--------------|
| **Discovered** | system | Opportunity found (publication/directory/outlet identified) |
| **Qualified** | system | Authority/relevance checked; **submission URL + contact + guidelines found** |
| **Content Created** | system | **Required content generated** (article draft / listing copy / pitch + quote) |
| **Ready For Submission** | system | **Package assembled + outreach draft written**, stored in Airtable → queued for human |
| **Submitted** | **HUMAN** | A person submits the form / sends the pitch / creates the listing, then sets this status |
| **Approved** | track | Destination accepted (editor/directory approved) |
| **Published** | track | Live (article published / citation live / coverage landed) |
| **Rejected** | track | Declined — keep record + reason (never delete) |

> The system may set status **only up to `Ready For Submission`**. `Submitted` onward is human-set.

---

## 3. Airtable field requirements

Add this **common "Submission" field set** to each of the 4 opportunity tables (Guest Post Pipeline, Citation Opportunities, Digital PR Opportunities, Link Opportunities):

| Field | Type | Purpose |
|-------|------|---------|
| **Submission Status** | Single select: `Discovered`, `Qualified`, `Content Created`, `Ready For Submission`, `Submitted`, `Approved`, `Published`, `Rejected` | the unified submission lifecycle |
| **Submission URL** | URL | where to submit/pitch (submit page / form / editorial contact page) |
| **Submission Method** | Single select: `Email`, `Web Form`, `Account/Portal`, `Postal/Manual` | tells the human how to submit |
| **Contact Name** | Single line text | public editorial/submission contact |
| **Contact Email** | Email | public contact / form address (never private/scraped) |
| **Required Content** | Long text *(+ Attachments)* | the content the destination requires (article draft / listing copy / pitch) |
| **Outreach Draft** | Long text | the personalised message for the human to send |
| **Submission Package** | Long text | the assembled, copy-paste-ready package (or summary + link) |
| **Package Link** | URL | link to the full package markdown in `outputs/` |
| **Submission Owner** | Single line text | the human assigned to submit |
| **Submitted Date** | Date | set when the human submits |
| **Result Notes** | Long text | approval/rejection reason, published URL, audit trail |

**Per-table reconciliation (keep existing fields; map them):**
- *Guest Post Pipeline* already has Brief/Writing/Publication Status + URL — keep for production tracking; `Submission Status` is the new umbrella.
- *Citation Opportunities* already has `Status` (Identified/Submitted/Live/Needs Fix) — map into Submission Status (below).
- *Digital PR Opportunities* already has `Status` (Identified/Drafted/Pitched/Landed/Passed) — map below.
- *Link Opportunities* already has `Status` (Identified/Qualified/Outreach/Won/Rejected) — map below.

### Status crosswalk (existing → Submission Status)
| Submission Status | Guest Post | Citation | Digital PR | Link Opp |
|-------------------|-----------|----------|-----------|----------|
| Discovered | Brief Pending | Identified | Identified | Identified |
| Qualified | Brief Pending (+URL found) | Identified (+URL) | Identified | Qualified |
| Content Created | Writing Draft/Review | — (copy drafted) | Drafted | — |
| Ready For Submission | Writing Completed | (package ready) | (pitch ready) | Outreach |
| Submitted | — | Submitted | Pitched | (sent) |
| Approved | — | — | — | — |
| Published | Publication Published | Live | Landed | Won |
| Rejected | (declined) | Needs Fix/(declined) | Passed | Rejected |

---

## 4. Submission package contents (what the system assembles per type)

Stored as a markdown file in `outputs/offpage/submissions/<type>/<slug>.md`, linked from Airtable `Package Link`; key fields mirrored into Airtable.

**Guest Post package:** publication + guidelines · proposed title + outline (Content Brief) · **full draft article (DRAFT — human reviews/publishes)** · author bio · target anchor + internal URL (e.g. Security Guards) · pitch email draft · submission URL + method.

**Citation / Directory package:** directory + submission URL/method · **canonical NAP block** (name, the 7 offices, phone 1300 723 887, ABN) · category · short + long business description · hours · logo/image references · listing copy · note: *human creates/owns the account*.

**PR package:** pitch email draft · headline options · story angle · expert quote · **supporting stats (sourced + verified — never invented)** · media contact + deadline · target page link · press-kit references.

**Directory package:** = Citation package (directory listings are NAP citations).

> All content is a **draft/proposal**. Guest-post articles are **never auto-published**; a human reviews and submits. Stats must be **verified before any pitch**.

---

## 5. Workflow updates (per agent)

Each off-page intelligence agent gains these steps (inserted into its existing Read→Dedup→Update→Backup flow):

1. **Discover** → create/maintain the opportunity record (`Submission Status = Discovered`).
2. **Qualify** → research the **submission URL, method, public contact, and guidelines**; set `Qualified`.
3. **Create content** → generate the required content (Content Brief agent for guest articles; Citation agent for listing copy + NAP; Digital PR agent for pitch + quote + sourced stats); set `Content Created`.
4. **Assemble package** → write the package file to `outputs/offpage/submissions/...`, draft the outreach, populate `Submission Package` + `Package Link` + `Outreach Draft`; set **`Ready For Submission`** → **STOP, queue for human**.
5. **Human submits** → person submits/sends/creates the listing, sets `Submitted` + `Submitted Date`.
6. **Track outcome** → `Approved` → `Published`, or `Rejected` (with reason); log won links/citations to Knowledge Base + Metrics Snapshots.

**Agent ownership:**
- Guest Post Intelligence → guest-post packages.
- Citation Intelligence → citation/directory packages (NAP).
- Digital PR Intelligence → PR packages.
- Backlink Intelligence → resource/partnership link packages (Link Opportunities).
- **Outreach Intelligence** → owns `Outreach Draft` generation across all types and the queue of `Ready For Submission` items.

**Automation Controller integration:** the daily scheduled runs ([AUTOMATION_CONTROLLER.md](AUTOMATION_CONTROLLER.md)) advance opportunities to `Ready For Submission`, log to **Execution Logs**, and update **Metrics Snapshots** (e.g. count `Ready For Submission` per type). They **never** cross the boundary to `Submitted`.

---

## 6. Result — human workload reduced to "final submission only"
For each opportunity, when the human opens it they find: the **submission URL + method**, the **contact**, the **finished content**, the **outreach draft**, and a **copy-paste package** — all in Airtable + a backup file. Their task shrinks to: review → submit → set `Submitted`. Everything before that is automated; everything outward stays human.

## 7. Guardrails
- System advances only to `Ready For Submission`; **humans set `Submitted` onward**.
- **Never** submit, send, create accounts, publish, or delete.
- Public contacts only; **no scraping** of private data.
- Stats/claims **sourced + verified** before any pitch; guest articles are drafts, never auto-published.
- Airtable = system of record; markdown package = backup; audit trail on every record (Rule 5); never delete (Rule 4).

## 8. Implementation steps
1. **Add the Submission field set** (§3) to the 4 tables — *(API can add these fields on approval; the `Submission Status` select + URL/email/text fields are all API-creatable).*
2. Create `outputs/offpage/submissions/{guest-posts,citations,pr,directories}/`.
3. Update the 5 off-page agent definitions with the §5 steps (add the submission-package stage).
4. Wire into the Automation Controller (advance to `Ready For Submission`, log, snapshot).
5. Build an Airtable **"Ready For Submission" view** per table (filter `Submission Status = Ready For Submission`) as the human's work queue.

> **Status:** specification only — no fields created and no automation activated yet. On approval I can add the Submission field set to the 4 tables and create the `submissions/` folders.
