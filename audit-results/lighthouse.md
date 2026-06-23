# Lighthouse (desktop) — 2026-06-23T18:23:14.974Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 87
- accessibility: 94
- best-practices: 81
- seo: 85

## performance — opportunities
- Total Blocking Time (220 ms)
- Speed Index (1.8 s)
- Use efficient cache lifetimes (Est savings of 19 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/f95a7f38c08f/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6185.28}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5244.999999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","cacheLifetimeMs":86400000,"wastedBytes":4668.400000000001}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2285.6}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1088.7999999999997}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4745}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-15-DIV","path":"1,HTML,1,BODY,11,DIV,1,SECTION,4,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":8...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-16-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,5,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748...
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Max Potential First Input Delay (160 ms)
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":"/* ════════════════════════════════════════════════════════════════\n  DESIGN v2 — Phantom Traders (…","wastedBytes":15982,"wastedPercent":77.31239277317687,"totalBytes":20672}
- Reduce unused JavaScript (Est savings of 151 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":162680,"wastedBytes":68250,"wastedPercent":41.95354893816574}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":51988,"wastedBytes":43376,"wastedPercent":83.43478367326951}
    · {"url":"https://aiphantomtraders.com/","totalBytes":82736,"wastedBytes":43321,"wastedPercent":52.360918171594896}
- Avoid serving legacy JavaScript to modern browsers
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (3 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":116...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":52450,"wastedBytes":5244.999...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":10888,"wastedBytes":1...
- Avoid an excessive DOM size (4,739 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4739}}
    · {"node":{"type":"node","lhId":"1-120-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,5,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219...
    · {"node":{"type":"node","lhId":"1-121-DIV","path":"1,HTML,1,BODY,11,DIV,1,SECTION,4,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-347,"right":9645,"w...
- Minimize main-thread work (2.1 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":822.4609999999924}
    · {"group":"other","groupLabel":"Other","duration":474.868999999997}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":380.7529999999999}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":234.28600000000398}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":125.91400000000009}
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-184-IMG","path":"1,HTML,1,BODY,11,DIV,11,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"bot...

## accessibility — opportunities
- Background and foreground colors do not have a sufficient contrast ratio.
    · {"node":{"type":"node","lhId":"1-0-DIV","path":"1,HTML,1,BODY,60,DIV,0,DIV,0,DIV,1,DIV","selector":"div#checkoutDrawer > div.checkout-header > div > div#checkoutSubtitle","boundingRect":{"top":52,"bottom":70,"left":1358,"right":1433,"width"...
    · {"node":{"type":"node","lhId":"1-2-BUTTON","path":"1,HTML,1,BODY,60,DIV,0,DIV,1,BUTTON","selector":"body > div#checkoutDrawer > div.checkout-header > button","boundingRect":{"top":29,"bottom":59,"left":1640,"right":1713,"width":73,"height":...
    · {"node":{"type":"node","lhId":"1-3-DIV","path":"1,HTML,1,BODY,60,DIV,1,DIV,0,DIV","selector":"body > div#checkoutDrawer > div#cartItemsEl > div#cartEmpty","boundingRect":{"top":107,"bottom":267,"left":1358,"right":1713,"width":355,"height":...
    · {"node":{"type":"node","lhId":"1-4-BUTTON","path":"1,HTML,1,BODY,60,DIV,2,DIV,0,DIV,1,BUTTON","selector":"div#checkoutDrawer > div.checkout-footer > div > button","boundingRect":{"top":784,"bottom":819,"left":1649,"right":1713,"width":64,"h...
    · {"node":{"type":"node","lhId":"1-5-P","path":"1,HTML,1,BODY,60,DIV,2,DIV,5,P","selector":"body > div#checkoutDrawer > div.checkout-footer > p","boundingRect":{"top":884,"bottom":900,"left":1358,"right":1713,"width":355,"height":16},"snippet...
- Image elements have `[alt]` attributes that are redundant text.
    · {"node":{"type":"node","lhId":"1-9-IMG","path":"1,HTML,1,BODY,7,DIV,0,DIV,0,A,0,IMG","selector":"div#mobileMenu > div.mobile-menu-header > a.nav-logo > img.nav-logo-mark","boundingRect":{"top":18,"bottom":50,"left":1356,"right":1404,"width"...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":1751}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":1751}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-29-A","path":"1,HTML,1,BODY,11,DIV,11,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":271,"right":3...
    · {"node":{"type":"node","lhId":"1-30-A","path":"1,HTML,1,BODY,11,DIV,11,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3697,"bottom":3718,"left":271,"right":3...
    · {"node":{"type":"node","lhId":"1-31-A","path":"1,HTML,1,BODY,11,DIV,11,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3728,"bottom":3749,"left":271,"right":3...
    · {"node":{"type":"node","lhId":"1-32-A","path":"1,HTML,1,BODY,11,DIV,11,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3759,"bottom":3780,"left":271,"right":3...
    · {"node":{"type":"node","lhId":"1-33-A","path":"1,HTML,1,BODY,11,DIV,11,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":386,"right":4...
- robots.txt is not valid (1 error found)
    · {"index":"29","line":"Content-Signal: search=yes,ai-train=no","message":"Unknown directive"}
