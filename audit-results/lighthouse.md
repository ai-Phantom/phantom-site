# Lighthouse (desktop) — 2026-10-02T05:06:28.958Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 72
- accessibility: 100
- best-practices: 81
- seo: 92

## performance — opportunities
- Largest Contentful Paint (1.2 s)
- Total Blocking Time (520 ms)
- Speed Index (1.9 s)
- Use efficient cache lifetimes (Est savings of 20 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/d76008a69eab/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6736.079999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5622.699999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","cacheLifetimeMs":86400000,"wastedBytes":4135.2}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2242.4}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1237.7999999999997}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4861}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-18-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":86...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-19-SPAN","path":"1,HTML,1,BODY,9,DIV,4,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3411,...
- Network dependency tree
- Max Potential First Input Delay (250 ms)
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":16229,"wastedPercent":75.72829854709049,"totalBytes":21430}
- Reduce unused JavaScript (Est savings of 157 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":178257,"wastedBytes":75413,"wastedPercent":42.30566995937598}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":55884,"wastedBytes":46673,"wastedPercent":83.51654897791789}
    · {"url":"https://aiphantomtraders.com/","totalBytes":73135,"wastedBytes":38820,"wastedPercent":53.07959716707934}
- Avoid serving legacy JavaScript to modern browsers (Est savings of 10 KiB)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","wastedBytes":10645,"subItems":{"type":"subitems","items":[{"signal":"Array.prototype.at","location":{"type":"source-location","url"...
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":103...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":56227,"wastedBytes":5622.699...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":12378,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":1727,"wastedBytes":161.60474860335185}
- Avoid an excessive DOM size (4,855 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4855}}
    · {"node":{"type":"node","lhId":"1-114-SPAN","path":"1,HTML,1,BODY,9,DIV,4,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3411,"bottom":3425,"left":1219,...
    · {"node":{"type":"node","lhId":"1-115-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-358,"right":9489,"wi...
- Minimize main-thread work (2.2 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":1089.4199999999767}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":368.9179999999997}
    · {"group":"other","groupLabel":"Other","duration":332.1379999999978}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":215.83700000000377}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":117.77700000000011}
- Largest Contentful Paint element (1,230 ms)
    · {"type":"table","headings":[{"key":"node","valueType":"node","label":"Element"}],"items":[{"node":{"type":"node","lhId":"page-0-H1","path":"1,HTML,1,BODY,9,DIV,0,SECTION,2,DIV,1,DIV,0,DIV,1,H1","selector":"div.v2-hero-inner > div.v2-hero-gr...
    · {"type":"table","headings":[{"key":"phase","valueType":"text","label":"Phase"},{"key":"percent","valueType":"text","label":"% of LCP"},{"key":"timing","valueType":"ms","label":"Timing"}],"items":[{"phase":"TTFB","timing":556.564,"percent":"...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-177-IMG","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":4313,"botto...

## best-practices — opportunities
- Uses deprecated APIs (2 warnings found)
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":11502}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-21-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-22-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4361,"bottom":4381,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4391,"bottom":4412,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4422,"bottom":4443,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-25-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":386,"right":457...
