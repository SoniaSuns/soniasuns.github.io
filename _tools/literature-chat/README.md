# Local Paper Chat

The static literature page connects to a loopback-only Node service that invokes
the installed Codex CLI. It reuses CLI login, not an API key embedded in the page.
Codex still sends supplied paper excerpts, questions, and recent conversation to
its model service. This is not an offline model or ChatGPT history synchronization.

## Start

Prerequisites: Node 22+, Python 3.11+ with `pypdf`, and `codex login` completed. Keep the
website checkout in `<research>/website`, PDFs in the research subfolders, and the
standalone preview in `<research>/literature-review`.

Run `<research>/Start-Literature-Chat.ps1`. It starts a hidden background service
and opens the existing public page with a pairing token in its URL fragment.
`-Local` opens the same UI at localhost instead, and `-NoBrowser` only starts the
service. The public page may require the browser's local-network permission.
The fragment is removed by the UI and is not sent to GitHub. A paired tab stores
the token in sessionStorage; never share it or publish connection.json.

Without the launcher, run `node website/_tools/literature-chat/server.mjs` from
the research directory, then enter the port and token from
`.literature-chat/connection.json` in the page's connection controls.
The default port is 8765, with the next nine ports tried if occupied.

## Storage And Scope

- Questions and answers: `<research>/.literature-chat/history.json`, with the
  previous successful version retained as `history.json.bak`.
- PDF hash index and extracted text: `<research>/literature-corpus/`, never served
  as public files or committed to the website. Build this first with
  `python website/_tools/literature-chat/extract-library.py`. Questions only read
  the resulting page-numbered text; they never open or reparse PDFs.
- Existing personal notes remain in browser localStorage, with their existing
  export/import format. They are NOT automatically sent to Codex. Public-site
  notes and localhost notes have separate storage; export/import moves them.
- Each question supplies 1-4 chosen papers, their library summaries, up to 60,000
  PDF text characters per paper, and at most 12 recent messages / 60,000 characters.
  All older messages remain visible and exportable, but are not automatically
  included in model context. Start a focused conversation for long discussions.
- Short PDFs are included in full when text fits. For longer PDFs, the opening
  pages, explicitly requested pages, and keyword-matching pages are prioritized.
  Each answer shows the actual pages supplied. Missing/invalid extracted files
  fall back to explicitly labeled summaries. Figures and scanned pages are not OCR'd.
- History export is JSON. To restore, stop the service, preserve a copy of the
  current history, and replace `history.json` with an exported version-1 file.
  Invalid history stops startup; it is never silently reset.
- Closing the browser does not stop a running answer. Refresh/reconnect restores
  it from the service; the stop button terminates the owned Codex process tree.
- A failed/interrupted answer retains the question. Resend it to retry. The new
  turn is kept separately rather than overwriting the earlier history.

## Security

The listener binds only to 127.0.0.1, checks Host, permits only the exact public
origin and its own local origin, and requires a random bearer token for every
API call. Mutations additionally require Origin and JSON where applicable.
There is no arbitrary command, path, model, or filesystem endpoint. Do not expose
the service through tunnels or port forwarding. Other pages on the same GitHub
origin are in the same browser trust boundary.

Codex runs with a read-only sandbox, never-approve policy, user config/rules
ignored, project instructions disabled, and shell, app/plugin, browsing,
computer-use, and multi-agent features disabled. Only selected context is passed
via stdin; credentials are not copied into the web page. Managed Codex policies
still apply. Authentication failure is surfaced rather than bypassed.

## Tests

`node --test website/_tools/literature-chat/server.test.mjs` exercises the API
with an injected deterministic runner, without model calls. Browser integration
and live Codex verification are separate; a mocked test is not a live model test.

Official interface: https://learn.chatgpt.com/docs/non-interactive-mode
