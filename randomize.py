import math
import random

def getSelection(pool, Kmin=0, Kmax=1e6):
    Kmax = min(Kmax, len(pool)) + 1
    K = random.randrange(Kmin, Kmax)
    S = random.sample(pool,k=K)
    return S


def randomize(packless,ilj_snflip,batalia_si,tree_skip,oltanis_mb):
    PW   = {}
    PG   = {}
    PC   = {}
    PGC  = {}
    RSW  = {}
    RSG  = {}
    RSC  = {}
    RSGC = {}

    pool_w  = [0, 1]
    pool_g  = []
    pool_c  = [1, 2]
    pool_gc = [1, 2, 3]


    # Veldin 1
    Sw = getSelection(pool_w,0,2)
    PW[1] = [w for w in pool_w]
    PG[1] = [g for g in pool_g]
    RSW[1] = Sw


    # Novalis
    pool_w.append(2)
    Sw = getSelection(pool_w,1,3)
    PW[2] = [w for w in pool_w]
    PG[2] = [g for g in pool_g]
    RSW[2] = Sw


    # Kerwan
    pool_w.append(3)
    pool_g.append(7)
    Sw = getSelection(pool_w,0,3)
    Sg = getSelection(pool_g)
    if(not packless and 7 not in Sg):
        Sg.append(7)

    PW[3] = [w for w in pool_w]
    PG[3] = [g for g in pool_g]
    RSW[3] = Sw
    RSG[3] = Sg

    pool_g.append(3)


    # Aridia
    Sw = getSelection(pool_w,0,3)
    Sg = getSelection(pool_g)

    PW[4] = [w for w in pool_w]
    PG[4] = [g for g in pool_g]
    RSW[4] = Sw
    RSG[4] = Sg

    if(3 in Sg or (ilj_snflip and 7 in Sg)):
        pool_g.append(1)

    hoverboard = 0
    if(len(Sw)>0):
        hoverboard = 1


    # Eudora
    pool_w.append(4)
    Sw = getSelection(pool_w,0,3)
    Sg = getSelection(pool_g)
    if(not packless and 7 not in Sg):
        Sg.append(7)

    PW[5] = [w for w in pool_w]
    PG[5] = [g for g in pool_g]
    RSW[5] = Sw
    RSG[5] = Sg

    if(7 in Sg):
        pool_w.append(5)


    # Nebula G34
    Sw = getSelection(pool_w,1,4)
    Sw += getSelection([6],0,1)
    pool_w.append(6)
    Sc = getSelection(pool_c)
    if(1 not in Sc):
        Sc = []
    Sg = getSelection(pool_g)
    if(not batalia_si and 3 not in Sg):
        Sg.append(3)

    PW[6] = [w for w in pool_w]
    PC[6] = [c for c in pool_c]
    PG[6] = [g for g in pool_g]
    RSW[6] = Sw
    RSC[6] = Sc
    RSG[6] = Sg

    if(3 in Sg):
        pool_g.append(13)
    if(7 in Sg or (1 in Sg and 1 in Sc and 2 in Sc)):
        pool_g.append(2)


    # Rilgar
    pool_w.append(7)
    pool_w.append(15)
    Sw = getSelection(pool_w,0,3)
    Sg = getSelection(pool_g)
    if(not packless and 7 not in Sg):
        Sg.append(7)

    PW[7] = [w for w in pool_w]
    PG[7] = [g for g in pool_g]
    RSW[7] = Sw
    RSG[7] = Sg

    if(hoverboard or 7 in Sg):
        pool_g.append(11)


    # Umbris
    Sw = getSelection(pool_w,2,5)
    Sg = getSelection(pool_g,1,3)
    if(not packless and 7 not in Sg):
        Sg.append(7)
    if(not ilj_snflip and 3 not in Sg):
        Sg.append(3)
    if(packless and ilj_snflip and (7 not in Sg) and (3 not in Sg)):
        Sg_aux = getSelection([3, 7],1,2)
        Sg += Sg_aux

    PW[8] = [w for w in pool_w]
    PG[8] = [g for g in pool_g]
    RSW[8] = Sw
    RSG[8] = Sg


    # Batalia
    pool_w.append(8)
    Sw = getSelection(pool_w,2,5)
    Sg = getSelection(pool_g,1,3)
    if(7 not in Sg and (0 not in Sw or 13 not in Sg)):
        Sg_aux = getSelection([7, 13],1,1)
        if(13 in Sg and 13 in Sg_aux):
            Sg_aux.remove(13)
        Sg += Sg_aux
        if(7 not in Sg and 0 not in Sw):
            Sw.append(0)
    if(not batalia_si and 13 not in Sg):
        Sg.append(13)

    # Allow Magneboots
    #Sg_aux = getSelection([14],0,1)
    #Sg += Sg_aux
    metal_det = 0
    if(14 in Sg or (7 in Sg and 0 in Sw)):
        metal_det = 1

    PW[9] = [w for w in pool_w]
    PG[9] = [g for g in pool_g]
    RSW[9] = Sw
    RSG[9] = Sg


    # Orxon 1
    pool_w.append(9)
    Sc = getSelection(pool_c,0,2)
    if(1 not in Sc):
        Sc.append(1)
    if(not tree_skip and 2 not in Sc):
        Sc.append(2)

    PW[10] = []
    PC[10] = [c for c in pool_c]
    PG[10] = []
    RSW[10] = []
    RSC[10] = Sc
    RSG[10] = []

    pool_g.append(14)
    if(metal_det):
        pool_g.append(5)


    # Gaspar
    pool_w.append(10)
    Sw = getSelection(pool_w,0,4)
    Sg = getSelection(pool_g,0,3)

    PW[11] = [w for w in pool_w]
    PG[11] = [g for g in pool_g]
    RSW[11] = Sw
    RSG[11] = Sg

    pool_g.append(12)


    # Pokitaru
    pool_w.append(11)
    pool_g.append(8)
    Sw = getSelection(pool_w,3,6)
    Sg = getSelection(pool_g,1,4)
    if(12 not in Sg):
        Sg.append(12)
    if(11 not in Sw and 8 not in Sg):
        Sw += getSelection([11],0,1)
        if(11 in Sw):
            Sg += getSelection([8],0,1)
        else:
            Sg.append(8)

    PW[12] = [w for w in pool_w]
    PG[12] = [g for g in pool_g]
    RSW[12] = Sw
    RSG[12] = Sg

    pool_g.append(10)


    # Orxon 2
    pool_exO2 = [11, 12]
    pool_gO2 = [g for g in pool_g if g not in pool_exO2]
    Sw = getSelection(pool_w,4,7)
    Sg = getSelection(pool_gO2,1,4)
    if(10 not in Sg):
        Sg.append(10)
    if(not packless and 7 not in Sg and 8 not in Sg):
        Sg_aux = getSelection([7, 8],1,2)
        Sg += Sg_aux
    if(7 not in Sg and 9 not in Sw):
        Sw.append(9)
    if(packless and 7 not in Sg and 8 not in Sg):
        if(11 not in Sw):
            Sw.append(11)
        if(3 not in Sg):
            Sg.append(3)
        if(14 not in Sg):
            Sg.append(14)

    PW[13] = [w for w in pool_w]
    PG[13] = [g for g in pool_gO2]
    RSW[13] = Sw
    RSG[13] = Sg


    # Hoven
    pool_w.append(12)
    Sw = getSelection(pool_w,3,6)
    Sg = getSelection(pool_g,1,4)

    PW[14] = [w for w in pool_w]
    PG[14] = [g for g in pool_g]
    RSW[14] = Sw
    RSG[14] = Sg

    if(8 in Sg or 2 in Sg):
        pool_g.append(9)


    # Gemlik Base
    pool_gO2 = [g for g in pool_g if g not in pool_exO2]
    Sw = getSelection(pool_w,3,6)
    Sg = getSelection(pool_gO2,1,4)
    Sg.append(12)
    if(10 not in Sg):
        Sg.append(10)
    if(7 not in Sg and 8 not in Sg):
        if(8 not in Sw and 9 not in Sw):
            Sw_aux = getSelection([8, 9],1,2)
            Sw += Sw_aux
        if(1 in pool_g and 1 not in Sg):
            Sg.append(1)
        if(1 not in pool_g and 11 not in Sw):
            Sw.append(11)
        if(3 not in Sg):
            Sg.append(3)
        if(14 not in Sg):
            Sg.append(14)

    PW[15] = [w for w in pool_w]
    PG[15] = [g for g in pool_gO2] + [12]
    RSW[15] = Sw
    RSG[15] = Sg


    # Oltanis
    pool_exPack = [7, 8, 9]
    pool_gPack = [g for g in pool_g if g not in pool_exPack]
    pool_w.append(13)
    Sw = getSelection(pool_w,4,7)
    Sg = getSelection(pool_gPack,1,4)
    if(13 not in Sg and 14 not in Sg):
        Sg_aux = getSelection([13, 14],1,2)
        Sg += Sg_aux
    if(not oltanis_mb and 13 not in Sg):
        Sg.append(4)

    PW[16] = [w for w in pool_w]
    PG[16] = [g for g in pool_gPack]
    RSW[16] = Sw
    RSG[16] = Sg

    if(14 in Sg):
        pool_g.append(4)
    if(3 in Sg or 4 in Sg):
        pool_w.append(14)


    # Quartu
    Sw  = getSelection(pool_w,3,6)
    Sgc = getSelection(pool_gc,0,3)
    kalebo = 0
    if(len(Sgc)>0):
        kalebo = 1
        pool_g.append(6)
    Sg  = getSelection(pool_g,1,4)
    if(not packless and 7 not in Sg and 8 not in Sg and 4 not in Sg):
        if(4 in pool_g):
            Sg_aux = getSelection([7, 8, 4],1,1)
        else:
            Sg_aux = getSelection([7, 8],1,1)
        Sg += Sg_aux
    if(7 not in Sg and 8 not in Sg and 4 not in Sg and 3 not in Sg):
        if(4 in pool_g):
            Sg_aux = getSelection([7, 8, 3, 4],1,1)
        else:
            Sg_aux = getSelection([7, 8, 3],1,1)
        Sg += Sg_aux
        if(3 in Sg):
            if(11 not in Sw):
                Sw.append(11)
            if(6 not in Sg and 13 not in Sw):
                Sg.append(6)

    PW[17] = [w for w in pool_w]
    PGC[17] = [gc for gc in pool_gc]
    PG[17] = [g for g in pool_g]
    RSW[17] = Sw
    RSG[17] = Sg
    RSGC[17] = Sgc


    # Kalebo III
    Sw  = getSelection(pool_w,4,7)
    Sg  = getSelection(pool_g,1,4)
    if(not hoverboard and 8 not in Sg and 4 not in Sg):
        Sg_aux = getSelection([8, 4],1,1)
        Sg += Sg_aux
    if(hoverboard and 7 not in Sg and 8 not in Sg and 4 not in Sg and 11 not in Sw and 9 not in Sw):
        Sg_aux = getSelection([7, 8, 4],0,1)
        Sg += Sg_aux
        if(len(Sg_aux)==0):
            Sw_aux = getSelection([11, 9],1,1)
            Sw += Sw_aux

    PW[18] = [w for w in pool_w]
    PG[18] = [g for g in pool_g]
    RSW[18] = Sw
    RSG[18] = Sg


    # Drek's Fleet
    Sw  = getSelection(pool_w,3,6)
    Sg  = getSelection(pool_g,1,4)
    if(4 not in Sg and ((1 not in Sw and 9 not in Sw and 6 not in Sg) or (11 not in Sw and 8 not in Sg and (14 not in Sg or 10 not in Sg or 12 not in Sg)))):
        if(4 in pool_g):
            Sg += getSelection([4],0,1)
        if(4 not in Sg):
            if(6 in pool_g and 1 not in Sw and 9 not in Sw):
                Sg += getSelection([6],0,1)
            if(6 not in Sg and 1 not in Sw and 9 not in Sw):
                Sw_aux = getSelection([1, 9],1,2)
                Sw += Sw_aux
            if (11 not in Sw and 8 not in Sg and (14 not in Sg or 10 not in Sg or 12 not in Sg)):
                Sg += getSelection([8],0,1)
                if(8 not in Sg):
                    Sw += getSelection([11],0,1)
                    if(11 not in Sw):
                        if(14 not in Sg):
                            Sg.append(14)
                        if(10 not in Sg):
                            Sg.append(10)
                        if(12 not in Sg):
                            Sg.append(12)

    PW[19] = [w for w in pool_w]
    PG[19] = [g for g in pool_g]
    RSW[19] = Sw
    RSG[19] = Sg


    # Veldin 2
    pool_wDrek = [13, 15, 8, 2]
    if(5 in pool_w):
        pool_wDrek.append(5)
    pool_exDrek = [w for w in pool_w if w not in pool_wDrek]
    Sw  = getSelection(pool_wDrek,2,3)
    Sw += getSelection(pool_exDrek,2,4)
    Sgc = getSelection(pool_gc,0,3)
    Sg  = getSelection(pool_g,1,3)
    if(8 not in Sg):
        Sg.append(8)
    if(4 not in Sg and (3 not in Sg or (11 not in Sw and 7 not in Sg and 14 not in Sg))):
        if(4 in pool_g):
            Sg += getSelection([4],0,1)
        if(4 not in Sg):
            if(3 not in Sg):
                Sg.append(3)
            if(11 not in Sw and 7 not in Sg and 14 not in Sg):
                Sg_aux = getSelection([7, 14],0,2)
                Sg += Sg_aux
                if(len(Sg_aux)==0):
                    Sw.append(11)

    PW[20] = [w for w in pool_w]
    PGC[20] = [gc for gc in pool_gc]
    PG[20] = [g for g in pool_g]
    RSW[20] = Sw
    RSG[20] = Sg
    RSGC[20] = Sgc

    return PW, PG, PC, PGC, RSW, RSG, RSC, RSGC, kalebo
