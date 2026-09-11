# Lighthouse (desktop) — 2026-09-11T03:19:24.742Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 61
- accessibility: 100
- best-practices: 81
- seo: 85

## performance — opportunities
- Largest Contentful Paint (1.2 s)
- Total Blocking Time (1,240 ms)
- Speed Index (2.7 s)
- Use efficient cache lifetimes (Est savings of 19 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/330e41bb475c/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6653.119999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5623.499999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","cacheLifetimeMs":86400000,"wastedBytes":4146.8}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2253.6}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1191.9999999999998}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4748}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-20-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":86...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-21-SPAN","path":"1,HTML,1,BODY,9,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,...
- Network dependency tree
- Time to Interactive (3.1 s)
- Max Potential First Input Delay (420 ms)
- Reduce unused CSS (Est savings of 15 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":15851,"wastedPercent":77.11527914884282,"totalBytes":20555}
- Reduce unused JavaScript (Est savings of 156 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":174914,"wastedBytes":74505,"wastedPercent":42.59541341988029}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":55888,"wastedBytes":46627,"wastedPercent":83.42894000109787}
    · {"url":"https://aiphantomtraders.com/","totalBytes":74379,"wastedBytes":38377,"wastedPercent":51.596378329387726}
- Avoid serving legacy JavaScript to modern browsers (Est savings of 10 KiB)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","wastedBytes":10675,"subItems":{"type":"subitems","items":[{"signal":"Array.prototype.at","location":{"type":"source-location","url"...
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":103...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":56235,"wastedBytes":5623.499...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11920,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":1729,"wastedBytes":161.7918994413407}
- Avoid an excessive DOM size (4,742 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4742}}
    · {"node":{"type":"node","lhId":"1-113-SPAN","path":"1,HTML,1,BODY,9,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219,...
    · {"node":{"type":"node","lhId":"1-114-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-448,"right":9398,"wi...
- Reduce JavaScript execution time (1.9 s)
    · {"url":"https://aiphantomtraders.com/","total":2147.326000000004,"scripting":859.7559999999992,"scriptParseCompile":28.554999999999996}
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","total":802.145999999983,"scripting":793.2019999999831,"scriptParseCompile":0.41800000000000004}
    · {"url":"Unattributable","total":358.9299999999979,"scripting":2.929999999999999,"scriptParseCompile":0}
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","total":222.7629999999984,"scripting":207.75999999999843,"scriptParseCompile":14.540999999999999}
- Minimize main-thread work (3.6 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":1897.1539999999554}
    · {"group":"other","groupLabel":"Other","duration":777.0550000000064}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":304.84500000000014}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":283.40700000000004}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":261.80500000000416}
- Largest Contentful Paint element (1,240 ms)
    · {"type":"table","headings":[{"key":"node","valueType":"node","label":"Element"}],"items":[{"node":{"type":"node","lhId":"page-0-H1","path":"1,HTML,1,BODY,9,DIV,0,SECTION,2,DIV,1,DIV,0,DIV,1,H1","selector":"div.v2-hero-inner > div.v2-hero-gr...
    · {"type":"table","headings":[{"key":"phase","valueType":"text","label":"Phase"},{"key":"percent","valueType":"text","label":"% of LCP"},{"key":"timing","valueType":"ms","label":"Timing"}],"items":[{"phase":"TTFB","timing":390.3880000000149,"...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-178-IMG","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"botto...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":3642}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":3642}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-20-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-21-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3697,"bottom":3718,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-22-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3728,"bottom":3749,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3759,"bottom":3780,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":386,"right":457...
- robots.txt is not valid (1 error found)
    · {"index":"30","line":"Content-Signal: search=yes,ai-train=no,use=reference","message":"Unknown directive"}
