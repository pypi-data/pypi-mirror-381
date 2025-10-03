from operator import *

# Import locally
from natlog.scanner import Scanner, VarNum

trace = 0


def rp(LP):
    return ")" if LP == "(" else "]"


def from_none(LP, w):
    if w is None:
        if LP == "(":
            return ()
        if LP == "[":
            return []
    return w


# simple LL(1) recursive descent Parser
# supporting parenthesized tuples and bracket lists
# scanned from whitespace separated tokens
class Parser:
    def __init__(self, words):
        words = list(reversed(words))
        self.words = words

    def get(self):
        if self.words:
            w = self.words.pop()
            return w
        else:
            return None

    def peek(self):
        if self.words:
            w = self.words[-1]
            return w
        else:
            return None

    def par(self, LP, RP):
        w = self.get()
        assert w == LP
        return self.pars(LP, RP)

    def pars(self, LP, RP):
        w = self.peek()
        if w == RP:
            self.get()
            return from_none(LP, None)
        elif w == LP:
            t = self.par(LP, RP)
            ts = self.pars(LP, RP)
            ts = from_none(LP, ts)
            return (t, ts) if LP == "(" else [t] + ts
        elif (w == "(") or (w == "[" and w != LP):
            t = self.par(w, rp(w))
            ts = self.pars(LP, RP)
            ts = from_none(LP, ts)
            return (t, ts) if LP == "(" else [t] + ts  # type: ignore
        else:
            self.get()
            ts = self.pars(LP, RP)
            ts = from_none(LP, ts)
            return (w, ts) if LP == "(" else [w] + ts  # type: ignore

    def run(self):
        ls = sum(1 for x in self.words if x == "(")
        rs = sum(1 for x in self.words if x == ")")
        assert ls == rs
        ls = sum(1 for x in self.words if x == "[")
        rs = sum(1 for x in self.words if x == "]")
        assert ls == rs
        t = self.par("(", ")")
        t = to_tuple(t)  # flatten (...) chains
        t = lists_to_cons(t)  # convert [...] to cons-pairs
        if trace:
            print("PARSED", t)
        return t


# extracts a Prolog-like clause made of tuples
def to_clause(xs):
    if not (":" in xs or "=>" in xs):
        return xs, ()
    if "=>" in xs:
        sep = "=>"
    else:
        sep = ":"
    neck = xs.index(sep)
    head = xs[:neck]
    body = xs[neck + 1 :]

    if sep == ":":
        if "," not in xs:
            res = head, (body,)
        else:
            bss = []
            bs = []
            for b in body:
                if b == ",":
                    bss.append(tuple(bs))
                    bs = []
                else:
                    bs.append(b)
            bss.append(tuple(bs))

            res = head, tuple(bss)
        return res
    if sep == "=>":
        n0 = 100
        n = n0
        if "," not in xs:
            vs = (VarNum(n), VarNum(n + 1))
            res = head + vs, (body + vs,)
        else:
            bss = []
            bs = []
            for b in body:
                if b == ",":
                    vs = VarNum(n), VarNum(n + 1)
                    n += 1
                    bs = tuple(bs) + vs
                    bss.append(bs)
                    bs = []
                else:
                    bs.append(b)

            vs = VarNum(n), VarNum(n + 1)
            n += 1
            bs = tuple(bs) + vs
            bss.append(bs)
            head = head + (VarNum(n0), VarNum(n))

            res = head, tuple(bss)
        return res


# main exported Parser + Scanner
def parse(text, gsyms=dict(), gixs=dict(), ground=False, rule=False):
    text = clean_comments(text)
    s = Scanner(text, gsyms=gsyms, gixs=gixs, ground=ground)
    for ws in s.run():
        if not rule:
            ws = ("head_", ":") + ws
        ws = ("(",) + ws + (")",)
        p = Parser(ws)
        r = p.run()
        r = to_clause(r)
        if not rule:
            r = to_cons_list(r[1])  # type: ignore
        if not rule and ground:
            r = (r[0],)  # type: ignore # db fact

        yield r, s.names


def mparse(text, ground=False, rule=False):
    for r, ixs in parse(text, ground=ground, rule=rule):
        yield r


# turns cons-like tuples into long tuples
# do not change, deep recursion needed
def to_tuple(xy):
    if xy is None or xy == ():
        return ()
    elif isinstance(xy, list):
        return [to_tuple(x) for x in xy]
    elif not isinstance(xy, tuple):
        return xy
    else:  # tuple
        x, y = xy
        t = to_tuple(x)
        ts = to_tuple(y)
        return (t,) + ts


def from_cons_list_as_tuple(xs):
    return tuple(from_cons_list(xs))


def from_cons_list(xs):
    rs = []
    while xs:
        x, xs = xs
        rs.append(x)
    return rs


def to_cons_list(ts, end=()):
    gs = end
    for g in reversed(ts):
        gs = (g, gs)
    return gs


def to_dif_list(ts, end):
    return to_cons_list(ts, end=end)


def q(xs):
    rs = []
    while xs:
        x, xs = xs
        rs.append(x)
    return rs


def numlist(n, m):
    return to_cons_list(range(n, m))


def clean_comments(text):
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        parts = line.split("%")
        if len(parts) > 1:
            line = parts[0]
        cleaned.append(line)
    text = "\n".join(cleaned)
    return text


# -------- NEW: list-to-cons transformation --------


def lists_to_cons(x):
    """
    Recursively convert every Python list produced by [...] into cons-pairs:
      [a, b, c]     -> (a,(b,(c,())))
      [X, Y, '|', T] -> (X,(Y,T))   ; tail notation
    Works inside arbitrary nested structures.
    """
    if isinstance(x, list):
        if "|" in x:
            bar_idx = x.index("|")
            head_elems = [lists_to_cons(e) for e in x[:bar_idx]]
            tail_part = x[bar_idx + 1 :]
            if len(tail_part) != 1:
                raise SyntaxError("List tail '|' must be followed by exactly one term")
            tail = lists_to_cons(tail_part[0])
            return to_cons_list(tuple(head_elems), end=tail)
        else:
            head_elems = [lists_to_cons(e) for e in x]
            return to_cons_list(tuple(head_elems), end=())
    elif isinstance(x, tuple):
        return tuple(lists_to_cons(e) for e in x)
    else:
        return x


# -------- tests (optional dev) --------
if __name__ == "__main__":
    sample = "foo [a b | Xs]. bar [x y z]. baz []."
    print(list(parse(sample, ground=False, rule=True)))
