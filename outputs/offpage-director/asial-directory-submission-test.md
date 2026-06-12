# Submission Layer Test — ASIAL Member Directory (Ready For Submission)

**Agent:** Citation Intelligence · **Date:** 2026-06-11
**Outcome:** Complete, production-ready citation/directory package built and advanced **Content Created → Ready For Submission**. System stopped at the boundary.

---

## What the system did (automated)
| Req | Result |
|-----|--------|
| 1. Read Knowledge Base | ✅ Canonical NAP (7 offices, 1300 723 887, ABN), services, differentiators |
| 2. Read Citation record | ✅ `recZgDAalpPPnJJIQ` (ASIAL Member Directory, Auth 60, target = Security Guards) |
| 3. Populate Submission Layer fields | ✅ URL, Method (Account/Portal), Contact, Required Content, Package, Package Link, Owner |
| 4. Directory listing package | ✅ all listing field values |
| 5. Business description | ✅ short (~25w) + long (~70w) |
| 6. Category recommendations | ✅ Guards + Grade A1 Monitoring lead; 8 categories mapped |
| 7. NAP package | ✅ canonical primary NAP + all 7 offices |
| 8. Submission checklist | ✅ in package |
| 9. Verification checklist | ✅ post-listing NAP consistency checks |
| Store package | ✅ `outputs/offpage/submissions/directories/asial-member-directory.md` |
| Update Airtable | ✅ `Submission Status = Ready For Submission` |

**Package:** [outputs/offpage/submissions/directories/asial-member-directory.md](../offpage/submissions/directories/asial-member-directory.md)
**Verified source:** [ASIAL Membership Directory](https://asial.com.au/Web/Web/Member-Resources/Membership-Directory.aspx)

---

## ⚠️ Key dependency the system surfaced
The ASIAL directory is **member-only**. StateGuard must be a **current ASIAL member** to be listed — which links to the **ASIAL membership** action already queued in Airtable (Link Opportunity `Outreach`; Outreach Campaign "ASIAL membership + directory listing" = **Ready to Send**). Secure membership first; the listing follows.

## ✋ What the HUMAN must do (final submission only)
1. **Confirm/secure ASIAL membership** (prerequisite — the membership outreach is queued).
2. **Log in to the ASIAL member portal.**
3. **Enter the listing values** (name, website, phone 1300 723 887, email, ABN) + **business description** + **categories** (lead with Security Guards + Grade A1 Monitoring) — all in the package.
4. **Apply the canonical NAP exactly** (character-for-character) and confirm all 7 states/offices.
5. **Upload the logo**, save/publish the profile.
6. **On completion →** set Airtable `Submission Status` = **Submitted**, `Submitted Date` = today; when live → `Published` (paste the listing URL into `Result Notes`).
7. **Run the verification checklist** (search the directory, confirm name/phone/website/services/states, cross-check NAP vs site + GBP). Log Citations Live +1 to Metrics Snapshots.

> Human workload = **confirm membership → fill the portal with the prepared values → verify.** Everything else was done.

## Boundary proof
- The system **did not** create the ASIAL account, complete the portal, or publish the listing.
- Status advanced **only to `Ready For Submission`** — never `Submitted`.
- **No contact details invented** — ASIAL lists no public editorial email, so `Contact Email` was left blank and the channel (asial.com.au / head office) noted.
- The canonical NAP is pulled from the Knowledge Base (verified facts), not guessed.

This is the second worked example of the Submission Automation Layer — a **directory/citation** type (vs the FMA guest post), both ending at the human-gated boundary.
