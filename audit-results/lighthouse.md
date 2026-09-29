# Lighthouse (desktop) — 2026-09-29T03:46:15.478Z

URL: https://aiphantomtraders.com/

## Scores
- performance: 98
- accessibility: 100
- best-practices: 81
- seo: 92

## performance — opportunities
- Use efficient cache lifetimes (Est savings of 32 KiB)
    · {"url":"https://fonts.gstatic.com/l/font?kit=tDbv2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yKwBNntkaToggR7BYXHKPxDcwgknk-4&skey=48ad01c60053c2ae&v=v24","cacheLifetimeMs":86400000,"wastedBytes":12667.2}
    · {"url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/d76008a69eab/main.js?","cacheLifetimeMs":14400000,"wastedBytes":6659.919999999999}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","cacheLifetimeMs":604800000,"wastedBytes":5662.499999999999}
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","cacheLifetimeMs":86400000,"wastedBytes":4135.2}
    · {"url":"https://js.sentry-cdn.com/6eb1dc678aa80aa6854d7acfbe8c4056.min.js","cacheLifetimeMs":3600000,"wastedBytes":2257.6}
- Forced reflow
    · {"type":"table","headings":[{"key":"source","valueType":"source-location","label":"Source"},{"key":"reflowTime","valueType":"ms","granularity":1,"label":"Total reflow time"}],"items":[{"source":{"type":"text","value":"[unattributed]"},"refl...
- Network dependency tree
- Reduce unused CSS (Est savings of 16 KiB)
    · {"url":":root{--bg-base:#0a0c0f;--bg-elev-1:#14161a;--bg-elev-2:#1c1f25;--bg-elev-3:#262a31;--reactor-blue:…","wastedBytes":15935,"wastedPercent":75.37203335471456,"totalBytes":21142}
- Reduce unused JavaScript (Est savings of 156 KiB)
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","totalBytes":177007,"wastedBytes":74513,"wastedPercent":42.09626564472396}
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","totalBytes":55884,"wastedBytes":46673,"wastedPercent":83.51654897791789}
    · {"url":"https://aiphantomtraders.com/","totalBytes":74318,"wastedBytes":38474,"wastedPercent":51.76849852498403}
- Avoid serving legacy JavaScript to modern browsers (Est savings of 10 KiB)
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","wastedBytes":10645,"subItems":{"type":"subitems","items":[{"signal":"Array.prototype.at","location":{"type":"source-location","url"...
    · {"url":"https://www.googletagmanager.com/gtag/js?id=G-T8NHESJZ90","wastedBytes":0,"subItems":{"type":"subitems","items":[{"signal":"@babel/plugin-transform-regenerator","location":{"type":"source-location","url":"https://www.googletagmanage...
- Serve static assets with an efficient cache policy (5 resources found)
    · {"url":"https://fonts.gstatic.com/l/font?kit=tDbv2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yKwBNntkaToggR7BYXHKPxDcwgknk-4&skey=48ad01c60053c2ae&v=v24","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cac...
    · {"url":"https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495","debugData":{"type":"debugdata","public":true,"max-age":86400},"cacheLifetimeMs":86400000,"cacheHitProbability":0.6,"totalBytes":103...
    · {"url":"https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":56625,"wastedBytes":5662.499...
    · {"url":"https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js","debugData":{"type":"debugdata","public":true,"max-age":604800,"s-maxage":"43200"},"cacheLifetimeMs":604800000,"cacheHitProbability":0.9,"totalBytes":11982,"wastedBytes":1...
    · {"url":"https://aiphantomtraders.com/logo.jpeg","debugData":{"type":"debugdata","public":true,"max-age":2592000},"cacheLifetimeMs":2592000000,"cacheHitProbability":0.9064245810055866,"totalBytes":2580,"wastedBytes":241.42458100558645}
- Avoid an excessive DOM size (4,689 elements)
    · {"statistic":"Total DOM Elements","value":{"type":"numeric","granularity":1,"value":4689}}
    · {"node":{"type":"node","lhId":"1-114-SPAN","path":"1,HTML,1,BODY,9,DIV,4,SECTION,0,DIV,1,DIV,2,DIV,1,DIV,1,DIV,1,DIV,3,DIV,0,DIV,0,DIV,1,SPAN,1,SPAN","selector":"div > div > span > span","boundingRect":{"top":3411,"bottom":3425,"left":1219,...
    · {"node":{"type":"node","lhId":"1-115-DIV","path":"1,HTML,1,BODY,9,DIV,0,SECTION,3,DIV,0,DIV","selector":"div#page-landing > section.v2-hero > div.v2-tape > div#v2TapeTrack","boundingRect":{"top":847,"bottom":865,"left":-321,"right":9526,"wi...
- Image elements do not have explicit `width` and `height`
    · {"url":"https://aiphantomtraders.com/logo.jpeg","node":{"type":"node","lhId":"1-177-IMG","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,0,DIV,0,DIV,0,IMG","selector":"div.v2-footer-grid > div > div > img","boundingRect":{"top":4313,"botto...

## best-practices — opportunities
- Uses deprecated APIs (2 warnings found)
    · {"value":"StorageType.persistent is deprecated. Please use standardized navigator.storage instead.","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"networ...
    · {"value":"Fledge","source":{"type":"source-location","url":"https://aiphantomtraders.com/cdn-cgi/challenge-platform/scripts/jsd/main.js","urlProvider":"network","line":0,"column":10818}}

## seo — opportunities
- Links are not crawlable
    · {"node":{"type":"node","lhId":"1-21-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-22-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,2,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4361,"bottom":4381,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-23-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,3,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4391,"bottom":4412,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-24-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,1,DIV,4,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4422,"bottom":4443,"left":271,"right":338...
    · {"node":{"type":"node","lhId":"1-25-A","path":"1,HTML,1,BODY,9,DIV,6,FOOTER,0,DIV,0,DIV,2,DIV,1,A","selector":"div.v2-footer-inner > div.v2-footer-grid > div.v2-footer-col > a","boundingRect":{"top":4330,"bottom":4351,"left":386,"right":457...
