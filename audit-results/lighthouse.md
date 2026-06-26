# Lighthouse (desktop) — 2026-06-26T20:20:08.030Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 79
- accessibility: 100
- best-practices: 81
- seo: 85

## performance — opportunities
- Largest Contentful Paint (1.2 s)
- Total Blocking Time (320 ms)
- Speed Index (2.0 s)
- Use efficient cache lifetimes (Est savings of 19 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/25e6c66701a0/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6219.959999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5211.0999999999985}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","cacheLifetimeMs":86400000,"wastedBytes":4668.400000000001}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2271.2000000000003}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1122.5999999999997}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4745}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-15-DIV","path":"1,HTML,1,BODY,6,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":86...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-16-SPAN","path":"1,HTML,1,BODY,6,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,...
- Network dependency tree
- Max Potential First Input Delay (200 ms)
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":15890,"wastedPercent":77.11527914884282,"totalBytes":20606}
- Reduce unused JavaScript (Est savings of 147 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":163321,"wastedBytes":68970,"wastedPercent":42.22965937205835}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":51988,"wastedBytes":43376,"wastedPercent":83.43478367326951}
    · {"url":"https://aiphantomtraders.com/","totalBytes":74562,"wastedBytes":38472,"wastedPercent":51.596378329387726}
- Avoid serving legacy JavaScript to modern browsers
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":116...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":52111,"wastedBytes":5211.099...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11226,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":2492,"wastedBytes":233.18994413407808}
- Avoid an excessive DOM size (4,739 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4739}}
    · {"node":{"type":"node","lhId":"1-112-SPAN","path":"1,HTML,1,BODY,6,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219,...
    · {"node":{"type":"node","lhId":"1-113-DIV","path":"1,HTML,1,BODY,6,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-330,"right":9623,"wi...
- Minimize main-thread work (2.2 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":958.4479999999859}
    · {"group":"other","groupLabel":"Other","duration":524.9349999999962}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":339.02299999999997}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":207.407000000003}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":145.21900000000005}
- Largest Contentful Paint element (1,200 ms)
    · {"type":"table","headings":[{"key":"node","valueType":"node","label":"Element"}],"items":[{"node":{"type":"node","lhId":"page-0-H1","path":"1,HTML,1,BODY,6,DIV,0,SECTION,2,DIV,1,DIV,0,DIV,1,H1","selector":"div.v2-hero-inner > div.v2-hero-gr...
    · {"type":"table","headings":[{"key":"phase","valueType":"text","label":"Phase"},{"key":"percent","valueType":"text","label":"% of LCP"},{"key":"timing","valueType":"ms","label":"Timing"}],"items":[{"phase":"TTFB","timing":463.018,"percent":"...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-177-IMG","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"botto...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":1716}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":1716}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-19-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-20-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3697,"bottom":3718,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-21-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3728,"bottom":3749,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-22-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3759,"bottom":3780,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":386,"right":457...
- robots.txt is not valid (1 error found)
    · {"index":"29","line":"Content-Signal: search=yes,ai-train=no","message":"Unknown directive"}
