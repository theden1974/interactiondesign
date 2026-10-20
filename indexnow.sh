#!/bin/sh
# Submit every URL in sitemap.xml to IndexNow (Bing, Yandex, Naver, Seznam, Yep). Run after a push.
KEY=555fdb1b3d03075a61c0b195fc231210
HOST=interactiondesign.nl
URLS=$(sed -n 's#.*<loc>\(.*\)</loc>.*#"\1",#p' "$(dirname "$0")/sitemap.xml" | tr -d '\n' | sed 's/,$//')
curl -sS -X POST "https://api.indexnow.org/indexnow" -H "Content-Type: application/json; charset=utf-8" \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"https://$HOST/$KEY.txt\",\"urlList\":[$URLS]}"
echo
