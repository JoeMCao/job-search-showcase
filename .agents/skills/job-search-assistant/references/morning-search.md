# Morning job search

## Run a scout

1. Read the current `.job-search/profile.md` and prior role records. If the profile is missing or inaccessible, report what needs to be set up. For web queries, use role and location criteria. Keep the candidate's name, contact details, and résumé out of search queries.
2. Search public employer careers sites and ATS boards, using public search or an allowed jobs connector already available to the candidate. Use aggregators for leads. Verify each shortlisted role on the employer or official ATS page, including the title, location, requisition ID if visible, and whether applications are still accepted. Record the official URL and date checked. Treat search snippets, disconnected apply buttons, and stale copies as leads that need verification.
3. Separate definite conflicts from unknowns on the candidate's hard requirements and the employer's stated minimum qualifications. Rank verified eligible roles by the candidate's preference order, breaking ties with evidence from their résumé. Put promising roles with unresolved requirements in a “needs verification” note. Explain the criteria and evidence that determined the order.
4. Check for duplicate records by employer and requisition ID, then by canonical posting URL without tracking parameters. If a cross-post is ambiguous, review it before adding it. Skip roles previously shortlisted, passed, prepared, submitted, or unclear after an attempted submission, unless the candidate asks to revisit a role or a material posting change warrants review. Save newly shortlisted roles and a dated run summary under `.job-search/runs/`. On a retry, preserve any results already reported that day.
5. Report up to five strong new matches by default, with links, fit evidence, and gaps. Distinguish “no verified new matches” from a search whose sources were unavailable. Ask which roles to pursue. Draft for a shortlisted role only if the candidate picks it or has opted in to automatic local drafts.

The scheduled run may search public pages and write private local reports and opt-in drafts. Reserve all employer form activity, sign-in, data transfer, and submission for an interactive chat.

## Set up the schedule

Run the first search in the local project to verify access to the profile, web, and output directory. When the candidate requests a schedule and supplies or accepts the time and time zone, use Codex's native scheduled task action. Use this chat so it retains the candidate's context and local project. Keep private details in the profile, outside the task prompt. When the app supports it, test the scheduled task once and check the actual run. If the schedule tool isn't available, give the candidate the prompt below and direct them to the desktop app's Scheduled view. Confirm creation or testing only after the app reports it.

Suggested task prompt:

```text
Use the job-search-assistant skill in this local project. Follow its morning
search instructions and read the current profile and role history under
.job-search/. Find and verify open roles from public sources, then rank and
record new matches. Report the shortlist with employer links and reasons.
If no verified new matches are found, say so briefly. If access failed, say
which source or permission blocked the run. Draft local packets only if the
profile opts in. Never contact an employer or interact with a live
application form in a scheduled run.
```
