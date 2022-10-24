

import itertools
from top.utils.const_max_qty import MAX_QTY
from top.utils.get_model_field_qty import get_model_field_qty


def get_all_choice_pattern_combinations(choice_list, answer_class):  # Answerをimportすると循環参照になるので引数でもらう
    """
    重複無し（（'a', 'b'）と（'b', 'a'）は重複）の選択肢リストを返す。
    また、1～ユーザが選択できる最大の選択肢数（SELECT_QTY_MAX）分のパターンで作成する。
    例）
    choice_list = ['a', 'b', 'c']

    ['a']
    ['b']
    ['a', 'b']
    ['a', 'b', 'c']
    """
    pair_list = []
    SELECT_QTY_MAX = get_model_field_qty(answer_class, "choice")

    # 1～MAX_QTY.COMBI_QTY_MAX個選択時の全パターンを取得
    for i in range(1, MAX_QTY.COMBI_QTY_MAX + 1):
        for pair in itertools.combinations(choice_list, i):
            pair = list(pair)  # 後でappendする可能性があるのでリストにする

            if len(pair) < SELECT_QTY_MAX:
                for j in range(SELECT_QTY_MAX - len(pair)):
                    pair.append(None)

            pair_list.append(pair)

    return pair_list

def get_all_choice_pattern_permutations(choice_list, answer_class):  # Answerをimportすると循環参照になるので引数でもらう
    """
    重複ありのリストの選択肢リストを返す。
    get_all_choice_pattern_combinationsとは違い、最大の選択肢数（SELECT_QTY_MAX）分のパターンのみ作成する。

    例）
    choice_list = ['a', 'b', 'c']

    ['a', 'b', 'c']
    ['a', 'c', 'b']
    ['b', 'a', 'c']
    ['b', 'c', 'a']
    ['c', 'b', 'a']
    ['c', 'a', 'b']
    """
    pair_list = []
    SELECT_QTY_MAX = get_model_field_qty(answer_class, "choice")

    for pair in itertools.permutations(choice_list, len(choice_list)):
        pair = list(pair)  # 後でappendする可能性があるのでリストにする

        if len(pair) < SELECT_QTY_MAX:
            for j in range(SELECT_QTY_MAX - len(pair)):
                pair.append(None)

        pair_list.append(pair)

    return pair_list