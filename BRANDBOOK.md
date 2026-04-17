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
  trigger: Any build or rebuild of the HTML. Any Stitch regeneration.
  locked_by: Space Grotesk is on the frontend-design skill's explicit avoid list. Inter is generic. Bebas Neue matches the aggressive condensed register of Dennis's voice and the Jack Mallers reference. DM Sans reads clean at light weights without genericness.
  confusable_with:
    - stitch_defaults: Stitch defaults to Space Grotesk and Inter. Every regeneration risks font drift. Test — does the rendered headline use Bebas Neue? If not, the build is wrong regardless of how the content looks.
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
  trigger: Any rebuild or Stitch regeneration that reintroduces these.
  locked_by:
    - Slide numbers are internal. Meaningless to visitor.
    - Decorative columns are filler.
    - Copyright year is noise.
    - Animations contradict static loads-once reads-once intent.
    - Icons require labeling with text anyway.
    - Images — typography is the only graphic element.
  confusable_with:
    - stitch_additions: Stitch added a dot-grid decorative column and vertical line in first output. These will reappear in regenerations. Test — does any element on the page exist without a content reason? Remove it.
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
# 2. Hosting — GitHub Pages vs Netlify vs Namecheap direct (session pending)
# 3. agent_layer — decided, not yet in the build
# 4. Monitoring — what gets measured: visits, agent reads, venue echo
# 5. proofbridge.nl — inherits this design language, builds after interactiondesign.nl is live
# 6. modelvault_sync — BRANDBOOK not yet in git

---

# MATURITY MODEL
# locked: decision closed, reason recorded, apply without asking Dennis
# open: decision pending, reason recorded, do not build until closed
# pending_implementation: decided, not yet in the build

# Current positions:
# locked: site_purpose, no_labels, typography, color, one_page_no_scroll, removed_elements, deploy_mechanism, offering_moat
# open: rotating_quotes, modelvault_sync
# pending_implementation: agent_layer
