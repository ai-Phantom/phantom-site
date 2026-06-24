# Lighthouse (desktop) — 2026-06-24T18:45:40.877Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 68
- accessibility: 95
- best-practices: 81
- seo: 85

## performance — opportunities
- Total Blocking Time (620 ms)
- Speed Index (2.3 s)
- Use efficient cache lifetimes (Est savings of 19 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/25e6c66701a0/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6047.24}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5277.299999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","cacheLifetimeMs":86400000,"wastedBytes":4668.400000000001}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2285.6}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1114.0999999999997}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4745}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-17-DIV","path":"1,HTML,1,BODY,6,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":86...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-18-SPAN","path":"1,HTML,1,BODY,6,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,...
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Max Potential First Input Delay (440 ms)
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":15880,"wastedPercent":77.11527914884282,"totalBytes":20592}
- Reduce unused JavaScript (Est savings of 147 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":162733,"wastedBytes":68292,"wastedPercent":41.965435034232165}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":52024,"wastedBytes":43407,"wastedPercent":83.43478367326951}
    · {"url":"https://aiphantomtraders.com/","totalBytes":74476,"wastedBytes":38486,"wastedPercent":51.675446497620804}
- Avoid serving legacy JavaScript to modern browsers
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (3 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":116...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":52773,"wastedBytes":5277.299...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11141,"wastedBytes":1...
- Avoid an excessive DOM size (4,739 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4739}}
    · {"node":{"type":"node","lhId":"1-119-SPAN","path":"1,HTML,1,BODY,6,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219,...
    · {"node":{"type":"node","lhId":"1-120-DIV","path":"1,HTML,1,BODY,6,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-386,"right":9579,"wi...
- Reduce JavaScript execution time (1.5 s)
    · {"url":"https://aiphantomtraders.com/","total":1302.828000000001,"scripting":385.8419999999993,"scriptParseCompile":26.075}
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","total":890.1249999999944,"scripting":887.1609999999944,"scriptParseCompile":0.5860000000000001}
    · {"url":"Unattributable","total":324.1309999999987,"scripting":7.497000000000001,"scriptParseCompile":0}
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","total":167.74099999999993,"scripting":149.92599999999993,"scriptParseCompile":15.481}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","total":116.48699999999998,"scripting":38.501999999999995,"scriptParseCompile":0.921}
- Minimize main-thread work (2.8 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":1493.319999999984}
    · {"group":"other","groupLabel":"Other","duration":621.1780000000016}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":367.4430000000002}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":183.4700000000022}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":128.44399999999982}
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-184-IMG","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"botto...

## accessibility — opportunities
- Background and foreground colors do not have a sufficient contrast ratio.
    · {"node":{"type":"node","lhId":"1-0-DIV","path":"1,HTML,1,BODY,28,DIV,0,DIV,0,DIV,1,DIV","selector":"div#checkoutDrawer > div.checkout-header > div > div#checkoutSubtitle","boundingRect":{"top":52,"bottom":70,"left":1358,"right":1433,"width"...
    · {"node":{"type":"node","lhId":"1-2-BUTTON","path":"1,HTML,1,BODY,28,DIV,0,DIV,1,BUTTON","selector":"body > div#checkoutDrawer > div.checkout-header > button","boundingRect":{"top":29,"bottom":59,"left":1640,"right":1713,"width":73,"height":...
    · {"node":{"type":"node","lhId":"1-3-DIV","path":"1,HTML,1,BODY,28,DIV,1,DIV,0,DIV","selector":"body > div#checkoutDrawer > div#cartItemsEl > div#cartEmpty","boundingRect":{"top":107,"bottom":267,"left":1358,"right":1713,"width":355,"height":...
    · {"node":{"type":"node","lhId":"1-4-BUTTON","path":"1,HTML,1,BODY,28,DIV,2,DIV,0,DIV,1,BUTTON","selector":"div#checkoutDrawer > div.checkout-footer > div > button","boundingRect":{"top":784,"bottom":819,"left":1649,"right":1713,"width":64,"h...
    · {"node":{"type":"node","lhId":"1-5-P","path":"1,HTML,1,BODY,28,DIV,2,DIV,4,P","selector":"body > div#checkoutDrawer > div.checkout-footer > p","boundingRect":{"top":884,"bottom":900,"left":1358,"right":1713,"width":355,"height":16},"snippet...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":7712}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":7712}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-28-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-29-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3697,"bottom":3718,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-30-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3728,"bottom":3749,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-31-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3759,"bottom":3780,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-32-A","path":"1,HTML,1,BODY,6,DIV,5,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":386,"right":457...
- robots.txt is not valid (1 error found)
    · {"index":"29","line":"Content-Signal: search=yes,ai-train=no","message":"Unknown directive"}
