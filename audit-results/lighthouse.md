# Lighthouse (desktop) — 2026-10-05T21:24:25.394Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 72
- accessibility: 100
- best-practices: 81
- seo: 92

## performance — opportunities
- Total Blocking Time (610 ms)
- Speed Index (1.7 s)
- Use efficient cache lifetimes (Est savings of 20 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/d76008a69eab/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6774.159999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5630.499999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","cacheLifetimeMs":86400000,"wastedBytes":4135.2}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2260}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1173.4999999999998}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":5015}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-19-DIV","path":"1,HTML,1,BODY,10,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":821,"bottom":8...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-20-SPAN","path":"1,HTML,1,BODY,10,DIV,4,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3411...
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Max Potential First Input Delay (500 ms)
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":16459,"wastedPercent":76.04543107898813,"totalBytes":21643}
- Reduce unused JavaScript (Est savings of 119 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":178260,"wastedBytes":75343,"wastedPercent":42.2658787778992}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":55848,"wastedBytes":46643,"wastedPercent":83.51654897791789}
- Avoid serving legacy JavaScript to modern browsers (Est savings of 10 KiB)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","wastedBytes":10645,"subItems":{"type":"subitems","items":[{"signal":"Array.prototype.at","location":{"type":"source-location","url"...
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":103...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":56305,"wastedBytes":5630.499...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11735,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":2576,"wastedBytes":241.0502793296088}
- Avoid an excessive DOM size (5,009 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":5009}}
    · {"node":{"type":"node","lhId":"1-117-SPAN","path":"1,HTML,1,BODY,10,DIV,4,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3411,"bottom":3425,"left":1219...
    · {"node":{"type":"node","lhId":"1-118-DIV","path":"1,HTML,1,BODY,10,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":821,"bottom":838,"left":-376,"right":9470,"w...
- Minimize main-thread work (2.2 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":1163.5189999999839}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":379.172}
    · {"group":"other","groupLabel":"Other","duration":344.70499999999623}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":200.94900000000248}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":88.87400000000012}
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-171-IMG","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":4313,"bott...

## best-practices — opportunities
- Uses deprecated APIs (2 warnings found)
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":1557}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4361,"bottom":4382,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-25-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4392,"bottom":4412,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-26-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4422,"bottom":4443,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-27-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":386,"right":45...
