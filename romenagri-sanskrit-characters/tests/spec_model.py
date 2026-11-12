# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Interpreter for the formal grammar of the Romenagri -> ACII parser.

The grammar is written once, in Romenagri/TRANSLITERATION.md (section 5.3, the fenced block "rmn2acii-grammar").  This module reads that
block and runs it, so the document itself is executable:

    spec = spec_model.load_doc()                       # parse the grammar block of the document
    spec_model.spec_parse(spec, "k_ri", T, new=True)   # -> bytes, exactly what rmn2acii("k_ri") returns

Every rule has a tag: none (the rule is in every version of the parser), '+' (added by patch 0001, the Sanskrit characters) or '!' (a
guard, added by patch 0002; section 14.7 of the document).  The argument `new` names the version of the parser:

    new=False (OLD)    ignores the rules marked '+' and '!': the parser as it was before the Sanskrit patch
    new="mid" (MID)    ignores the rules marked '!':          the parser of patch 0001 alone (the Sanskrit characters, no guards)
    new=True  (NEW)    all rules:                             the parser of this package (the default)

tests/diff_parser.py compares this interpreter with the real C parsers (the three builds) and with tests/handwritten_parser.py (a
second, hand-written model) on more than a million strings.  When all of them agree, the grammar printed in the document is, by test,
the behaviour of the C code.

Exceptions are the ones of tests/model.py:  Overrun (the C code would read past the terminator: undefined behaviour),
Missing (a row that the grammar asks for is not in the table: lookup() returns NULL and the C code crashes).
"""
import os
import re

import config  # noqa: F401  (puts tools/ on sys.path)
import model

BLOCK = re.compile(r"```rmn2acii-grammar\n(.*?)\n```", re.S)
OLD, MID, NEW = False, "mid", True                 # the three versions of the parser (the values of the argument `new`)


def active(tag, new):
    """does a rule with this tag belong to the version `new` of the parser?"""
    if tag == "":
        return True
    if tag == "+":
        return new is True or new == MID
    return new is True
_TOKEN_GUARD = re.compile(r"\s*(\[[^\]]*\]|'[^']*'|\$|\.)")
_TOKEN_ACT = re.compile(r"\s*('[^']*'|[A-Za-z_][A-Za-z_0-9]*|\d+)")


class GrammarError(Exception):
    pass


class Rule:
    """tag: '' | '+' | '!' ;  guard: the tuple of guard items ;  src: the text of the rule, tag included ;  witness: the string that shows
    what the guard is for (guards only: the shortest string that breaks the pairing law of section 14.2 when this guard is left out)"""
    __slots__ = ("tag", "guard", "actions", "src", "witness")

    def __init__(self, tag, guard, actions, src, witness=None):
        self.tag, self.guard, self.actions, self.src, self.witness = tag, guard, actions, src, witness

    @property
    def text(self):
        """the rule as written, without its tag"""
        return self.src.lstrip("+! ")

    @property
    def new(self):
        """added by the Sanskrit patch (patch 0001)"""
        return self.tag == "+"


class Spec:
    def __init__(self):
        self.classes = {}
        self.states = {}                       # name -> (param or None, [Rule])
        self._index = {}                       # (state, first character, version) -> the rules that can match there, in order

    def candidates(self, state, ch, new):
        """The rules of `state` whose first guard item accepts ch (all of them, in the order of the grammar).  A pure speed-up:
        the other rules cannot match, whatever follows."""
        key = (state, ch, new)
        hit = self._index.get(key)
        if hit is None:
            hit = self._index[key] = tuple(r for r in self.states[state][1] if active(r.tag, new) and _first_accepts(r, ch))
        return hit


def _first_accepts(rule, ch):
    item = rule.guard[0]
    kind = item[0]
    if kind == "end":
        return ch == "\0"
    if kind == "any":
        return True
    if kind == "lit":
        return ch == item[1]
    return ch in item[1]


def _class_chars(spec, body):
    out = []
    for tok in body.split():
        if tok in spec.classes:
            out.extend(spec.classes[tok])
        elif len(tok) == 1:
            out.append(tok)
        else:
            raise GrammarError("unknown class item %r" % tok)
    return out


def parse_grammar(text):
    spec = Spec()
    cur = None
    for lineno, raw in enumerate(text.split("\n"), 1):
        line = raw.split("#", 1)[0].rstrip()
        wm = re.search(r"#.*\bwitness:\s*(\S+)\s*$", raw)
        if not line.strip():
            continue
        m = re.match(r"^class\s+(\w+)\s*=\s*(.*)$", line)
        if m:
            spec.classes[m.group(1)] = _class_chars(spec, m.group(2))
            continue
        m = re.match(r"^state\s+(\w+)(?:\((\w+)\))?\s*$", line)
        if m:
            cur = (m.group(2), [])
            spec.states[m.group(1)] = cur
            continue
        if cur is None:
            raise GrammarError("line %d: rule outside a state: %r" % (lineno, raw))
        tag = line.lstrip()[0] if line.lstrip()[0] in "+!" else ""
        body = line.lstrip()[1:] if tag else line
        if tag == "!" and not wm:
            raise GrammarError("line %d: a guard ('!') must name its witness in its comment, 'witness: <string>': %r" % (lineno, raw))
        if "->" not in body:
            raise GrammarError("line %d: no '->' in %r" % (lineno, raw))
        gtext, atext = body.split("->", 1)
        guard, pos = [], 0
        gtext = gtext.rstrip()
        while pos < len(gtext.rstrip()):
            m = _TOKEN_GUARD.match(gtext, pos)
            if not m:
                raise GrammarError("line %d: bad guard %r" % (lineno, gtext))
            tok = m.group(1)
            pos = m.end()
            if tok == "$":
                guard.append(("end",))
            elif tok == ".":
                guard.append(("any",))
            elif tok.startswith("'"):
                guard.extend(("lit", ch) for ch in tok[1:-1])
            else:
                chars = _class_chars(spec, tok[1:-1])
                guard.append(("set", frozenset("\0" if ch == "$" else ch for ch in chars)))
        actions = []
        for part in atext.split(";"):
            toks, pos = [], 0
            part = part.rstrip()
            while pos < len(part):
                m = _TOKEN_ACT.match(part, pos)
                if not m:
                    raise GrammarError("line %d: bad action %r" % (lineno, part))
                toks.append(m.group(1))
                pos = m.end()
            if toks:
                actions.append(tuple(toks))
        cur[1].append(Rule(tag, tuple(guard), tuple(actions), re.sub(r"\s+", " ", line.strip()), wm.group(1) if tag == "!" else None))
    for name, (param, rules) in spec.states.items():
        if not rules:
            raise GrammarError("state %s has no rules" % name)
    return spec


def load_doc(path=None):
    """the grammar of the document: RMN_GRAMMAR=<file> (any file that holds the fenced block) overrides the package's own document"""
    path = path or os.environ.get("RMN_GRAMMAR") or os.path.join(config.ROOT, "Romenagri", "TRANSLITERATION.md")
    text = open(path, encoding="utf-8").read()
    m = BLOCK.search(text)
    if not m:
        raise GrammarError("no ```rmn2acii-grammar block in %s" % path)
    return parse_grammar(m.group(1))


def spec_parse(spec, s, T, new=True, trace=None):
    """-> bytes.  If trace is a list, one entry per rule applied is appended: (state, stem, cursor, rule text, output so far)."""
    out = bytearray()
    n = len(s)
    i = 0
    state, arg = "L1", None

    def at(p):
        if p < n:
            return s[p]
        if p == n:
            return "\0"
        raise model.Overrun(p)

    def expr(toks, env):
        key = ""
        for t in toks:
            key += t[1:-1] if t.startswith("'") else env[t]
        return key

    def emit(key):
        if key not in T:
            raise model.Missing(key)
        out.extend(T[key])

    while True:
        if i > n:
            raise model.Overrun(i)
        first = at(i)
        for rule in spec.candidates(state, first, new):
            chars = [first]
            ok = True
            for item in rule.guard[1:]:
                ch = at(i + len(chars))
                kind = item[0]
                if kind == "end":
                    ok = ch == "\0"
                elif kind == "any":
                    ok = True
                elif kind == "lit":
                    ok = ch == item[1]
                else:
                    ok = ch in item[1]
                if not ok:
                    break
                chars.append(ch)
            if not ok:
                continue
            env = {"c": chars[0], "d": chars[1] if len(chars) > 1 else "", "stem": arg}
            nxt = None
            if trace is not None:
                trace.append((state, arg, i, rule.src, None))
                at_rule = len(trace) - 1
            for act in rule.actions:
                op = act[0]
                if op == "emit":
                    emit(expr(act[1:], env))
                elif op == "halant":
                    emit("^")
                elif op == "raw":
                    v = expr(act[1:], env)
                    if v != "\0":
                        out.extend(v.encode("latin-1"))
                elif op == "vocalic":
                    if len(out) > 0 and out[-1] == T["^"][0]:
                        out.pop()
                        emit(act[2][1:-1])
                    else:
                        emit(act[1][1:-1])
                elif op == "skip":
                    i += int(act[1])
                elif op == "goto":
                    nxt = (act[1], expr(act[2:], env) if len(act) > 2 else None)
                elif op == "accept":
                    if trace is not None:
                        trace[at_rule] = trace[at_rule][:4] + (bytes(out),)
                    return bytes(out)
                else:
                    raise GrammarError("unknown action %r in %r" % (op, rule.src))
            if nxt is None:
                raise GrammarError("rule without goto/accept: %r" % rule.src)
            if trace is not None:
                trace[at_rule] = trace[at_rule][:4] + (bytes(out),)
            state, arg = nxt
            break
        else:
            raise GrammarError("no rule of state %s matches at %d in %r" % (state, i, s))


# ------------------------------------------------------------------------------------------------------------------
# Static analysis: read the rules, run nothing
# ------------------------------------------------------------------------------------------------------------------
def _values(item):
    kind = item[0]
    if kind == "lit":
        return [item[1]]
    if kind == "set":
        return sorted(c for c in item[1] if c != "\0")
    return None                                    # '.' and '$': unbounded


def lookup_keys(spec, new=True, stems_out=None):
    """Every table key the grammar can ask for, worked out from the rules alone (an over-approximation: a key is listed when
    some rule can look it up, whether or not some input reaches that rule in that context).  Returns {key: sorted sources}.

    A state with a parameter (L2b) is entered with every value that some `goto` hands it; the values are propagated to a fixed point,
    then every rule is instantiated with every value of its variables.  A key in this set that the table lacks is a key whose
    use makes the C parser dereference NULL (lookup() returns NULL, strcat() crashes).

    stems_out, if given, is filled with {state: sorted stems} for the states that take a parameter (L2b: the consonant stems)."""
    stems = {name: set() for name, (param, _) in spec.states.items() if param}
    found = {}

    def expr(toks, env):
        out = ""
        for t in toks:
            if t.startswith("'"):
                out += t[1:-1]
            else:
                if env[t] is None:
                    raise GrammarError("variable %s is unbounded where a key is built" % t)
                out += env[t]
        return out

    changed = True
    while changed:
        changed = False
        for name, (param, rules) in spec.states.items():
            for stem in (sorted(stems[name]) if param else [None]):
                for rule in rules:
                    if not active(rule.tag, new):
                        continue
                    cs = _values(rule.guard[0]) or [None]
                    ds = (_values(rule.guard[1]) or [None]) if len(rule.guard) > 1 else [None]
                    where = "%s: %s" % (name, rule.text.split("->")[0].strip())
                    for c in cs:
                        for d in ds:
                            env = {"c": c, "d": d, "stem": stem}
                            for act in rule.actions:
                                op = act[0]
                                if op == "emit":
                                    found.setdefault(expr(act[1:], env), set()).add(where)
                                elif op == "halant":
                                    found.setdefault("^", set()).add(where)
                                elif op == "vocalic":
                                    for k in (act[1][1:-1], act[2][1:-1]):
                                        found.setdefault(k, set()).add(where)
                                elif op == "goto" and len(act) > 2:
                                    v = expr(act[2:], env)
                                    if v not in stems[act[1]]:
                                        stems[act[1]].add(v)
                                        changed = True
    if stems_out is not None:
        stems_out.update({k: sorted(v) for k, v in stems.items()})
    return {k: sorted(v) for k, v in found.items()}


def stats(spec, new=True):
    """(number of states, number of rules, of them added by patch 0001, of them guards (patch 0002), longest guard in characters),
    for the version `new` of the parser (the default: all rules)"""
    rules = [r for _, rs in spec.states.values() for r in rs if active(r.tag, new)]
    return len(spec.states), len(rules), sum(r.tag == "+" for r in rules), sum(r.tag == "!" for r in rules), max(len(r.guard) for r in rules)


# ------------------------------------------------------------------------------------------------------------------
# Underscores (section 14): which rules can read one in any way the grammar does not intend, and the guards that stop them
# (the rules to analyse are those of the version of the parser that has no guards: new=MID; with the guards, new=NEW, there are none)
# ------------------------------------------------------------------------------------------------------------------
def _accepts(item, ch):
    kind = item[0]
    if kind == "end":
        return ch == "\0"
    if kind == "any":
        return True
    if kind == "lit":
        return ch == item[1]
    return ch in item[1]


def _first_rule(spec, state, chars, new=True):
    padded = chars + "\0" * 8
    for r in spec.states[state][1]:
        if not active(r.tag, new):
            continue
        if len(r.guard) <= len(padded) and all(_accepts(it, padded[i]) for i, it in enumerate(r.guard)):
            return r
    return None


def sync_breakers(spec, new=True, char="_"):
    """The rules that can consume an underscore (char="_") -- or step over the terminator (char="\\0") -- otherwise than as the first
    character of a unit or as the second character of a pair.

    A rule consumes the characters from the cursor up to its `skip` count.  The first one is the one its guard tests first; every
    later one is either tested by a guard item that accepts `_` (a wildcard `.`: the rule keeps the character as plain text) or not
    tested at all (an unchecked skip: the rule jumps over it unseen).  A rule counts only if some input can really reach it with an
    underscore in that position, that is, if no earlier rule of the state catches that input first.
    Returns [(state, rule, position, kind)], kind being 'wildcard' or 'unseen'."""
    found = []
    for name, (param, rules) in spec.states.items():
        for r in rules:
            if not active(r.tag, new):
                continue
            k = len(r.guard)
            skip = sum(int(a[1]) for a in r.actions if a[0] == "skip")
            for j in range(1, skip):
                if j < k and not _accepts(r.guard[j], char):
                    continue
                def choices(i):
                    if i == j:
                        return [char]
                    if i >= k:
                        return ["x"]
                    kind, item = r.guard[i][0], r.guard[i]
                    if kind == "lit":
                        return [item[1]]
                    if kind == "set":
                        return sorted(c for c in item[1] if c != "\0") or ["\0"]
                    return ["\0"] if kind == "end" else ["x"]
                for combo in _product([choices(i) for i in range(max(k, j + 1))]):
                    if _first_rule(spec, name, "".join(combo), new) is r:
                        found.append((name, r, j, "wildcard" if j < k else "unseen"))
                        break
    return found


def _product(lists):
    out = [""]
    for opts in lists:
        out = [a + b for a in out for b in opts]
    return out


def pairing_ok(spec, T, s, new=True):
    """True/False: the output holds exactly one byte `_` (5F) per pair of underscores in the input, counting each maximal run separately.
    None where the parse is undefined (a missing row, or a read past the end of the input)."""
    try:
        out = spec_parse(spec, s, T, new)
    except (model.Overrun, model.Missing):
        return None
    return out.count(b"_") == sum(len(m.group(0)) // 2 for m in re.finditer(r"_+", s))


def breaker_witnesses(spec, T, alphabet="acehjklnortvyz_^", maxlen=4, new=True):
    """{(state, rule text): the shortest string that breaks the pairing law by way of that rule}.  Searches all strings up to maxlen
    over the alphabet; a string counts for a rule if the rule was applied with an underscore in a position it does not test."""
    sites = {}
    for name, r, j, kind in sync_breakers(spec, new):
        sites.setdefault((name, r.src), []).append(j)
    todo = set(sites)
    out = {}
    import itertools
    for length in range(1, maxlen + 1):
        for t in itertools.product(alphabet, repeat=length):
            s = "".join(t)
            trace = []
            try:
                res = spec_parse(spec, s, T, new, trace=trace)
            except (model.Overrun, model.Missing):
                continue
            if res.count(b"_") == sum(len(m.group(0)) // 2 for m in re.finditer(r"_+", s)):
                continue
            for state, stem, i, src, _ in trace:
                key = (state, src)
                if key in todo and key not in out and any(i + j < len(s) and s[i + j] == "_" for j in sites[key]):
                    out[key] = s
        if len(out) == len(todo):
            break
    return out


def doc_text(path=None):
    """the text of the document that holds the grammar (RMN_GRAMMAR=<file> overrides the package's own)"""
    path = path or os.environ.get("RMN_GRAMMAR") or os.path.join(config.ROOT, "Romenagri", "TRANSLITERATION.md")
    return open(path, encoding="utf-8").read()


def guard_rows(spec):
    """The guards of the grammar (the rules tagged '!', section 14.7): [(state, guard rule, anchor rule, witness)], in the order of the
    grammar.  The anchor of a guard is the first rule after it, in the same state, that is not a guard itself: the rule that the guard
    stands in front of.  The witness is the shortest string that breaks the pairing law when this guard alone is left out (the grammar
    names it in the comment of the guard; check_guards() shows that it does)."""
    rows = []
    for name, (param, rules) in spec.states.items():
        for i, r in enumerate(rules):
            if r.tag == "!":
                j = i + 1
                while rules[j].tag == "!":
                    j += 1
                rows.append((name, r.text, rules[j].text, r.witness))
    return rows


def without_guard(spec, n):
    """A copy of the grammar in which the n-th guard (in the order of guard_rows) is left out: to show that each guard is needed."""
    out = Spec()
    out.classes = spec.classes
    k = 0
    for name, (param, rules) in spec.states.items():
        keep = []
        for r in rules:
            if r.tag == "!":
                k += 1
                if k - 1 == n:
                    continue
            keep.append(r)
        out.states[name] = (param, keep)
    return out
