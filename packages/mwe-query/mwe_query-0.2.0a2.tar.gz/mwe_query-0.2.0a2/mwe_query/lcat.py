"""
Methods for converting a standard treebank into a treebank where a
phrasal node is generated for each (relevant) non-head single word.
"""

from typing import Optional
from sastadev.sastatypes import SynTree
from sastadev.treebankfunctions import (
    getattval as gav,
    allcats as validcats,
    find1,
)
import copy
import logging
import lxml.etree as ET

log = logging.getLogger()

dummy = "dummy"


def expandnonheadwords(stree: SynTree) -> SynTree:
    # it is presupposed that the input stree is not None
    newnode = copy.copy(stree)
    for child in newnode:
        newnode.remove(child)
    if stree.tag == "node":
        for child in stree:
            if 'word' in child.attrib:
                rel = gav(child, "rel")
                if rel not in ["hd", "mwp", "hdf", "cmp"]:  # leave svp out here
                    newchild = mkphrase(child)
                else:
                    newchild = copy.copy(child)
            else:
                newchild = expandnonheadwords(child)
            newnode.append(newchild)
    else:
        for child in stree:
            newchild = expandnonheadwords(child)
            newnode.append(newchild)
    return newnode


def getlcatatt(node: SynTree) -> str:
    pt = gav(node, "pt")
    cat = gav(node, "cat")
    if cat == "mwu":
        firstchildlcat = find1(node, './node[@rel="mwp"]/@lcat')
        result = str(firstchildlcat)
    elif pt != "":
        lcat = gav(node, "lcat")
        if lcat == "part":
            result = "pp"
        else:
            result = lcat
    else:
        result = ""
    return result


def mkphrase(child: SynTree) -> SynTree:
    newnode = ET.Element("node")
    if "íd" in child.attrib:
        newnode.attrib["id"] = str(child.attrib["id"]) + "a"
    lcat = getlcatatt(child)
    if lcat in validcats:
        newnode.attrib["cat"] = lcat
    else:
        computedlcat = getlcat(child)
        if computedlcat is None:
            pass
            # newnode = copy.copy(child)   # put off to check expansion of prt in mwestructures
            # return newnode
        else:
            newnode.attrib["cat"] = computedlcat
    for att in ["begin", "end", "index", "rel"]:
        if att in child.attrib:
            newnode.attrib[att] = child.attrib[att]
    newchild = copy.copy(child)
    newchild.attrib["rel"] = "hd"
    if "index" in newchild.attrib:
        del newchild.attrib["index"]
    newnode.append(newchild)
    return newnode


def getlcat(node: SynTree, prel=None) -> Optional[str]:  # noqa: C901
    pt = gav(node, "pt")
    rel = gav(node, "rel") if prel is None else prel
    positie = gav(node, "positie")
    wvorm = gav(node, "wvorm")
    frame = gav(node, "frame")
    numtype = gav(node, "numtype")
    vwtype = gav(node, "vwtype")
    pdtype = gav(node, "pdtype")
    result: Optional[str] = "xp0"
    if (
        "word" not in node.attrib
        or "pt" not in node.attrib
        or pt in {"let", "tsw", "vg"}
    ):  # or rel in {'svp'}: put off to see what happens
        result = None
    elif rel == "mwp":
        result = "mwu"
    elif rel == "--":
        result = None
    elif pt == "n":
        result = "detp" if rel == "det" else "np"
    elif pt == "adj":
        if positie == "nom":
            result = "np"
        elif positie == "vrij":
            if "adjective" in frame or frame == "":
                result = "ap"
            elif "preposition" in frame:
                result = "pp"
            elif "adverb" in frame:
                result = "advp"
            else:
                result = "ap"
        elif positie == "postnom":
            result = "ap"
        elif positie == "prenom":
            if rel == "mod":
                result = "ap"
            elif rel == "det":
                result = "detp"
            else:
                result = "np"
    elif pt == "bw":
        if "er_adverb" in frame:
            result = "pp"
        elif "adjective" in frame:
            result = "ap"
        elif "particle" in frame:
            result = None
        else:
            result = "advp"
    elif pt == "lid":
        result = "detp"
    elif pt == "vz":
        if "particle" in frame:
            result = "pp"  # used to be "part"
        elif "adjective" in frame:
            result = "ap"
        elif "adverb" in frame:
            result = "advp"
        elif "post_p" in frame or "preposition" in frame:
            result = "pp"
        elif rel == 'obj1':      # for intransitive prepositions
            result = "advp"
        else:
            result = "pp"
    elif pt == "ww":
        if wvorm == "od":
            result = "ppres"
        elif wvorm == "vd" and positie in {"vrij", "prenom"}:
            result = "ppart"
        elif wvorm == "vd" and positie == "nom":
            result = "np"
        elif wvorm == "vd":
            result = "xp2"
        elif wvorm == "inf" and positie == "nom":
            result = "np"
        elif wvorm == "inf" and positie == "vrij":
            result = "inf"
        elif wvorm == "inf" and positie == "prenom":
            result = "inf"  # checked in Lassy-Small
        elif wvorm == "pv":
            result = "sv1"
        else:
            result = "xp3"
    elif pt == "tw" and numtype == "hoofd":
        if positie == "nom":
            result = "np"
        elif positie == "prenom" and "adjective" in frame:
            result = "ap"
        elif positie == "prenom" and ("number" in frame or frame == ""):
            result = "detp"
        elif positie == "vrij":
            result = "np"
        else:
            result = "xp4"
    elif pt == "tw" and numtype == "rang":
        result = "ap"
    elif pt == "vnw":
        if positie == "nom":
            result = "np"
        elif positie == "prenom" and "determiner" in frame:
            result = "detp"
        elif positie == "prenom" and vwtype == "bez":
            result = "detp"
        elif positie == "prenom" and vwtype == "onbep":
            result = "detp"
        elif pdtype == "adv-pron":
            result = "advp"
        elif "positie" not in node.attrib and vwtype == "aanw":
            result = "detp"
        elif rel == "det" and vwtype == "aanw":
            result = "detp"
        elif vwtype in {"aanw", "betr", "pers", "pr", "recip", "vb", "onbep", "refl", "excl"}:
            result = "np"
        else:
            result = "xp5"
    elif pt == "spec" and rel == "app":
        result = "np"
    elif pt == "spec":
        result = None
    elif pt == dummy:
        result = None
    else:
        log.warning('Unknown att value (pt) encountered in: %s',
                    ET.tostring(node))
        result = None
    if result == 'xp':
        log.warning('Unexpected att value encountered in: %s',
                    ET.tostring(node))

    return result
