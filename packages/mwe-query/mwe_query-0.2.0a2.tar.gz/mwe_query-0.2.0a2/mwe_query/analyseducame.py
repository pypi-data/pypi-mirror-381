from collections import defaultdict
import os
import re
from typing import List, Tuple
from mwe_query.canonicalform import preprocess_MWE, tokenize, vblwords
from mwe_query.annotations import dropanns, lvcannotation2annotationcodedict
from sastadev.xlsx import getxlsxdata


plussym = "+"
bracketvblpattern = r"<[^>]*>"
bracketvblre = re.compile(bracketvblpattern)

illegalsymbols = """@#$%&()_{};"\\/123456789"""
illegalstrings = ['iest', 'iemnd']

ducamepath = r"D:\Dropbox\jodijk\Utrecht\researchproposals\MWEs"
ducamefilename = "DUCAME_Current.xlsx"
ducamefullname = os.path.join(ducamepath, ducamefilename)


def countvbls(rawnewcan: str) -> int:
    vblcount = 0
    # angleopen = 0
    # angleclose = 0
    # replace anglebrackteed strings by a variable name
    newcan = re.sub(bracketvblpattern, ' iets ', rawnewcan)
    tokens = tokenize(newcan)
    for token in tokens:
        if token in vblwords:
            vblcount += 1

    # for ch in newcan:
    #     if ch == "<":
    #         angleopen += 1
    #     elif ch == ">":
    #         angleclose += 1
    #
    # if angleopen == angleclose:
    #     vblcount += angleopen
    # else:
    #     print(f"Angled bracket mismatch in {newcan}")

    return vblcount


def getbracketvbls(newcan: str) -> List[str]:
    results = []
    matches = bracketvblre.finditer(newcan)
    for match in matches:
        results.append(match.group())
    return results


def getcomponents(rawnewcan: str) -> List[str]:
    components = []
    newcan = re.sub(bracketvblpattern, '', rawnewcan)
    anntokens = preprocess_MWE(newcan)
    for token, ann in anntokens:
        if ann not in dropanns:
            components.append(token)
    return components


def findlvcverbs(newcan: str) -> Tuple[str, str]:
    results = []
    errors = []
    annwords = preprocess_MWE(newcan)
    for wrd, ann in annwords:
        if ann in lvcannotation2annotationcodedict:
            anncode = lvcannotation2annotationcodedict[ann]
            results.append((wrd, anncode))
            if wrd == "":
                errors.append((anncode, newcan))
    return results, errors


def containsillegalsymbols(canform: str) -> Tuple[bool, str]:
    illegalchars = ''
    result = False
    for ch in canform:
        if ch in illegalsymbols:
            illegalchars += ch
            result = True
    return result, illegalchars


def containsillegalwords(canform: str) -> Tuple[bool, List[str]]:
    illegalwords = []
    result = False
    tokens = canform.split()
    for token in tokens:
        if token in illegalstrings:
            illegalwords.append(token)
            result = True
    return result, illegalwords


def analyseentries(ducamedata):
    vblcountdict = {}
    bracketvbldict = defaultdict(int)
    componentdict = defaultdict(list)
    compvalencydict = defaultdict(list)
    lvcverbdict = defaultdict(lambda: defaultdict(int))
    all_lvcerrors = []
    for row in ducamedata:
        newcan = row[4]
        mweid = row[0]

        wrong, wrongstr = containsillegalsymbols(newcan)
        if wrong:
            print(f'Error: Illegal symbol(s) ({wrongstr}) in {newcan}')

        wrong, wronglist = containsillegalwords(newcan)
        if wrong:
            print(f'Error: Illegal word(s) ({wronglist}) in {newcan}')

        vblcount = countvbls(newcan)
        vblcountdict[mweid] = vblcount

        bracketvbls = getbracketvbls(newcan)
        for bracketvbl in bracketvbls:
            bracketvbldict[bracketvbl] += 1

        components = getcomponents(newcan)
        componentstr = plussym.join(components)
        componentdict[(componentstr, vblcount)].append(newcan)
        compvalencydict[componentstr].append((vblcount, newcan))

        lvcverbs, lvcerrors = findlvcverbs(newcan)
        all_lvcerrors += lvcerrors
        for wrd, anncode in lvcverbs:
            lvcverbdict[anncode][wrd] += 1

    print("<<<LVC annotation errors>>>")
    for code, canform in all_lvcerrors:
        print(f"{code}: {canform}")
    print("<<<END LVC annotation errors>>>\n")

    result = (vblcountdict, bracketvbldict,
              componentdict, compvalencydict, lvcverbdict)
    return result


def run():
    exactduplicatescount = 0
    reportfilename = "ducameanalysisreport.txt"
    header, ducamedata = getxlsxdata(ducamefullname)
    vblcountdict, bracketvbldict, componentdict, compvalencydict, lvcverbdict = (
        analyseentries(ducamedata)
    )

    with open(reportfilename, "w", encoding="utf8") as reportfile:
        sortedbracketvbls = sorted(
            [(key, val) for key, val in bracketvbldict.items()], key=lambda x: x[0]
        )
        for key, val in sortedbracketvbls:
            print(key, val, file=reportfile)

        for key in componentdict:
            if len(componentdict[key]) > 1:
                componentstr, vblcnt = key
                print(f"{componentstr}, {vblcnt}:", file=reportfile)
                duplist = []
                for canform in componentdict[key]:
                    print(f"\t{canform}", file=reportfile)
                    canformtuple = tuple(canform.split())
                    if canformtuple in duplist:
                        exactduplicatescount += 1
                    else:
                        duplist.append(canformtuple)

        print("****Light Verbs****", file=reportfile)
        for lvcat in lvcverbdict:
            for wrd in lvcverbdict[lvcat]:
                frq = lvcverbdict[lvcat][wrd]
                print(f"{lvcat}\t{wrd}\t{frq}", file=reportfile)

        print("****Valency alternations****", file=reportfile)
        for compstr in compvalencydict:
            if len(compvalencydict[compstr]) > 1:
                print(f"\n{compstr}:", file=reportfile)
                sortedexamples = sorted(
                    compvalencydict[compstr], key=lambda x: x[0])
                for vblcnt, canform in sortedexamples:
                    print(f"{vblcnt}/{canform}", file=reportfile)

        print('\n*****Number of exact duplicates*****')
        print(exactduplicatescount)


if __name__ == "__main__":
    run()
