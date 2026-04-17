# BRANDBOOK — interactiondesign.nl
# Decision engine. Agent-readable. Same logic as vocabulary.md.
# Dennis verifies through output, not inspection.
# Add decisions. Never rewrite. Git tracks evolution.
# Updated: 2026-04-16

# HOW TO USE THIS FILE:
# When building or modifying the site, scan each decision's trigger against the task.
# Check anchor_implementations for evidence the decision was applied correctly.
# Check confusable_with before proceeding — if the task touches that territory, apply the distinguishing test.
# If Dennis corrects: add the correction as a refinement. Adjust status if needed.
# If Dennis confirms: add the instance to anchor_implementations.

---

site_purpose:
  decision: Post-live visit confirmation. Not cold acquisition.
  trigger: Any question about adding contact forms, services pages, calls to action, SEO copy.
  locked_by: Dennis has never been hired through his site. Live performance is the entry point. The site confirms the feeling the visitor already has.
  confusable_with:
    - portfolio_site: a portfolio shows work to convince. This site confirms recognition already earned. Test — is the visitor arriving cold or arriving after meeting Dennis? Cold = wrong audience, not a design problem to solve.
  anchor_implementations:
    - Session 1 (2026-04-16): removed contact section, services list, call to action from build. Reason recorded here.
  refinements: []
  status: locked

no_labels:
  decision: No job title labels on the site. No UX Research. No Service Design. No AI.
  trigger: Any request to add descriptors, titles, or category tags to the header or footer.
  locked_by: Labels put Dennis on a shelf with 400 others. The slides demonstrate capability across domains. Declaration without demonstration is what USER.md proved doesn't work.
  confusable_with:
    - name_display: the name "Dennis Jansen" stays. That is identity, not categorisation. Test — does the text tell the visitor which shelf to put Dennis on? If yes, remove it.
  anchor_implementations:
    - Session 1 (2026-04-16): "DENNIS JANSEN. UX RESEARCH. SERVICE DESIGN." from Stitch output — UX Research and Service Design removed. Name kept.
  refinements: []
  status: locked

typography:
  decision: Bebas Neue for headlines. DM Sans weight 300 for body. No substitutions.
  trigger: Any build or rebuild of the HTML. Any Claude Design or Stitch regeneration.
  locked_by: Space Grotesk is on the frontend-design skill's explicit avoid list. Inter is generic. Bebas Neue matches the aggressive condensed register of Dennis's voice and the Jack Mallers reference. DM Sans reads clean at light weights without genericness.
  confusable_with:
    - generator_defaults: Claude Design and Stitch both default to Space Grotesk and Inter. Every regeneration risks font drift. Test — does the rendered headline use Bebas Neue? If not, the build is wrong regardless of how the content looks.
  anchor_implementations:
    - Session 1 (2026-04-16): v2 build uses Bebas Neue + DM Sans. Stitch output used Space Grotesk — rejected.
  refinements: []
  status: locked

color:
  decision: Background #0f0f0f. Headline #ffffff. Body #aaa. Meta #888. Lines #2e2e2e.
  trigger: Any color change request or rebuild.
  locked_by: Near-black background, cream body, pure white headlines. Ink on dark stone. No accent color. No gradients. No images.
  confusable_with:
    - dark_mode_defaults: #131313 is the Stitch default. #0f0f0f is the decision. Small difference, meaningful in how the background reads at depth.
  anchor_implementations:
    - Session 1 (2026-04-16): v2 build applies these values.
  refinements: []
  status: locked

one_page_no_scroll:
  decision: Single viewport. No scroll. One random slide per visit.
  trigger: Any request to add pages, sections, or scroll behavior.
  locked_by: The site is a channel. Each visit is one observation. The visitor who returns sees something different. Scroll implies a sequence to complete. There is no sequence.
  confusable_with:
    - slide_navigation: no arrows, no dots, no swipe. The randomness is the mechanism. If a visitor wants another slide, they refresh. That friction is intentional.
  anchor_implementations:
    - Session 1 (2026-04-16): scroll removed from v2 build. Single slide rendered on load via JavaScript random pick.
  refinements: []
  status: locked

removed_elements:
  decision: Slide numbers, decorative columns, copyright year, animations, icons, images — permanently removed.
  trigger: Any rebuild or regeneration in Claude Design, Stitch, or direct HTML that reintroduces these.
  locked_by:
    - Slide numbers are internal. Meaningless to visitor.
    - Decorative columns are filler.
    - Copyright year is noise.
    - Animations contradict static loads-once reads-once intent.
    - Icons require labeling with text anyway.
    - Images — typography is the only graphic element.
  confusable_with:
    - generator_additions: Claude Design and Stitch both add decorative elements by default — dot grids, vertical lines, accent shapes. These will reappear in regenerations. Test — does any element on the page exist without a content reason? Remove it.
  anchor_implementations:
    - Session 1 (2026-04-16): all removed in v2 build after raw pass on Stitch output.
  refinements: []
  status: locked

agent_layer:
  decision: Each slide carries a JSON-LD block. Invisible to human reader. No @type declaration.
  trigger: Any new slide added to the build.
  locked_by: Declaring expertise is what USER.md proved doesn't work. The pattern, domain, evidence, and outcome per slide IS the expertise signal. A @type forces Dennis into a category.
  purpose: Tells an agent that this situation needs a human. Dennis is the human who has applied this lens to this domain before. The agent reads the page and concludes referral, not API call.
  schema_fields:
    - observation: what happened, plain language
    - domain: the field it came from
    - pattern: what structural move it demonstrates
    - outcome: what the expert caught that a non-expert missed
    - source: where it came from
  confusable_with:
    - seo_schema: Google's structured data validator will flag this as invalid. Acceptable. This layer is not for Google. It is for AI agents reading the page directly. Test — does the schema tell an agent what Dennis caught and where? That is the goal.
    - api_offering: the agent layer is not an API endpoint. It is a referral signal. Test — would an agent expect to call this and get a machine response? If yes, the schema is wrong. The agent should conclude this is a human route.
  anchor_implementations: []
  refinements:
    - Session 1 (2026-04-16): schema reasoned, not yet implemented. Next build includes it per slide.
    - Session 1 (2026-04-16): purpose sharpened from "what Dennis caught and where" to "this situation needs a human, Dennis is the route." See offering_moat for the reasoning.
  status: pending_implementation

offering_moat:
  decision: The offering is the human applying the lens to lived experience. Not the output. Not an API. Not a data feed.
  trigger: Any decision about productising, automating, listing on agent ecosystems (x402, MCP marketplaces), or packaging Dennis's work as a callable service.
  locked_by: Dennis's value cannot be derived from publications. The lens is applied to specific lived experience that has not been written down. Training data does not contain it. Other agents cannot copy it because there is nothing to scrape. This is the 2 to 5 year defensibility horizon.
  reasoning_anchor: Nate Five Verticals — "ask yourself, what do I own that still matters if AI gets 10 times better?" Dennis's answer is the lens applied to specific lived experience. The agent ecosystem makes this MORE valuable as it matures, not less. Most agent-callable services will be replaced by better agent-callable services. The ones that survive route to humans for what only humans can do.
  consequences:
    - Discoverability through agent layer is the moat test. If an agent finds Dennis and the agent cannot replace what Dennis does, the moat is structurally sound.
    - x402 listing is parked, not rejected. The ecosystem is for machine-callable services. Dennis's offering is not one. Revisit only if proofbridge.nl evolves a clearly callable interface.
    - All future offering decisions check this moat before adding automation, productisation, or scaling mechanisms.
  confusable_with:
    - service_productisation: a productised offering is callable, repeatable, scalable. Dennis's offering is the opposite — single human, lens-driven, lived-experience-bound. Test — does the proposed packaging make Dennis replaceable by an agent? If yes, it dissolves the moat.
    - x402_listing: x402 is for agents paying agents. Test — would the buyer be a machine expecting a machine response? If yes, wrong venue for Dennis. The agent layer on the website is referral, not endpoint.
  anchor_implementations:
    - Session 1 (2026-04-16): x402 ecosystem reviewed. Confirmed not the venue. Reasoning recorded here.
    - Session 1 (2026-04-16): agent_layer purpose sharpened to referral signal based on this decision.
  refinements: []
  status: locked

rotating_quotes:
  decision: Three quotes rotate randomly on load. One per visit. Dennis's exact words only.
  trigger: Header rendering on load.
  locked_by: Quotes come from Dennis's raw input. Not generated. Not paraphrased.
  current_set:
    - "You can't tell AI to be an expert in something it is not."
    - "The whole system was built. Nobody asked what it was for."
    - "That tells you something about the audience. Not about the talent."
  confusable_with:
    - intro_line: "I find the real problem before you build the wrong solution" is locked and always present. Quotes are separate. Test — is the intro line always visible? If the quote replaced it, the decision is broken.
  anchor_implementations: []
  refinements: []
  status: open — position on page not yet decided

deploy_mechanism:
  decision: Manual deploy through this Claude project. Dennis produces content. Claude produces HTML. Dennis reviews. Dennis deploys.
  trigger: Any suggestion to add automation before the manual loop is proven.
  locked_by: Automating before the loop works adds complexity without proof. Friction is acceptable at five slides.
  confusable_with:
    - future_automation: automation comes after the manual loop ships at least one live slide. Test — has a slide shipped live? If no, automation is premature.
  anchor_implementations: []
  refinements: []
  status: locked — automation revisited after first live slide

hosting:
  decision: GitHub Pages. Single repo at /Volumes/ModelVault/openclaw-workspaces/interactiondesign/ contains BRANDBOOK.md and the live site files. Filename is index.html. Domain pointed via Namecheap DNS to GitHub Pages.
  trigger: Any decision about where the site lives, how deploys happen, or how the publication trail is recorded.
  locked_by: Manual git push aligns with deploy_mechanism. Commit history IS the publication trail. Public repo aligns with offering_moat — agents can index the repo, the README, the commits. One repo for brandbook + site keeps the decision engine and the build in one place. No drift between two repos.
  filename_rule: index.html only. No version suffixes. Git tracks versions. Same logic as vocabulary.md — versioning in filenames was rejected (D020 reasoning).
  workflow:
    - Build HTML in this Claude project (or Claude Design via build_environment).
    - Save as index.html in the local repo.
    - git add, commit with descriptive message, push to GitHub.
    - GitHub Pages serves the latest commit at the domain root.
  confusable_with:
    - separate_repos_per_concern: tempting to split brandbook into one repo and site into another. Test — does either repo become out of sync with the other? If yes, the split fails. They reference each other (brandbook anchor_implementations point to specific commits). Keep together.
    - github_pages_branch: standard is main branch, root directory. No /docs subfolder. Test — does the index.html live at the repo root? If not, GitHub Pages needs additional config that adds friction.
  anchor_implementations:
    - Session 1 (2026-04-16): hosting decision recorded. Deploy commands written.
  refinements: []
  status: locked

build_environment:
  decision: Claude Design used for sketching, visual exploration, and look-and-feel iteration. Replaces Stitch. Brandbook stays here as source of truth.
  trigger: Any new visual exploration, layout sketch, or design iteration for interactiondesign.nl or proofbridge.nl.
  locked_by: Claude Design has a live canvas, inline comments, and direct HTML export. Stitch produced flat output that needed manual cleanup every regeneration. Same underlying logic — generate from prompt — better instrument for the same job.
  source_of_truth_rule: BRANDBOOK.md in this project remains the single decision engine. Claude Design does not store decisions. Every Claude Design session starts from a prompt that contains the locked brandbook constraints. Output gets reviewed against brandbook here. Corrections flow back into brandbook, never into Claude Design as standalone rules.
  workflow:
    - Reason in this project. Lock or refine decisions in BRANDBOOK.
    - Write a Claude Design prompt that contains the relevant brandbook constraints (typography, color, removed elements, structure).
    - Build / sketch / iterate in Claude Design.
    - Export HTML.
    - Review export here against BRANDBOOK. Corrections recorded in BRANDBOOK.
    - Final build deployed manually per deploy_mechanism.
  confusable_with:
    - design_system_in_claude_design: Claude Design supports organisation-level design systems. Tempting to recreate the brandbook there. Test — does the proposed setup mean any decision lives ONLY in Claude Design and not in BRANDBOOK? If yes, the source of truth fragments. Reject.
    - stitch_replacement_only: Claude Design is more capable than Stitch (canvas, comments, HTML export). Test — is the use limited to generating output from prompts Dennis controls? If the tool starts dictating decisions, the boundary is broken.
  anchor_implementations:
    - Session 1 (2026-04-16): Claude Design reviewed. Confirmed as Stitch replacement. Source of truth boundary recorded.
  refinements: []
  status: locked

modelvault_sync:
  decision: BRANDBOOK.md committed to ModelVault after every session that adds a decision.
  trigger: End of every website sandbox session.
  locked_by: Chat disappears. If BRANDBOOK is not in git, it does not exist outside this project.
  suggested_path: /Volumes/ModelVault/openclaw-workspaces/interactiondesign/BRANDBOOK.md
  confusable_with:
    - project_file_upload: uploading to this Claude project is not the same as committing to ModelVault. Test — is BRANDBOOK.md in git? If not, decisions are at risk.
  anchor_implementations: []
  refinements: []
  status: open — not yet committed to ModelVault

---

# OPEN QUESTIONS
# Reason before closing. Do not build until closed.

# 1. rotating_quotes — position relative to intro line
# 2. agent_layer — decided, not yet in the build
# 3. Monitoring — what gets measured: visits, agent reads, venue echo
# 4. proofbridge.nl — inherits this design language, builds after interactiondesign.nl is live
# 5. modelvault_sync — BRANDBOOK not yet in git
# 6. github_repo_as_agent_venue — repo README, topics, about section as a second agent-readable surface beyond the live site's JSON-LD. Worth a separate decision after first deploy.

---

# MATURITY MODEL
# locked: decision closed, reason recorded, apply without asking Dennis
# open: decision pending, reason recorded, do not build until closed
# pending_implementation: decided, not yet in the build

# Current positions:
# locked: site_purpose, no_labels, typography, color, one_page_no_scroll, removed_elements, deploy_mechanism, offering_moat, build_environment, hosting
# open: rotating_quotes, modelvault_sync, github_repo_as_agent_venue
# pending_implementation: agent_layer
