# Lighthouse (desktop) — 2026-10-19T19:42:17.096Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 89
- accessibility: 100
- best-practices: 81
- seo: 92

## performance — opportunities
- Total Blocking Time (210 ms)
- Speed Index (1.5 s)
- Use efficient cache lifetimes (Est savings of 21 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/d2d3316b729e/main.js?","cacheLifetimeMs":14400000,"wastedBytes":7938.999999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5632.499999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/vce701823e78c4301a35b7e07294d87301792088814092","cacheLifetimeMs":86400000,"wastedBytes":4191.2}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2256.8}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1277.2999999999997}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4842}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-17-DIV","path":"1,HTML,1,BODY,10,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":821,"bottom":8...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-18-SPAN","path":"1,HTML,1,BODY,10,DIV,4,SECTION,0,DIV,1,DIV,1,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3390...
- Network dependency tree
- Max Potential First Input Delay (140 ms)
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":16466,"wastedPercent":75.89065817409767,"totalBytes":21697}
- Reduce unused JavaScript (Est savings of 118 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":179573,"wastedBytes":73564,"wastedPercent":40.96615257181128}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":55990,"wastedBytes":46774,"wastedPercent":83.53970476530398}
- Avoid serving legacy JavaScript to modern browsers (Est savings of 10 KiB)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/vce701823e78c4301a35b7e07294d87301792088814092","wastedBytes":10414,"subItems":{"type":"subitems","items":[{"signal":"Array.prototype.at","location":{"type":"source-location","url"...
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/vce701823e78c4301a35b7e07294d87301792088814092","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":104...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":56325,"wastedBytes":5632.499...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":12773,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":2568,"wastedBytes":240.30167597765347}
- Avoid an excessive DOM size (4,836 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4836}}
    · {"node":{"type":"node","lhId":"1-118-SPAN","path":"1,HTML,1,BODY,10,DIV,4,SECTION,0,DIV,1,DIV,1,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3390,"bottom":3404,"left":1219...
    · {"node":{"type":"node","lhId":"1-119-DIV","path":"1,HTML,1,BODY,10,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":821,"bottom":838,"left":-314,"right":9493,"w...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-170-IMG","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":4274,"bott...

## best-practices — opportunities
- Uses deprecated APIs (2 warnings found)
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":5543}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4292,"bottom":4312,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4322,"bottom":4343,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-25-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4353,"bottom":4374,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-26-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4384,"bottom":4405,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-27-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4292,"bottom":4312,"left":386,"right":45...
