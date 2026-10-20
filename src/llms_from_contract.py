# Renders interactiondesign.nl/llms.txt from the proofbridge task contract, so both sites state the same facts.
# Usage: python3 src/llms_from_contract.py <path to proofbridge_website/src/contract.json>
import json, sys, os
K = json.load(open(sys.argv[1], encoding='utf-8'))
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fmt = lambda n: f"{n:,}".replace(',', ' ')
T1, T2 = K['tiers']
txt = f"""# interactiondesign.nl · Dennis Jansen

> {K['provider']['name']}, {K['provider']['role']}. This site holds his field observations and how he works. Paid requests go through proofbridge.nl under a fixed task contract.

## Hireable through proofbridge.nl (closed list)
""" + "\n".join(f"- `{x['id']}`: {x['does']} Output: {x['output']}" for x in K['task_types']) + f"""

Price: tier 1 from {fmt(T1['minimum_sats'])} sats, tier 2 from {fmt(T2['minimum_sats'])} sats, on-chain bitcoin. Reply within {K['lifecycle']['reply_window_days']} days. Field experience: {', '.join(K['domains_with_field_experience'])}.

- [Task contract (markdown)](https://proofbridge.nl/agents/index.md)
- [Offer as JSON](https://proofbridge.nl/offer.json)
- [Request schema](https://proofbridge.nl/schema/request.schema.json)

## What this site holds
- [Observations](https://interactiondesign.nl/index.md): twelve cases where AI output, plans or data and the field part ways, each with its source.
- [How I work](https://interactiondesign.nl/setup/index.md): process, the system behind it, skills.

## Contact
- {K['request']['to']}

## Optional
- [AI meetup live playback](https://interactiondesign.nl/AIpresentation/)
"""
open(os.path.join(OUT, 'llms.txt'), 'w', encoding='utf-8').write(txt)
print(txt)
