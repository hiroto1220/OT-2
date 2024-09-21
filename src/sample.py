from opentrons import protocol_api
 
metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.11'
}

# チューブラックに設置するする各溶液の種類・濃度とチューブの位置を決める
tube_data = {
    'AA_6': 'A1',
    'AA_4.15': 'A2', 
    'Mg_80': 'A4',
    'Mg_44': 'A5',
    'milliQ': 'D2',
    'cell_extract': 'D5',
}

# 各条件
condition1={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'DNA': 1,'cell_extract': 5}
condition2={'AA_4.15': 4, 'milliQ': 2.0, 'Mg_80': 2, 'DNA': 1, 'cell_extract': 5}

# ポジティブコントロール
positive_control = {
    'AA_6':5, 
    'milliQ':1, 
    'Mg_80':2, 
    'DNA':1,
    'cell_extract':5, 
}

# ネガティブコントロール
negative_control = {
    'AA_6':5, 
    'milliQ':2, 
    'Mg_80':2, 
    'cell_extract':5, 
}


# 各条件を入れるウェルを指定する
well_num = {
    'condition1': 'B1',
    'condition2': 'B2',
    'positive_control': 'C1',
    'negative_control': 'C2',
}



#========================================================================================================================================================================
# 各条件の文字列と辞書型の変数を対応させる

conditions = {
    'positive_control': positive_control,
    'condition1': condition1,
    'condition2': condition2, 
    'negative_control': negative_control,
}


# 各チューブの残量を記録する
tube_volume = {
    'AA_6': 105,
    'AA_4.15': 160,
    'AA_0.6': 160,
    'cell_extract': 200,
}


#========================================================================================================================================================================

#各溶液ごとに分注するためのサンプルコード

def run(protocol: protocol_api.ProtocolContext):
    for i in range(len(positive_control)):
        for key, value in conditions.items():  # それぞれのコンディションのi番目のkeyとvalueを取得
            if key == 'negative_control' and i == len(positive_control)-1: # negative_controlは入れる溶液の数が1つ少ないので、最後のループでbreak
                break 
            print(list(value.keys())[i],list(value.values())[i],key)

    