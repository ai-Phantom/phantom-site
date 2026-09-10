# Lighthouse (desktop) — 2026-09-10T21:35:11.156Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 74
- accessibility: 100
- best-practices: 81
- seo: 85

## performance — opportunities
- Total Blocking Time (530 ms)
- Speed Index (1.9 s)
- Use efficient cache lifetimes (Est savings of 20 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/330e41bb475c/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6823.799999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5661.399999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","cacheLifetimeMs":86400000,"wastedBytes":4135.2}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2258.4}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1151.8999999999996}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4748}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-18-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":86...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-19-SPAN","path":"1,HTML,1,BODY,9,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,...
- Network dependency tree
- Max Potential First Input Delay (410 ms)
- Reduce unused CSS (Est savings of 15 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":15851,"wastedPercent":77.11527914884282,"totalBytes":20555}
- Reduce unused JavaScript (Est savings of 156 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":174887,"wastedBytes":74626,"wastedPercent":42.670782846020316}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":55879,"wastedBytes":46620,"wastedPercent":83.42894000109787}
    · {"url":"https://aiphantomtraders.com/","totalBytes":74379,"wastedBytes":38377,"wastedPercent":51.596378329387726}
- Avoid serving legacy JavaScript to modern browsers (Est savings of 10 KiB)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","wastedBytes":10645,"subItems":{"type":"subitems","items":[{"signal":"Array.prototype.at","location":{"type":"source-location","url"...
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":103...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":56614,"wastedBytes":5661.399...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11519,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":1750,"wastedBytes":163.75698324022338}
- Avoid an excessive DOM size (4,742 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4742}}
    · {"node":{"type":"node","lhId":"1-113-SPAN","path":"1,HTML,1,BODY,9,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219,...
    · {"node":{"type":"node","lhId":"1-114-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-354,"right":9493,"wi...
- Reduce JavaScript execution time (1.4 s)
    · {"url":"https://aiphantomtraders.com/","total":986.1740000000005,"scripting":357.4269999999987,"scriptParseCompile":12.211999999999998}
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","total":828.2969999999833,"scripting":825.9899999999832,"scriptParseCompile":0.323}
    · {"url":"Unattributable","total":228.43099999999964,"scripting":112.03800000000001,"scriptParseCompile":0}
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","total":68.8329999999998,"scripting":61.94599999999979,"scriptParseCompile":6.692}
- Minimize main-thread work (2.2 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":1390.6919999999677}
    · {"group":"other","groupLabel":"Other","duration":268.7810000000005}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":250.89800000000008}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":114.4490000000015}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":102.2770000000001}
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-178-IMG","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"botto...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":11564}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":11564}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-20-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-21-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3697,"bottom":3718,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-22-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3728,"bottom":3749,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3759,"bottom":3780,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":386,"right":457...
- robots.txt is not valid (1 error found)
    · {"index":"30","line":"Content-Signal: search=yes,ai-train=no,use=reference","message":"Unknown directive"}
