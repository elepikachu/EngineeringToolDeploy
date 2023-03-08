# -------------------------------------------------------------
# cal/calculation.py
# 计算器功能实现函数
# -------------------------------------------------------------
from iapws import iapws97


class CalculationFunc:
    # -------------------------------------------------------------
    # 函数名： water_steam_cal
    # 功能： 计算蒸汽数据
    # -------------------------------------------------------------
    def water_steam_cal(self, water_pressure_q, water_tempeature_q, water_mass_q):
        P = float(water_pressure_q / 1000000)  # pa
        T = float(water_tempeature_q)  # K
        M = float(water_mass_q)  # 万吨/年
        print(P, T, M)

        res = {}

        zone_number = iapws97._Bound_TP(T, P)

        if zone_number == None:
            res = {'z': 0, 'v': 0, 'h': 0, 's': 0, 'cp': 0, 'cv': 0, 'w': 0, 'alfav': 0, 'kt': 0, 'water_H': 0}
        else:
            if zone_number == 1:
                a = iapws97._Region1(T, P)
                v1 = a["v"]  # Specific volume, [m³/kg]
                h1 = a["h"]  # Specific enthalpy, [kJ/kg]
                s1 = a["s"]  # Specific entropy, [kJ/kgK]
                cp1 = a["cp"]  # Specific isobaric heat capacity, [kJ/kgK]
                cv1 = a["cv"]  # Specific isocoric heat capacity, [kJ/kgK]
                w1 = a["w"]  # Speed of sound, [m/s]
                alfav1 = a["alfav"]  # Cubic expansion coefficient, [1/K]
                kt1 = a["kt"]  # Isothermal compressibility, [1/MPa]
                water_H = (h1 - 83.74) * 0.001 * M * 10000
                res = {'z': 1, 'v': v1, 'h': h1, 's': s1, 'cp': cp1, 'cv': cv1, 'w': w1, 'alfav': alfav1, 'kt': kt1,
                       'water_H': water_H}
            if zone_number == 2:
                a = iapws97._Region2(T, P)
                v2 = a["v"]  # Specific volume, [m³/kg]
                h2 = a["h"]  # Specific enthalpy, [kJ/kg]
                s2 = a["s"]  # Specific entropy, [kJ/kgK]
                cp2 = a["cp"]  # Specific isobaric heat capacity, [kJ/kgK]
                cv2 = a["cv"]  # Specific isocoric heat capacity, [kJ/kgK]
                w2 = a["w"]  # Speed of sound, [m/s]
                alfav2 = a["alfav"]  # Cubic expansion coefficient, [1/K]
                kt2 = a["kt"]  # Isothermal compressibility, [1/MPa]
                water_H = (h2 - 83.74) * 0.001 * M * 10000
                res = {'z': 1, 'v': v2, 'h': h2, 's': s2, 'cp': cp2, 'cv': cv2, 'w': w2, 'alfav': alfav2, 'kt': kt2,
                       'water_H': water_H}

        return res

    # -------------------------------------------------------------
    # 函数名： carbon_content_cal
    # 功能： 计算碳缺省值
    # -------------------------------------------------------------
    def carbon_content_cal(self, NCVi_q, EFi_q):
        NCVi = float(NCVi_q)
        EFi = float(EFi_q)
        CCi = NCVi * EFi
        return CCi


class UnitConvert:
    # -------------------------------------------------------------
    # 函数名： convert_ES
    # 功能： 质量单位换算
    # -------------------------------------------------------------
    def convert_ES(self, n, unit1, unit2):
        c = [1000, 700]
        l = ['千克标油', '千克标煤']
        if unit1 not in l or unit2 not in l:
            result = 0
        else:
            unit1_index = l.index(unit1)
            unit2_index = l.index(unit2)
            print(type(n))
            print(n.get())
            num = int(n.get())
            result = num / c[unit1_index] * c[unit2_index]
        return result

    # -------------------------------------------------------------
    # 函数名： convert_E
    # 功能： 热量单位换算
    # -------------------------------------------------------------
    def convert_E(self, n, unit1, unit2):
        c = [0.2389, 1, 1000, 1000000, 1000000000, 1000000000000]
        l = ['kcal', 'KJ', 'MJ', 'GJ', 'TJ']
        if unit1 not in l or unit2 not in l:
            result = 0
        else:
            unit1_index = l.index(unit1)
            unit2_index = l.index(unit2)
            print(type(n))
            print(n.get())
            num = int(n.get())
            result = num / c[unit1_index] * c[unit2_index]
        return result

    # -------------------------------------------------------------
    # 函数名： convert_L
    # 功能： 长度单位换算
    # -------------------------------------------------------------
    def convert_L(self, n, unit1, unit2):
        c = [1000, 100, 10, 1, 0.001]
        l = ['毫米', '厘米', '分米', '米', '千米']
        if unit1 not in l or unit2 not in l:
            result = 0
        else:
            unit1_index = l.index(unit1)
            unit2_index = l.index(unit2)
            print(type(n))
            print(n.get())
            num = int(n.get())
            result = num / c[unit1_index] * c[unit2_index]
        return result
