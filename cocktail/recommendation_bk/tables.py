# coding: utf-8

import random
import numpy as np
import pandas as pd
import math
import operator
import json

def cocktail_table():
    
    cocktail_df = pd.DataFrame(columns = ['idx', 'nameEng', 'nameKor', 'baseIdx', 'ingredientIdx', 'glassIdx', 'abv']) # 일단 가니쉬는 무시

    temp = pd.DataFrame([
            [0, 'gin tonic', '진 토닉', 2, [4, 11], 8, 14],
            [1, 'jack coke', '잭 콕', 0, [0, 19], 8, 14],
            [2, 'skrewdriver', '스크류드라이버', 1, [2, 12], 1, 25],
            [3, 'rum coke', '럼 콕', 3, [5, 19], 2, 14],
            [4, 'cuba libre', '쿠바 리브레', 3, [5, 15, 19], 2, 14],
            [5, 'tequila sunrise', '데낄라 선라이즈', 4, [8, 12, 23], 2, 12],
            [6, 'kahlua milk', '깔루아 밀크', 5, [9, 10], 8, 5],
            [7, 'baileys milk', '베일리스 밀크', 5, [10, 17], 8, 5],
            [8, 'martini', '마티니', 2, [4, 13], 0, 34],
            [9, 'orange blossom', '오렌지 블라썸', 2, [4, 12], 0, 20],
            [10, 'peach crush', '피치 크러쉬', 5, [14, 20, 21], 1, 4],
            [11, 'kamikaze', '카미카제', 1, [2, 15, 18], 0, 27],
            [12, 'sex on the beach', '섹스 온 더 비치', 1, [2, 14, 12, 21], 1, 7],
            [13, 'cosmopolitan', '코스모폴리탄', 1, [2, 15, 18, 21], 0, 24],
            [14, 'almond milk', '아몬드 밀크', 5, [22, 10], 8, 5],
            [15, 'orgasm', '오르가즘', 5, [9, 17, 22], 0, 20],
            [16, 'black russian', '블랙 러시안', 1, [2, 9], 8, 37],
            [17, 'white russian', '화이트 러시안', 1, [2, 9, 10], 8, 22],
            #[18, 'long island iced tea', '롱아일랜드 아이스티', [1,2,3,4], [2,4,5,8,18,19,20], 1, 19],
            [18, 'god father', '갓 파더', 0, [1, 22], 8, 34],
            [19, 'god mother', '갓 마더', 1, [2, 22], 8, 34],
            [20, 'midori sour', '미도리 사워', 5, [24, 20, 16, 11], 8, 10]
        ], columns = list(cocktail_df))

    cocktail_df = cocktail_df.append(temp)
    
    # 숫자 타입 int로 변경
    cocktail_df[['idx', 'baseIdx', 'glassIdx', 'abv']] = cocktail_df[['idx', 'baseIdx', 'glassIdx', 'abv']].astype(int)
    
    return cocktail_df


def base_table():

    base_df = pd.DataFrame(columns = ['idx', 'nameEng', 'nameKor'])

    temp = pd.DataFrame([
            [0, 'whiskey', '위스키'],
            [1, 'vodka', '보드카'],
            [2, 'gin', '진'],
            [3, 'rum', '럼'],
            [4, 'tequila', '데낄라'],
            [5, 'liqueur', '리큐르'],
            [6, 'non alcohol', '논 알콜']
        ], columns = list(base_df))

    base_df = base_df.append(temp)
    
    # 숫자 타입 int로 변경
    base_df[['idx']] = base_df[['idx']].astype(int)
    
    return base_df


def ingredient_table():
    
    ingredient_df = pd.DataFrame(columns = ['idx', 'baseIdx', 'nameEng', 'nameKor'])

    temp = pd.DataFrame([
            [0, 0, 'bourbon whiskey', '버번 위스키'],
            [1, 0, 'scotch whiskey', '스카치 위스키'],
            [2, 1, 'vodka', '보드카'],
            [3, 1, 'vodka peach', '보드카 피치'],
            [4, 2, 'dry gin', '드라이 진'],
            [5, 3, 'white rum', '화이트 럼'],
            [6, 3, 'gold rum', '골드 럼'],
            [7, 3, 'dark rum', '다크 럼'],
            [8, 4, 'tequila', '데낄라'],
            [9, 5, 'coffee liqueur', '커피 리큐르'],
            [10, 6, 'milk', '우유'],
            [11, 6, 'tonic water', '토닉 워터'],
            [12, 6, 'orange juice', '오렌지 쥬스'],
            [13, 5, 'dry vermouth', '드라이 베르무트'],
            [14, 5, 'peach schnapps', '피치 시냅스'],
            [15, 6, 'lime juice', '라임 쥬스'],
            [16, 6, 'lemon juice', '레몬 쥬스'],
            [17, 5, 'irish cream', '아이리쉬 크림'],
            [18, 5, 'triple sec', '트리플 섹'],
            [19, 6, 'coke', '콜라'],
            [20, 6, 'sweet sour mix', '스윗 사워 믹스'],
            [21, 6, 'cranberry juice', '크랜베리 쥬스'],
            [22, 5, 'amaretto', '아마레또'],
            [23, 6, 'grenadine syrup', '그레나딘 시럽'],
            [24, 5, 'melon liqueur', '멜론 리큐르']
        ], columns = list(ingredient_df))

    ingredient_df = ingredient_df.append(temp)
    
    # 숫자 타입 int로 변경
    ingredient_df[['idx', 'baseIdx']] = ingredient_df[['idx', 'baseIdx']].astype(int)

    return ingredient_df


def glass_table():

    glass_df = pd.DataFrame(columns = ['idx', 'nameEng', 'nameKor', 'size'])

    temp = pd.DataFrame([
            [0, 'Cocktail Glass', '칵테일 글래스', 4.5],
            [1, 'Highball Glass', '하이볼 글래스', 8],
            [2, 'Collins Glass', '칼린스 글래스', 12.5],
            [3, 'Pilsner Glass', '필스너 글래스', 10],
            [4, 'Sour Glass', '사워 글래스', 5],
            [5, 'Champagne Glass', '샴페인 글래스', 4],
            [6, 'Shot Glass', '샷 글래스', 1],
            [7, 'Double Shot Glass', '더블 샷 글래스', 2],
            [8, 'Old Fashioned Glass', '올드 패션드 글래스', 8]
        ], columns = list(glass_df))

    glass_df = glass_df.append(temp)
    
    # 숫자 타입 int로 변경
    glass_df[['idx']] = glass_df[['idx']].astype(int)
    
    return glass_df