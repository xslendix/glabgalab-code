def string_with_arrows(text, pstart, pend):
    result = ''

    istart = max(text.rfind('\n', 0, pstart.idx), 0)
    iend   = text.find('\n', istart + 1)
    if iend < 0: iend = len(text)
    
    lcount = pend.ln - pstart.ln + 1
    for i in range(lcount):
        line = text[istart:iend]
        cstart = pstart.col if i == 0 else 0
        cend   = pend.col if i == lcount - 1 else len(line) - 1

        result += line + '\n'
        result += ' ' * cstart + '^' * (cend - cstart) + ' here'

        istart = iend
        iend = text.find('\n', istart + 1)
        if iend < 0: iend = len(text)
    
    return result.replace('\t', '')