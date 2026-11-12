/* Copyright (C) 1993-2026 Abhishek Choudhary
   SPDX-License-Identifier: GPL-2.0-or-later
   This file is part of the Romenagri Transliteration System; see the file COPYING.
   The demonstration on index.html: it shows every stage of the chain for the text in the box, with romenagri.js (the four converters
   in JavaScript, compared with the C programs by build_site.py --check) and the examples of examples.js. */
(function () {
  "use strict";
  var R = window.Romenagri, EX = window.ROMENAGRI_EXAMPLES || [];
  function $(id) { return document.getElementById(id); }
  var inp = $("demo-in"), out = $("demo-out"), sel = $("demo-ex"), warn = $("demo-warn");
  if (!R || !inp || !out) return;

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }
  function codePoints(s) {
    var a = [];
    for (var i = 0; i < s.length;) {
      var cp = s.codePointAt(i);
      var h = cp.toString(16).toUpperCase();
      while (h.length < 4) h = "0" + h;
      a.push("U+" + h);
      i += cp > 0xFFFF ? 2 : 1;
    }
    return a.join(" ");
  }
  function hexBytes(a) { return a.map(R.hex2).join(" "); }
  function radio(name) { var r = document.querySelector('input[name="' + name + '"]:checked'); return r ? r.value : ""; }

  function step(title) {
    var d = el("div", "step");
    d.appendChild(el("h4", "", title));
    out.appendChild(d);
    return d;
  }
  function line(box, text, cls) { box.appendChild(el("div", "v" + (cls ? " " + cls : ""), text)); }

  function textLine(box, s) {
    /* a code point line and the text itself */
    line(box, codePoints(s));
    var t = el("div", "v dev-line", s.replace(/\r\n/g, "\n"));
    t.setAttribute("lang", "hi");
    box.appendChild(t);
  }

  function render() {
    var form = radio("demo-form") || R.defaultForm, dir = radio("demo-dir");
    var text = inp.value;
    out.textContent = "";
    var box, a, bytes, rm, back, outText;

    if (dir === "rev") {
      box = step("Romenagri, as typed");
      line(box, text);
      back = R.rmn2acii(text);
      box = step("rmn2acii: the ACII bytes");
      if (back.crash) { line(box, back.crash + "; the C program stops here (exit status 139).", "err"); return; }
      line(box, hexBytes(back.bytes));
      outText = R.acii2uni(back.bytes, { form: form });
      box = step("acii2uni, form " + form + ": Unicode");
      textLine(box, outText);
      return;
    }

    box = step("Unicode, as typed");
    textLine(box, text);

    a = R.uni2acii(text, { form: form, warn: warn.checked });
    box = step("uni2acii, form " + form + ": the ACII bytes");
    line(box, a.bytes.length ? hexBytes(a.bytes) : "(none)");
    if (a.warnings.length) line(box, a.warnings.join("\n"), "wlines");

    rm = R.acii2rmn(a.bytes);
    box = step("acii2rmn: Romenagri");
    if (rm.crash) {
      line(box, rm.crash + "; the C program stops here (exit status 139).", "err");
      box = step("acii2uni, form " + form + ": Unicode, straight from the ACII bytes");
      textLine(box, R.acii2uni(a.bytes, { form: form }));
      return;
    }
    line(box, rm.text);

    bytes = R.rmn2acii(rm.text);
    box = step("rmn2acii: the ACII bytes again");
    if (bytes.crash) { line(box, bytes.crash + "; the C program stops here (exit status 139).", "err"); return; }
    line(box, hexBytes(bytes.bytes));
    line(box, hexBytes(bytes.bytes) === hexBytes(a.bytes) ? "the same bytes as the first conversion" : "not the same bytes as the first conversion", hexBytes(bytes.bytes) === hexBytes(a.bytes) ? "ok" : "err");

    outText = R.acii2uni(bytes.bytes, { form: form });
    box = step("acii2uni, form " + form + ": Unicode again");
    textLine(box, outText);
    var a1 = text.replace(/\r\n/g, "\n"), b1 = outText.replace(/\r\n/g, "\n");
    var verdict = a1 === b1 ? "exactly the text that was typed" :
      (a1.normalize("NFD") === b1.normalize("NFD") ? "the text that was typed, up to canonical equivalence (the same letters, written as Unicode's normalisation forms write them)" :
       "not the text that was typed");
    line(box, verdict, a1 === b1 ? "ok" : (a1.normalize("NFD") === b1.normalize("NFD") ? "warn" : "err"));
  }

  EX.forEach(function (e, i) {
    var o = document.createElement("option");
    o.value = String(i);
    o.textContent = e.label;
    sel.appendChild(o);
  });
  sel.addEventListener("change", function () {
    var e = EX[Number(sel.value)];
    if (!e) return;
    inp.value = e.text;
    var r = document.querySelector('input[name="demo-dir"][value="' + e.dir + '"]');
    if (r) r.checked = true;
    warn.checked = !!e.warn;
    render();
  });
  inp.addEventListener("input", render);
  Array.prototype.forEach.call(document.querySelectorAll('input[name="demo-form"], input[name="demo-dir"], #demo-warn'), function (n) {
    n.addEventListener("change", render);
  });
  if (EX.length) { sel.value = "0"; inp.value = EX[0].text; }
  render();
})();
