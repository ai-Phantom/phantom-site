# Lighthouse (desktop) — 2026-09-23T13:56:17.963Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 91
- accessibility: 98
- best-practices: 78
- seo: 92

## performance — opportunities
- Total Blocking Time (230 ms)
- Use efficient cache lifetimes (Est savings of 19 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/330e41bb475c/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6707.5199999999995}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5630.799999999998}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","cacheLifetimeMs":86400000,"wastedBytes":4135.2}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2257.6}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1128.1999999999998}
- LCP request discovery
    · {"type":"checklist","items":{"priorityHinted":{"label":"fetchpriority=high should be applied","value":false},"requestDiscoverable":{"label":"Request is discoverable in initial document","value":true},"eagerlyLoaded":{"label":"lazy load not ...
    · {"type":"node","lhId":"page-0-IMG","path":"0,IMG","selector":"div#splashScreen > img","boundingRect":{"top":0,"bottom":0,"left":0,"right":0,"width":0,"height":0},"snippet":"<img src=\"logo.jpeg\" alt=\"Phantom Traders\" style=\"width:120px;...
- Network dependency tree
- Max Potential First Input Delay (190 ms)
- Reduce unused CSS (Est savings of 19 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":19748,"wastedPercent":92.47273893521488,"totalBytes":21356}
- Reduce unused JavaScript (Est savings of 154 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":175692,"wastedBytes":72579,"wastedPercent":41.31019100995082}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":55848,"wastedBytes":46643,"wastedPercent":83.51654897791789}
    · {"url":"https://aiphantomtraders.com/","totalBytes":75070,"wastedBytes":38863,"wastedPercent":51.76849852498403}
- Avoid serving legacy JavaScript to modern browsers (Est savings of 10 KiB)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","wastedBytes":10645,"subItems":{"type":"subitems","items":[{"signal":"Array.prototype.at","location":{"type":"source-location","url"...
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":103...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":56308,"wastedBytes":5630.799...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11282,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":1750,"wastedBytes":163.75698324022338}
- Avoid an excessive DOM size (3,756 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":3756}}
    · {"node":{"type":"node","lhId":"1-99-SPAN","path":"1,HTML,1,BODY,19,DIV,1,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":0,"bottom":0,"left":0,"right":0...
    · {"node":{"type":"node","lhId":"1-100-BODY","path":"1,HTML,1,BODY","selector":"body","boundingRect":{"top":0,"bottom":26,"left":0,"right":1350,"width":1350,"height":26},"snippet":"<body>","nodeLabel":"body"},"statistic":"Maximum Child Elemen...

## accessibility — opportunities
- Skip links are not focusable.
    · {"node":{"type":"node","lhId":"1-1-A","path":"1,HTML,1,BODY,1,A","selector":"body > a.skip-link","boundingRect":{"top":0,"bottom":41,"left":-9999,"right":-9811,"width":188,"height":41},"snippet":"<a href=\"#main-content\" class=\"skip-link\...

## best-practices — opportunities
- Uses deprecated APIs (2 warnings found)
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":11202}}
- Browser errors were logged to the console
    · {"source":"exception","description":"SyntaxError: Unexpected token '}'","sourceLocation":{"type":"source-location","url":"https://aiphantomtraders.com/","urlProvider":"network","line":15,"column":107318}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-28-A","path":"1,HTML,1,BODY,9,DIV,0,NAV,0,A","selector":"body > div#page-login > nav#authNav > a.nav-logo","boundingRect":{"top":0,"bottom":0,"left":0,"right":0,"width":0,"height":0},"snippet":"<a class=\"na...
    · {"node":{"type":"node","lhId":"1-29-A","path":"1,HTML,1,BODY,9,DIV,0,NAV,1,DIV,1,A","selector":"div#page-login > nav#authNav > div > a","boundingRect":{"top":0,"bottom":0,"left":0,"right":0,"width":0,"height":0},"snippet":"<a onclick=\"show...
    · {"node":{"type":"node","lhId":"1-30-A","path":"1,HTML,1,BODY,9,DIV,0,NAV,2,DIV,0,SPAN,1,A","selector":"nav#authNav > div > span > a","boundingRect":{"top":0,"bottom":0,"left":0,"right":0,"width":0,"height":0},"snippet":"<a onclick=\"showPag...
    · {"node":{"type":"node","lhId":"1-31-A","path":"1,HTML,1,BODY,9,DIV,0,NAV,2,DIV,0,SPAN,3,A","selector":"nav#authNav > div > span > a","boundingRect":{"top":0,"bottom":0,"left":0,"right":0,"width":0,"height":0},"snippet":"<a onclick=\"showPag...
    · {"node":{"type":"node","lhId":"1-32-A","path":"1,HTML,1,BODY,9,DIV,1,DIV,0,DIV,7,DIV,0,LABEL,1,A","selector":"div.auth-card > div.form-group > label.form-label > a","boundingRect":{"top":0,"bottom":0,"left":0,"right":0,"width":0,"height":0}...
