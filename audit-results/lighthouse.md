# Lighthouse (desktop) — 2026-06-29T16:55:09.022Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 93
- accessibility: 100
- best-practices: 81
- seo: 85

## performance — opportunities
- Cumulative Layout Shift (0.143)
    · {"cumulativeLayoutShiftMainFrame":0.14305254212475857,"newEngineResult":{"cumulativeLayoutShift":0.14305254212475857,"cumulativeLayoutShiftMainFrame":0.14305254212475857},"newEngineResultDiffered":false}
- Use efficient cache lifetimes (Est savings of 19 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/25e6c66701a0/main.js?","cacheLifetimeMs":14400000,"wastedBytes":5684.799999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5237.899999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","cacheLifetimeMs":86400000,"wastedBytes":4668.8}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2285.6}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1153.4999999999998}
- Layout shift culprits
    · {"type":"table","headings":[{"key":"node","valueType":"node","subItemsHeading":{"key":"extra"},"label":"Element"},{"key":"score","valueType":"numeric","subItemsHeading":{"key":"cause","valueType":"text"},"granularity":0.001,"label":"Layout ...
- Network dependency tree
- Reduce unused CSS (Est savings of 15 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":15854,"wastedPercent":77.11527914884282,"totalBytes":20559}
- Reduce unused JavaScript (Est savings of 148 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":163976,"wastedBytes":69469,"wastedPercent":42.365187267818776}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":52024,"wastedBytes":43407,"wastedPercent":83.43478367326951}
    · {"url":"https://aiphantomtraders.com/","totalBytes":74395,"wastedBytes":38385,"wastedPercent":51.596378329387726}
- Avoid serving legacy JavaScript to modern browsers
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":116...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":52379,"wastedBytes":5237.899...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11535,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":2517,"wastedBytes":235.5293296089384}
- Avoid an excessive DOM size (4,742 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4742}}
    · {"node":{"type":"node","lhId":"1-113-SPAN","path":"1,HTML,1,BODY,9,DIV,3,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":2748,"bottom":2762,"left":1219,...
    · {"node":{"type":"node","lhId":"1-114-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-267,"right":9699,"wi...
- Avoid large layout shifts (4 layout shifts found)
    · {"node":{"type":"node","lhId":"page-1-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,1,DIV","selector":"body > div#page-landing > section.v2-hero > div.v2-hero-glow","boundingRect":{"top":-175,"bottom":625,"left":268,"right":1068,"width":800,"h...
    · {"node":{"type":"node","lhId":"page-4-DIV","path":"1,HTML,1,BODY,4,NAV,0,DIV,4,DIV","selector":"body > nav#mainNav > div.v2-nav-inner > div.v2-nav-cta","boundingRect":{"top":12,"bottom":45,"left":1083,"right":1332,"width":250,"height":33},"...
    · {"node":{"type":"node","lhId":"page-9-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV,7,DIV","selector":"section.v2-hero > div.v2-tape > div#v2TapeTrack > div.v2-tape-item","boundingRect":{"top":847,"bottom":865,"left":790,"right":91...
    · {"node":{"type":"node","lhId":"page-6-DIV","path":"1,DIV","selector":"div#splashScreen > div","boundingRect":{"top":0,"bottom":0,"left":0,"right":0,"width":0,"height":0},"snippet":"<div style=\"margin-top: 20px; width: 120px; height: 2px; b...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-178-IMG","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":3649,"botto...

## best-practices — opportunities
- Uses deprecated APIs (3 warnings found)
    · {"value":"SharedStorage","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":1533}}
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":1533}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-20-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-21-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3697,"bottom":3718,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-22-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3728,"bottom":3749,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3759,"bottom":3780,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,9,DIV,5,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":3667,"bottom":3687,"left":386,"right":457...
- robots.txt is not valid (1 error found)
    · {"index":"29","line":"Content-Signal: search=yes,ai-train=no","message":"Unknown directive"}
