# Job Search Assistant for Codex

Open this repository in Codex to run a guided job search. Codex asks for your résumé and preferences, finds and ranks open roles, and prepares a tailored résumé PDF and application answers for the roles you choose. With supported browser access, it can prepare the employer's form and submit it after you approve the final review.

## Quickstart

1. Clone the repo, then open the `job-search-showcase` folder as a **local project** in the ChatGPT desktop app and start a Codex chat.

   ```sh
   git clone https://github.com/JoeMCao/job-search-showcase.git
   ```

2. Copy the [launch prompt](START.md) into that chat. Pick a starting point.

   | I want to… | What to say or provide |
   | --- | --- |
   | Try it with fictional data | “Run the fictional demo.” See the [worked example](worked-example.md) for the inputs and expected review. |
   | Evaluate my own posting | Attach your résumé, paste the posting URL or text, and say “Evaluate this role.” |
   | Find jobs every morning | Say “Set up my job search.” Codex will ask for your résumé, target roles, location, hard requirements, and preferred morning time. |

3. For PDF export, let Codex use a Python environment with `reportlab` and `pypdf`. If those are missing, it can set up an environment with the commands below. For visual PDF review, Codex needs a PDF viewer or renderer such as Poppler. Everything else in the fictional demo works from the supplied files.

   ```sh
   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   ```

   On Windows, use `py -m venv .venv` and `.venv\Scripts\python.exe -m pip install -r requirements.txt`.

Codex discovers the [repository skill](.agents/skills/job-search-assistant/SKILL.md) in the clone. You can also use `$job-search-assistant` directly or paste the launch prompt. Candidate files and results live under the Git-ignored `.job-search/` directory in your local checkout. Work in your own local copy with a résumé you're comfortable giving to Codex.

## Morning search

Once Codex has saved your profile, ask it to run a live search now. Inspect the first shortlist, then tell Codex the time and time zone you want. It can create a scheduled task in that chat, with the repo's [morning search instructions](.agents/skills/job-search-assistant/references/morning-search.md). You can review, pause, or change the task in **Scheduled**.

Each run verifies postings at employer sources, skips previously reviewed roles, and reports the strongest new matches with links, reasons, and open questions. Reply with the roles you want to pursue. You can also explicitly opt in to automatic local drafts for top matches.

Live search requires web access. Keep the computer on and the desktop app running when the task needs your local files. The schedule is created in your account during setup. [OpenAI scheduled task guide](https://learn.chatgpt.com/docs/scheduled-tasks).

## From a shortlist to a submitted application

1. Tell Codex which role you like. It drafts the résumé, generates and grades the PDF, and shows the supporting experience and application answers.
2. Approve the packet for the named employer and ask Codex to prepare the form. Codex opens the verified page, fills the approved details, and asks you to step in for steps such as sign-in, verification, or file upload when needed.
3. Review the final fields and attachment. Tell Codex **“Submit this application”** when you are ready. If the browser and site allow it, Codex submits and records the observed receipt. If you need to click Submit yourself, it hands you the form with a list of anything still open. [OpenAI browser guide](https://learn.chatgpt.com/docs/browser).

The fictional demo ends with the review packet. It uses a simulated posting and never contacts an employer.
