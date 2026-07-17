def compute(x):
    """Return the society-corpus arithmetic result for ``x``.

    Consolidates the 33,105 byte-identical ``mod_<N>_<i>(x)`` functions from the
    original JavaScript corpus into a single source of truth. The original body
    accumulated ``x*1 + x*2 + x*3`` (i.e. ``6*x``) and then added 10 when the
    running total was even. The accumulation is folded into ``6 * x``; the parity
    branch is retained verbatim to preserve float edge cases (e.g. ``compute(2.5)``
    returns ``15.0`` because ``15.0`` is odd so no adjustment is applied).
    """
    r = 6 * x
    return r + 10 if r % 2 == 0 else r
