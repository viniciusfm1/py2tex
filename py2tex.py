def tabular(align, data= [], lines = 1):
    tabular = open('tabular.tex','w')
    
    begin = f'\\begin{{tabular}}{{ {align} }}\n'
    tabular.write(begin)

    if not data:
        cell = '\t&'
        cells = f'{cell*(len(align)-1)}'
        for i in range(lines-1):
            tabular.write(cells+'\t\\\\\n')
        tabular.write(cells+'\n')
    else:
        for line in data:
            cells = '& '.join(map(str,line))
            tabular.write('\t'+cells+'\\\\\n')
    
    tabular.write(f'\\end{{tabular}}')
    tabular.close()
