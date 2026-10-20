#!/bin/sh
# Tell Bing / IndexNow engines that interactiondesign.nl changed. Run after every push (from your Mac).
curl -s -H "Content-Type: application/json; charset=utf-8" https://api.indexnow.org/indexnow -d '{
  "host": "interactiondesign.nl",
  "key": "555fdb1b3d03075a61c0b195fc231210",
  "keyLocation": "https://interactiondesign.nl/555fdb1b3d03075a61c0b195fc231210.txt",
  "urlList": ["https://interactiondesign.nl/", "https://interactiondesign.nl/setup/", "https://interactiondesign.nl/llms.txt", "https://interactiondesign.nl/index.md", "https://interactiondesign.nl/setup/index.md"]
}' -w "IndexNow HTTP %{http_code}\n"
