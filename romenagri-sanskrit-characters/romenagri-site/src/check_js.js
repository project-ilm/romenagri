// Copyright (C) 1993-2026 Abhishek Choudhary
// SPDX-License-Identifier: GPL-2.0-or-later
// This file is part of the Romenagri Transliteration System; see the file COPYING.
//
// Used by romenagri-site/build_site.py --check:  node check_js.js <path of docs/romenagri.js>  <  cases.json  >  results.json
// Runs a list of cases through the JavaScript port in one process.
"use strict";
const fs = require("fs");
const R = require(require("path").resolve(process.argv[2]));
const cases = JSON.parse(fs.readFileSync(0, "utf8"));

function attempt(f) {
  try { return f(); } catch (e) { if (e && e.crash) return { crash: e.crash }; throw e; }
}

const out = cases.map(function (c) {
  switch (c.fn) {
    case "uni2acii": return R.uni2acii(c.units, { form: c.form, warn: c.warn });
    case "acii2uni": return { text: R.acii2uni(c.bytes, { form: c.form }) };
    case "acii2rmn": return R.acii2rmn(c.bytes);
    case "acii2rmnTok": return attempt(function () { return { text: R.acii2rmnTok(c.bytes) }; });
    case "rmn2acii": return R.rmn2acii(c.text);
    case "rmn2aciiRun": return attempt(function () { return { bytes: R.rmn2aciiRun(c.text) }; });
    case "chain": {
      const a = R.uni2acii(c.units, { form: c.form }).bytes;
      const r = R.acii2rmn(a);
      if (r.crash) return { crash: "acii2rmn" };
      const b = R.rmn2acii(r.text);
      if (b.crash) return { crash: "rmn2acii" };
      return { text: R.acii2uni(b.bytes, { form: c.form }) };
    }
    default: throw new Error("unknown case " + c.fn);
  }
});
process.stdout.write(JSON.stringify(out));
