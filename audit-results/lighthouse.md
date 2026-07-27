# Lighthouse (desktop) — 2026-07-27T16:21:47.566Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 79
- accessibility: 100
- best-practices: 81
- seo: 85

## performance — opportunities
- Total Blocking Time (270 ms)
- Cumulative Layout Shift (0.149)
    · {"cumulativeLayoutShiftMainFrame":0.1487523257892731,"newEngineResult":{"cumulativeLayoutShift":0.1487523257892731,"cumulativeLayoutShiftMainFrame":0.1487523257892731},"newEngineResultDiffered":false}
- Speed Index (1.6 s)
- Use efficient cache lifetimes (Est savings of 20 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/b0da9f4911ba/main.js?","cacheLifetimeMs":14400000,"wastedBytes":7112.119999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5363.199999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v4513226cdae34746b4dedf0b4dfa099e1781791509496","cacheLifetimeMs":86400000,"wastedBytes":4630.400000000001}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2257.6}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1171.4999999999998}
- Layout shift culprits
    · {"type":"table","headings":[{"key":"node","valueType":"node","subItemsHeading":{"key":"extra"},"label":"Element"},{"key":"score","valueType":"numeric","subItemsHeading":{"key":"cause","valueType":"text"},"granularity":0.001,"label":"Layout ...
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4748}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-12-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":86...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-18-SPAN","path":"1,HTML,1,BODY,9,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,...
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Max Potential First Input Delay (160 ms)
- Reduce unused CSS (Est savings of 15 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":15846,"wastedPercent":77.11527914884282,"totalBytes":20549}
- Reduce unused JavaScript (Est savings of 149 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":166394,"wastedBytes":69922,"wastedPercent":42.02165444194468}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":53281,"wastedBytes":44339,"wastedPercent":83.21725347038763}
    · {"url":"https://aiphantomtraders.com/","totalBytes":74359,"wastedBytes":38366,"wastedPercent":51.596378329387726}
- Avoid serving legacy JavaScript to modern browsers
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v4513226cdae34746b4dedf0b4dfa099e1781791509496","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":115...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":53632,"wastedBytes":5363.199...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11715,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":2528,"wastedBytes":236.55865921787694}
- Avoid an excessive DOM size (4,742 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4742}}
    · {"node":{"type":"node","lhId":"1-113-SPAN","path":"1,HTML,1,BODY,9,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219,...
    · {"node":{"type":"node","lhId":"1-114-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-323,"right":9470,"wi...
- Minimize main-thread work (2.1 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":861.7969999999731}
    · {"group":"other","groupLabel":"Other","duration":448.0699999999966}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":370.016}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":220.18900000000312}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":115.72700000000009}
- Avoid large layout shifts (3 layout shifts found)
    · {"node":{"type":"node","lhId":"page-3-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,1,DIV","selector":"body > div#page-landing > section.v2-hero > div.v2-hero-glow","boundingRect":{"top":-175,"bottom":625,"left":268,"right":1068,"width":800,"h...
    · {"node":{"type":"node","lhId":"page-7-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV,5,DIV","selector":"section.v2-hero > div.v2-tape > div#v2TapeTrack > div.v2-tape-item","boundingRect":{"top":847,"bottom":865,"left":390,"right":51...
    · {"node":{"type":"node","lhId":"page-1-IMG","path":"0,IMG","selector":"div#splashScreen > img","boundingRect":{"top":0,"bottom":0,"left":0,"right":0,"width":0,"height":0},"snippet":"<img src=\"logo.jpeg\" alt=\"Phantom Traders\" style=\"widt...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-178-IMG","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"botto...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":11222}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":11222}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-20-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-21-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3697,"bottom":3718,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-22-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3728,"bottom":3749,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3759,"bottom":3780,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":386,"right":457...
- robots.txt is not valid (1 error found)
    · {"index":"30","line":"Content-Signal: search=yes,ai-train=no,use=reference","message":"Unknown directive"}
