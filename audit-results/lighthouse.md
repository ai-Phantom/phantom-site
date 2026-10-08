# Lighthouse (desktop) — 2026-10-08T20:50:16.512Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 71
- accessibility: 100
- best-practices: 81
- seo: 92

## performance — opportunities
- Total Blocking Time (600 ms)
- Speed Index (1.8 s)
- Use efficient cache lifetimes (Est savings of 21 KiB)
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/4df4a60fa397/main.js?","cacheLifetimeMs":14400000,"wastedBytes":8259.279999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5672.499999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v4bc70e2c01a94c73b74392e4234840661791215815920","cacheLifetimeMs":86400000,"wastedBytes":4175.2}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2256}
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","cacheLifetimeMs":604800000,"wastedBytes":1197.8999999999996}
- Optimize DOM size
    · {"statistic":"Total elements","value":{"type":"numeric","granularity":1,"value":4994}}
    · {"statistic":"Most children","node":{"type":"node","lhId":"page-17-DIV","path":"1,HTML,1,BODY,10,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":821,"bottom":8...
    · {"statistic":"DOM depth","node":{"type":"node","lhId":"page-18-SPAN","path":"1,HTML,1,BODY,10,DIV,4,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3411...
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Max Potential First Input Delay (380 ms)
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":16477,"wastedPercent":76.04543107898813,"totalBytes":21667}
- Reduce unused JavaScript (Est savings of 119 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":180351,"wastedBytes":74626,"wastedPercent":41.37830899217236}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":55982,"wastedBytes":46753,"wastedPercent":83.51367825732264}
- Avoid serving legacy JavaScript to modern browsers (Est savings of 10 KiB)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v4bc70e2c01a94c73b74392e4234840661791215815920","wastedBytes":10431,"subItems":{"type":"subitems","items":[{"signal":"Array.prototype.at","location":{"type":"source-location","url"...
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (4 resources found)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v4bc70e2c01a94c73b74392e4234840661791215815920","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":104...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":56725,"wastedBytes":5672.499...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11979,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":1734,"wastedBytes":162.25977653631276}
- Avoid an excessive DOM size (4,988 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4988}}
    · {"node":{"type":"node","lhId":"1-117-SPAN","path":"1,HTML,1,BODY,10,DIV,4,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3411,"bottom":3425,"left":1219...
    · {"node":{"type":"node","lhId":"1-118-DIV","path":"1,HTML,1,BODY,10,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":821,"bottom":838,"left":-366,"right":9468,"w...
- Reduce JavaScript execution time (1.4 s)
    · {"url":"https://aiphantomtraders.com/","total":1213.5720000000003,"scripting":460.2039999999986,"scriptParseCompile":19.461000000000006}
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","total":757.8729999999955,"scripting":751.0259999999955,"scriptParseCompile":0.517}
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","total":187.232999999999,"scripting":175.190999999999,"scriptParseCompile":10.084999999999999}
    · {"url":"Unattributable","total":165.55399999999705,"scripting":6.879999999999995,"scriptParseCompile":0}
- Minimize main-thread work (2.4 s)
    · {"group":"scriptEvaluation","groupLabel":"Script Evaluation","duration":1425.5089999999861}
    · {"group":"other","groupLabel":"Other","duration":389.77299999999696}
    · {"group":"styleLayout","groupLabel":"Style & Layout","duration":228.66800000000003}
    · {"group":"paintCompositeRender","groupLabel":"Rendering","duration":177.08700000000226}
    · {"group":"parseHTML","groupLabel":"Parse HTML & CSS","duration":105.75899999999996}
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-170-IMG","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":4313,"bott...

## best-practices — opportunities
- Uses deprecated APIs (2 warnings found)
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":12194}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4361,"bottom":4382,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-25-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4392,"bottom":4412,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-26-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4422,"bottom":4443,"left":271,"right":33...
    · {"node":{"type":"node","lhId":"1-27-A","path":"1,HTML,1,BODY,10,DIV,6,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":386,"right":45...
