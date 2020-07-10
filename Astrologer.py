"""
學習目標:
1. 學習撰寫模組，在python，一個檔案或是一個資料夾都可被視為一個模組。
2. 用test_case來測試自己寫的東西對不對
核心概念:先畫靶再射箭，先設定好自己要的結果，再開始coding。
"""


def get_constellation(month, day) -> str:
    """
    根據生日回傳正確的星座
    牡羊座	3月21日～4月20日
    金牛座	4月21日～5月20日
    雙子座	5月21日～6月20日
    巨蟹座	6月21日～7月22日
    獅子座	7月23日～8月22日
    處女座	8月23日～9月22日
    天秤座	9月23日～10月22日
    天蠍座	10月23日～11月22日
    射手座	11月23日～12月22日
    魔羯座	12月23日～1月21日
    水瓶座	1月22日～2月19日
    雙魚座	2月20日～3月20日
    """
    '''
    牡羊座 0321 ~ 0420
    金牛座 0421 ~ 0520
    雙子座 0521 ~ 0620
    巨蟹座 0621 ~ 0722
    獅子座 0723 ~ 0822
    處女座 0823 ~ 0922
    天秤座 0923 ~ 1022
    天蠍座 1023 ~ 1122
    射手座 1123 ~ 1222
    魔羯座>1223  <0121    else
    水瓶座 0122 ~ 0219
    雙魚座 0220 ~ 0320
    '''

    # convert to date string
    date = "%02d%02d" % (month, day)

    if date >= "0321" and date <= "0420":
        return "牡羊座"
    elif date >= "0421" and date <= "0520":
        return "金牛座"
    elif date >= "0521" and date <= "0620":
        return "雙子座"
    elif date >= "0621" and date <= "0722":
        return "巨蟹座"
    elif date >= "0723" and date <= "0822":
        return "獅子座"
    elif date >= "0823" and date <= "0922":
        return "處女座"
    elif date >= "0923" and date <= "1022":
        return "天秤座"
    elif date >= "1023" and date <= "1122":
        return "天蠍座"
    elif date >= "1123" and date <= "1222":
        return "射手座"
    elif date >= "0122" and date <= "0219":
        return "水瓶座"
    elif date >= "0220" and date <= "0320":
        return "雙魚座"
    else:
        return "魔羯座"


def get_each_number(number: int) -> []:
    """
    輸入一個正整數，然後將每一位數分開。
    ex get_each_number(1920) 
    return [1,9,2,0]
    """

    result = [1, 2, 3]

    result = [int(x) for x in list(str(number))]

    return result


def get_life_number(year=1900, month=1, day=1) -> int:
    """
    會回傳一個生命靈數，生命靈數的計算方式是出生年月日的每一個數字的總和，不斷加總至個位數。
    ex 1995 12 13 -> 1+9+9+5+1+2+1+3 = 31 -> 3+1 =4
    這樣生命靈數就是4
    """
    life_num = 10

    nums = get_each_number(year) + get_each_number(month) + get_each_number(
        day)

    # until single digit
    while life_num > 9:
        life_num = sum(nums)

        nums = get_each_number(life_num)

    return life_num
