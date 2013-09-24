for j in range(1,9):
    f = open('matrix/matrix%s.txt' %j, 'r')
    l=[]
    for i in range(20):
        l.append(f.readline()[3:-1].split("	   "))
    s='''digraph G {
    ranksep="3"; size = "10,10";\n'''
    index=["Sem1","Sem2","Sem3","Sem4",
              "mat","cat","hat","dog","log","fog",
              "m","a","t","k","h","d","o","g","l","f"]
    for i in range(20):
        s+='''%s [style="setlinewidth(%s)" label = "%s\\n%s" fontsize = 24 width=2.5,height=2.5];\n'''%(index[i],float(l[i][i])*100,index[i],l[i][i])

    s+='''{ rank = same ;"Sem1"; "Sem2"; "Sem3"; "Sem4" }
    { rank = same; "mat";"cat"; "dog"; "hat"; "dog" ; "log";  "fog"}
    { rank = same;"m"; "a"; "t"; "k" ;"h"; "d"; "o"; "g"; "l"; "f" }
    Sem1-> cat[style="setlinewidth(%s)"  ];
    Sem2-> cat[style="setlinewidth(%s)"  ];
    Sem2-> dog[style="setlinewidth(%s)"  ];
    Sem3-> cat[style="setlinewidth(%s)"  ];
    Sem3-> dog[style="setlinewidth(%s)"  ];
    Sem4-> dog[style="setlinewidth(%s)"  ];
    mat-> m[style="setlinewidth(%s)"  ];
    mat-> a[style="setlinewidth(%s)"  ];
    mat-> t[style="setlinewidth(%s)"  ];
    cat-> Sem1[style="setlinewidth(%s)"  ];
    cat-> Sem2[style="setlinewidth(%s)"  ];
    cat-> Sem3[style="setlinewidth(%s)"  ];
    cat-> a[style="setlinewidth(%s)"  ];
    cat-> t[style="setlinewidth(%s)"  ];
    cat-> k[style="setlinewidth(%s)"  ];
    hat-> a[style="setlinewidth(%s)"  ];
    hat-> t[style="setlinewidth(%s)"  ];
    hat-> h[style="setlinewidth(%s)"  ];
    dog-> Sem2[style="setlinewidth(%s)"  ];
    dog-> Sem3[style="setlinewidth(%s)"  ];
    dog-> Sem4[style="setlinewidth(%s)"  ];
    dog-> d[style="setlinewidth(%s)"  ];
    dog-> o[style="setlinewidth(%s)"  ];
    dog-> g[style="setlinewidth(%s)"  ];
    log-> o[style="setlinewidth(%s)"  ];
    log-> g[style="setlinewidth(%s)"  ];
    log-> l[style="setlinewidth(%s)"  ];
    fog-> o[style="setlinewidth(%s)"  ];
    fog-> g[style="setlinewidth(%s)"  ];
    fog-> f[style="setlinewidth(%s)"  ];
    m-> mat[style="setlinewidth(%s)"  ];
    a-> mat[style="setlinewidth(%s)"  ];
    a-> cat[style="setlinewidth(%s)"  ];
    a-> hat[style="setlinewidth(%s)"  ];
    t-> mat[style="setlinewidth(%s)"  ];
    t-> cat[style="setlinewidth(%s)"  ];
    t-> hat[style="setlinewidth(%s)"  ];
    k-> cat[style="setlinewidth(%s)"  ];
    h-> hat[style="setlinewidth(%s)"  ];
    d-> dog[style="setlinewidth(%s)"  ];
    o-> dog[style="setlinewidth(%s)"  ];
    o-> log[style="setlinewidth(%s)"  ];
    o-> fog[style="setlinewidth(%s)"  ];
    g-> dog[style="setlinewidth(%s)"  ];
    g-> log[style="setlinewidth(%s)"  ];
    g-> fog[style="setlinewidth(%s)"  ];
    l-> log[style="setlinewidth(%s)"  ];
    f-> fog[style="setlinewidth(%s)"  ];
    }'''%(
    float(l[0][5])*100,
    float(l[1][5])*100,
    float(l[1][7])*100,
    float(l[2][5])*100,
    float(l[2][7])*100,
    float(l[3][7])*100,
    float(l[4][10])*100,
    float(l[4][11])*100,
    float(l[4][12])*100,
    float(l[5][0])*100,
    float(l[5][1])*100,
    float(l[5][2])*100,
    float(l[5][11])*100,
    float(l[5][12])*100,
    float(l[5][13])*100,
    float(l[6][11])*100,
    float(l[6][12])*100,
    float(l[6][14])*100,
    float(l[7][1])*100,
    float(l[7][2])*100,
    float(l[7][3])*100,
    float(l[7][15])*100,
    float(l[7][16])*100,
    float(l[7][17])*100,
    float(l[8][16])*100,
    float(l[8][17])*100,
    float(l[8][18])*100,
    float(l[9][16])*100,
    float(l[9][17])*100,
    float(l[9][19])*100,
    float(l[10][4])*100,
    float(l[11][4])*100,
    float(l[11][5])*100,
    float(l[11][6])*100,
    float(l[12][4])*100,
    float(l[12][5])*100,
    float(l[12][6])*100,
    float(l[13][5])*100,
    float(l[14][6])*100,
    float(l[15][7])*100,
    float(l[16][7])*100,
    float(l[16][8])*100,
    float(l[16][9])*100,
    float(l[17][7])*100,
    float(l[17][8])*100,
    float(l[17][9])*100,
    float(l[18][8])*100,
    float(l[19][9])*100
          )

    ff= open('dot/dot%s.txt'%j, 'w')
    ff.write(s)
