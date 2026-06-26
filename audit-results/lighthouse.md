# Lighthouse (desktop) — 2026-06-26T20:26:23.280Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 66
- accessibility: 100
- best-practices: 81
- seo: 85

## performance — opportunities
- Total Blocking Time (490 ms)
- Cumulative Layout Shift (0.149)
    · {"cumulativeLayoutShiftMainFrame":0.14867033229739418,"newEngineResult":{"cumulativeLayoutShift":0.14867033229739418,"cumulativeLayoutShiftMainFrame":0.14867033229739418},"newEngineResultDiffered":false}
- Speed Index (2.2 s)
- Use efficient cache lifetimes (Est savings of 19 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/25e6c66701a0/main.js?","cacheLifetimeMs":14400000,"wastedBytes":5907.839999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5244.899999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","cacheLifetimeMs":86400000,"wastedBytes":4668.400000000001}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2285.6}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1088.6999999999998}
- Layout shift culprits
    · {"type":"table","headings":[{"key":"node","valueType":"node","subItemsHeading":{"key":"extra"},"label":"Element"},{"key":"score","valueType":"numeric","subItemsHeading":{"key":"cause","valueType":"text"},"granularity":0.001,"label":"Layout ...
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4745}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-11-DIV","path":"1,HTML,1,BODY,6,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":86...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-17-SPAN","path":"1,HTML,1,BODY,6,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,...
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Max Potential First Input Delay (210 ms)
- Reduce unused CSS (Est savings of 15 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":15836,"wastedPercent":77.11527914884282,"totalBytes":20536}
- Reduce unused JavaScript (Est savings of 148 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":163975,"wastedBytes":69528,"wastedPercent":42.40142047338063}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":51988,"wastedBytes":43376,"wastedPercent":83.43478367326951}
    · {"url":"https://aiphantomtraders.com/","totalBytes":74309,"wastedBytes":38341,"wastedPercent":51.596378329387726}
- Avoid serving legacy JavaScript to modern browsers
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":116...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":52449,"wastedBytes":5244.899...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":10887,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":2507,"wastedBytes":234.59357541899428}
- Avoid an excessive DOM size (4,739 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4739}}
    · {"node":{"type":"node","lhId":"1-112-SPAN","path":"1,HTML,1,BODY,6,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219,...
    · {"node":{"type":"node","lhId":"1-113-DIV","path":"1,HTML,1,BODY,6,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-338,"right":9614,"wi...
- Minimize main-thread work (2.5 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":1057.708}
    · {"group":"other","groupLabel":"Other","duration":559.9200000000033}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":498.6999999999999}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":220.7250000000038}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":121.25400000000009}
- Avoid large layout shifts (3 layout shifts found)
    · {"node":{"type":"node","lhId":"page-2-DIV","path":"1,HTML,1,BODY,6,DIV,0,SECTION,1,DIV","selector":"body > div#page-landing > section.v2-hero > div.v2-hero-glow","boundingRect":{"top":-175,"bottom":625,"left":268,"right":1068,"width":800,"h...
    · {"node":{"type":"node","lhId":"page-7-DIV","path":"1,HTML,1,BODY,6,DIV,0,SECTION,3,DIV,0,DIV,6,DIV","selector":"section.v2-hero > div.v2-tape > div#v2TapeTrack > div.v2-tape-item","boundingRect":{"top":847,"bottom":865,"left":542,"right":67...
    · {"node":{"type":"node","lhId":"page-1-DIV","path":"1,DIV","selector":"div#splashScreen > div","boundingRect":{"top":0,"bottom":0,"left":0,"right":0,"width":0,"height":0},"snippet":"<div style=\"margin-top: 20px; width: 120px; height: 2px; b...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-177-IMG","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"botto...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":1921}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":1921}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-19-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-20-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3697,"bottom":3718,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-21-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3728,"bottom":3749,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-22-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3759,"bottom":3780,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":386,"right":457...
- robots.txt is not valid (1 error found)
    · {"index":"29","line":"Content-Signal: search=yes,ai-train=no","message":"Unknown directive"}
