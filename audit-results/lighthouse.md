# Lighthouse (desktop) — 2026-06-23T17:28:38.627Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 86
- accessibility: 95
- best-practices: 81
- seo: 85

## performance — opportunities
- First Contentful Paint (1.0 s)
- Total Blocking Time (220 ms)
- Speed Index (1.8 s)
- Use efficient cache lifetimes (Est savings of 19 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/f95a7f38c08f/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6060.839999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5237.899999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","cacheLifetimeMs":86400000,"wastedBytes":4660.8}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2284.8}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1152.5999999999997}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4745}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-13-DIV","path":"1,HTML,1,BODY,11,DIV,1,SECTION,4,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":8...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-14-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,5,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748...
- Network dependency tree
- Render blocking requests
    · {"url":"https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Barlow:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@400;500;600;700&family=Space+Grot...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","totalBytes":11526,"wastedMs":220}
- Max Potential First Input Delay (170 ms)
- Eliminate render-blocking resources (Est savings of 370 ms)
    · {"url":"https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Barlow:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@400;500;600;700&family=Space+Grot...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","totalBytes":11526,"wastedMs":220}
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":"/* ════════════════════════════════════════════════════════════════\n  DESIGN v2 — Phantom Traders (…","wastedBytes":15996,"wastedPercent":77.29602100671283,"totalBytes":20694}
- Reduce unused JavaScript (Est savings of 151 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":162683,"wastedBytes":68295,"wastedPercent":41.98034601728411}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":52024,"wastedBytes":43407,"wastedPercent":83.43478367326951}
    · {"url":"https://aiphantomtraders.com/","totalBytes":82808,"wastedBytes":43359,"wastedPercent":52.360918171594896}
- Avoid serving legacy JavaScript to modern browsers
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (3 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":116...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":52379,"wastedBytes":5237.899...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11526,"wastedBytes":1...
- Avoid an excessive DOM size (4,739 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4739}}
    · {"node":{"type":"node","lhId":"1-130-SPAN","path":"1,HTML,1,BODY,11,DIV,7,SECTION,0,DIV,1,DIV,5,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219...
    · {"node":{"type":"node","lhId":"1-131-DIV","path":"1,HTML,1,BODY,11,DIV,1,SECTION,4,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-338,"right":9654,"w...
- Minimize main-thread work (2.1 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":855.2949999999836}
    · {"group":"other","groupLabel":"Other","duration":463.72399999999897}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":349.84700000000026}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":210.83300000000287}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":124.16900000000018}
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-190-IMG","path":"1,HTML,1,BODY,4,NAV,0,DIV,0,A,0,IMG","selector":"nav#mainNav > div.v2-nav-inner > a.v2-nav-logo > img","boundingRect":{"top":13,"bottom":45,"le...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-191-IMG","path":"1,HTML,1,BODY,7,DIV,0,DIV,0,A,0,IMG","selector":"div#mobileMenu > div.mobile-menu-header > a.nav-logo > img.nav-logo-mark","boundingRect":{"top...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-195-IMG","path":"1,HTML,1,BODY,11,DIV,11,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"bot...

## accessibility — opportunities
- Background and foreground colors do not have a sufficient contrast ratio.
    · {"node":{"type":"node","lhId":"1-0-A","path":"1,HTML,1,BODY,7,DIV,1,DIV,0,A","selector":"body > div#mobileMenu > div.mobile-menu-body > a.mobile-menu-link","boundingRect":{"top":85,"bottom":135,"left":1356,"right":1635,"width":279,"height":...
    · {"node":{"type":"node","lhId":"1-2-A","path":"1,HTML,1,BODY,7,DIV,1,DIV,1,A","selector":"body > div#mobileMenu > div.mobile-menu-body > a.mobile-menu-link","boundingRect":{"top":137,"bottom":188,"left":1356,"right":1635,"width":279,"height"...
    · {"node":{"type":"node","lhId":"1-3-A","path":"1,HTML,1,BODY,7,DIV,1,DIV,2,A","selector":"body > div#mobileMenu > div.mobile-menu-body > a.mobile-menu-link","boundingRect":{"top":190,"bottom":240,"left":1356,"right":1635,"width":279,"height"...
    · {"node":{"type":"node","lhId":"1-4-A","path":"1,HTML,1,BODY,7,DIV,1,DIV,3,A","selector":"body > div#mobileMenu > div.mobile-menu-body > a.mobile-menu-link","boundingRect":{"top":242,"bottom":293,"left":1356,"right":1635,"width":279,"height"...
    · {"node":{"type":"node","lhId":"1-5-A","path":"1,HTML,1,BODY,7,DIV,1,DIV,4,A","selector":"body > div#mobileMenu > div.mobile-menu-body > a.mobile-menu-link","boundingRect":{"top":295,"bottom":345,"left":1356,"right":1635,"width":279,"height"...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":7571}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":7571}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-31-A","path":"1,HTML,1,BODY,4,NAV,0,DIV,0,A","selector":"body > nav#mainNav > div.v2-nav-inner > a.v2-nav-logo","boundingRect":{"top":13,"bottom":45,"left":40,"right":428,"width":389,"height":32},"snippet":"...
    · {"node":{"type":"node","lhId":"1-32-A","path":"1,HTML,1,BODY,4,NAV,0,DIV,1,DIV,0,A","selector":"nav#mainNav > div.v2-nav-inner > div.v2-nav-links > a","boundingRect":{"top":20,"bottom":37,"left":460,"right":494,"width":33,"height":18},"snip...
    · {"node":{"type":"node","lhId":"1-33-A","path":"1,HTML,1,BODY,4,NAV,0,DIV,1,DIV,1,A","selector":"nav#mainNav > div.v2-nav-inner > div.v2-nav-links > a","boundingRect":{"top":20,"bottom":37,"left":512,"right":579,"width":67,"height":18},"snip...
    · {"node":{"type":"node","lhId":"1-34-A","path":"1,HTML,1,BODY,4,NAV,0,DIV,1,DIV,2,A","selector":"nav#mainNav > div.v2-nav-inner > div.v2-nav-links > a","boundingRect":{"top":20,"bottom":37,"left":597,"right":655,"width":59,"height":18},"snip...
    · {"node":{"type":"node","lhId":"1-35-A","path":"1,HTML,1,BODY,4,NAV,0,DIV,1,DIV,3,A","selector":"nav#mainNav > div.v2-nav-inner > div.v2-nav-links > a","boundingRect":{"top":20,"bottom":37,"left":673,"right":749,"width":75,"height":18},"snip...
- robots.txt is not valid (1 error found)
    · {"index":"29","line":"Content-Signal: search=yes,ai-train=no","message":"Unknown directive"}
