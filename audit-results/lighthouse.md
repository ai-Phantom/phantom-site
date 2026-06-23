# Lighthouse (desktop) — 2026-06-23T17:35:37.848Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 65
- accessibility: 95
- best-practices: 81
- seo: 85

## performance — opportunities
- Largest Contentful Paint (1.2 s)
- Total Blocking Time (770 ms)
- Speed Index (2.4 s)
- Use efficient cache lifetimes (Est savings of 19 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/f95a7f38c08f/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6092.12}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5244.899999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","cacheLifetimeMs":86400000,"wastedBytes":4664.400000000001}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2285.6}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1088.6999999999998}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4745}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-19-DIV","path":"1,HTML,1,BODY,11,DIV,1,SECTION,4,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":8...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-20-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,5,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748...
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Time to Interactive (2.6 s)
- Max Potential First Input Delay (230 ms)
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":"/* ════════════════════════════════════════════════════════════════\n  DESIGN v2 — Phantom Traders (…","wastedBytes":16002,"wastedPercent":77.30011329824971,"totalBytes":20701}
- Reduce unused JavaScript (Est savings of 151 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":162680,"wastedBytes":68256,"wastedPercent":41.957107925236144}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":51988,"wastedBytes":43376,"wastedPercent":83.43478367326951}
    · {"url":"https://aiphantomtraders.com/","totalBytes":82839,"wastedBytes":43375,"wastedPercent":52.360918171594896}
- Avoid serving legacy JavaScript to modern browsers
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (3 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":116...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":52449,"wastedBytes":5244.899...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":10887,"wastedBytes":1...
- Avoid an excessive DOM size (4,739 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4739}}
    · {"node":{"type":"node","lhId":"1-129-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,5,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219...
    · {"node":{"type":"node","lhId":"1-130-DIV","path":"1,HTML,1,BODY,11,DIV,1,SECTION,4,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-366,"right":9626,"w...
- Reduce JavaScript execution time (1.3 s)
    · {"url":"https://aiphantomtraders.com/","total":1766.6999999999946,"scripting":654.4519999999986,"scriptParseCompile":27.54400000000001}
    · {"url":"Unattributable","total":485.0089999999974,"scripting":13.878000000000013,"scriptParseCompile":0}
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","total":458.9929999999992,"scripting":445.22399999999925,"scriptParseCompile":0.7170000000000001}
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","total":162.958999999999,"scripting":141.43699999999902,"scriptParseCompile":17.268}
- Minimize main-thread work (3.0 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":1304.8129999999883}
    · {"group":"other","groupLabel":"Other","duration":698.7670000000015}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":425.4959999999996}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":288.84399999999835}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":192.35699999999932}
- Largest Contentful Paint element (1,220 ms)
    · {"type":"table","headings":[{"key":"node","valueType":"node","label":"Element"}],"items":[{"node":{"type":"node","lhId":"page-0-H1","path":"1,HTML,1,BODY,11,DIV,1,SECTION,2,DIV,3,DIV,1,DIV,1,H1","selector":"div.v2-hero-inner > div.v2-hero-g...
    · {"type":"table","headings":[{"key":"phase","valueType":"text","label":"Phase"},{"key":"percent","valueType":"text","label":"% of LCP"},{"key":"timing","valueType":"ms","label":"Timing"}],"items":[{"phase":"TTFB","timing":281.967,"percent":"...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-190-IMG","path":"1,HTML,1,BODY,7,DIV,0,DIV,0,A,0,IMG","selector":"div#mobileMenu > div.mobile-menu-header > a.nav-logo > img.nav-logo-mark","boundingRect":{"top...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-194-IMG","path":"1,HTML,1,BODY,11,DIV,11,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"bot...

## accessibility — opportunities
- Background and foreground colors do not have a sufficient contrast ratio.
    · {"node":{"type":"node","lhId":"1-0-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,1,DIV,1,DIV,1,DIV,1,DIV,2,DIV,0,SPAN","selector":"div > div.v2-discord-embed > div.v2-discord-embed-body > span","boundingRect":{"top":2702,"bottom"...
    · {"node":{"type":"node","lhId":"1-2-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,1,DIV,1,DIV,1,DIV,1,DIV,4,DIV,1,SPAN","selector":"div > div.v2-discord-embed > div.v2-discord-embed-foot > span.v2-discord-embed-foot-link","boundin...
    · {"node":{"type":"node","lhId":"1-3-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,3,DIV,1,DIV,1,DIV,1,DIV,4,DIV,1,SPAN","selector":"div > div.v2-discord-embed > div.v2-discord-embed-foot > span.v2-discord-embed-foot-link","boundin...
    · {"node":{"type":"node","lhId":"1-5-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,5,DIV,1,DIV,1,DIV,1,DIV,4,DIV,1,SPAN","selector":"div > div.v2-discord-embed > div.v2-discord-embed-foot > span.v2-discord-embed-foot-link","boundin...
    · {"node":{"type":"node","lhId":"1-7-SPAN","path":"1,HTML,1,BODY,11,DIV,11,FOOTER,0,DIV,1,DIV,0,SPAN","selector":"footer.v2-footer > div.v2-footer-inner > div.v2-footer-bot > span","boundingRect":{"top":3962,"bottom":3978,"left":80,"right":34...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":7843}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":7843}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-31-A","path":"1,HTML,1,BODY,7,DIV,0,DIV,0,A","selector":"body > div#mobileMenu > div.mobile-menu-header > a.nav-logo","boundingRect":{"top":18,"bottom":50,"left":1356,"right":1562,"width":206,"height":32},"s...
    · {"node":{"type":"node","lhId":"1-32-A","path":"1,HTML,1,BODY,7,DIV,1,DIV,0,A","selector":"body > div#mobileMenu > div.mobile-menu-body > a.mobile-menu-link","boundingRect":{"top":85,"bottom":135,"left":1356,"right":1635,"width":279,"height"...
    · {"node":{"type":"node","lhId":"1-33-A","path":"1,HTML,1,BODY,7,DIV,1,DIV,1,A","selector":"body > div#mobileMenu > div.mobile-menu-body > a.mobile-menu-link","boundingRect":{"top":137,"bottom":188,"left":1356,"right":1635,"width":279,"height...
    · {"node":{"type":"node","lhId":"1-34-A","path":"1,HTML,1,BODY,7,DIV,1,DIV,2,A","selector":"body > div#mobileMenu > div.mobile-menu-body > a.mobile-menu-link","boundingRect":{"top":190,"bottom":240,"left":1356,"right":1635,"width":279,"height...
    · {"node":{"type":"node","lhId":"1-35-A","path":"1,HTML,1,BODY,7,DIV,1,DIV,3,A","selector":"body > div#mobileMenu > div.mobile-menu-body > a.mobile-menu-link","boundingRect":{"top":242,"bottom":293,"left":1356,"right":1635,"width":279,"height...
- robots.txt is not valid (1 error found)
    · {"index":"29","line":"Content-Signal: search=yes,ai-train=no","message":"Unknown directive"}
