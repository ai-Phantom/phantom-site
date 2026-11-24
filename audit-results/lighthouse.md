# Lighthouse (desktop) — 2026-11-24T01:31:03.545Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 94
- accessibility: 100
- best-practices: 81
- seo: 85

## performance — opportunities
- First Contentful Paint (1.1 s)
- Speed Index (1.4 s)
- Use efficient cache lifetimes (Est savings of 12 KiB)
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":4885.199999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/vce701823e78c4301a35b7e07294d87301792088814092","cacheLifetimeMs":86400000,"wastedBytes":4191.2}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2256.8}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1108.7999999999997}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4943}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-15-DIV","path":"1,HTML,1,BODY,10,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":821,"bottom":8...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-16-SPAN","path":"1,HTML,1,BODY,10,DIV,4,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3411...
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":16578,"wastedPercent":75.8400102012624,"totalBytes":21859}
- Reduce unused JavaScript (Est savings of 115 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":182959,"wastedBytes":77011,"wastedPercent":42.09172919652643}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":48403,"wastedBytes":40282,"wastedPercent":83.22259960397469}
- Avoid serving legacy JavaScript to modern browsers (Est savings of 10 KiB)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/vce701823e78c4301a35b7e07294d87301792088814092","wastedBytes":10414,"subItems":{"type":"subitems","items":[{"signal":"Array.prototype.at","location":{"type":"source-location","url"...
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/vce701823e78c4301a35b7e07294d87301792088814092","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":104...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":48852,"wastedBytes":4885.199...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11088,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":1753,"wastedBytes":164.0377094972066}
- Avoid an excessive DOM size (4,937 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4937}}
    · {"node":{"type":"node","lhId":"1-118-SPAN","path":"1,HTML,1,BODY,10,DIV,4,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3411,"bottom":3425,"left":1219...
    · {"node":{"type":"node","lhId":"1-119-DIV","path":"1,HTML,1,BODY,10,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":821,"bottom":838,"left":-251,"right":9609,"w...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-171-IMG","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":4313,"bott...

## best-practices — opportunities
- Uses deprecated APIs (2 warnings found)
    · {"value":"FencedFrame","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js?ray=a5f4a68c1960478d","urlProvider":"network","line":0,"column":10273}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js?ray=a5f4a68c1960478d",...

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4361,"bottom":4382,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-25-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4392,"bottom":4412,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-26-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4422,"bottom":4443,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-27-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":386,"right":45...
- robots.txt is not valid (1 error found)
    · {"index":"31","line":"Content-Signal: search=yes,ai-train=no,use=reference","message":"Unknown directive"}
