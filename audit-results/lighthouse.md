# Lighthouse (desktop) — 2026-07-20T15:51:59.554Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 96
- accessibility: 100
- best-practices: 81
- seo: 85

## performance — opportunities
- Speed Index (1.3 s)
- Use efficient cache lifetimes (Est savings of 20 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/3104729c556c/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6775.5199999999995}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5349.5999999999985}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v4513226cdae34746b4dedf0b4dfa099e1781791509496","cacheLifetimeMs":86400000,"wastedBytes":4630.8}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2258.4}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1172.4999999999998}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4748}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-17-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":86...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-18-SPAN","path":"1,HTML,1,BODY,9,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,...
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Max Potential First Input Delay (170 ms)
- Reduce unused CSS (Est savings of 15 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":15860,"wastedPercent":77.11527914884282,"totalBytes":20567}
- Reduce unused JavaScript (Est savings of 149 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":166255,"wastedBytes":69846,"wastedPercent":42.011610893472415}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":53145,"wastedBytes":44231,"wastedPercent":83.22612591823392}
    · {"url":"https://aiphantomtraders.com/","totalBytes":74421,"wastedBytes":38399,"wastedPercent":51.596378329387726}
- Avoid serving legacy JavaScript to modern browsers
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v4513226cdae34746b4dedf0b4dfa099e1781791509496","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":115...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":53496,"wastedBytes":5349.599...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11725,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":2507,"wastedBytes":234.59357541899428}
- Avoid an excessive DOM size (4,742 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4742}}
    · {"node":{"type":"node","lhId":"1-113-SPAN","path":"1,HTML,1,BODY,9,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219,...
    · {"node":{"type":"node","lhId":"1-114-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-326,"right":9362,"wi...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-178-IMG","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"botto...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":11020}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":11020}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-20-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-21-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3697,"bottom":3718,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-22-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3728,"bottom":3749,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3759,"bottom":3780,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":386,"right":457...
- robots.txt is not valid (1 error found)
    · {"index":"30","line":"Content-Signal: search=yes,ai-train=no,use=reference","message":"Unknown directive"}
