def main(data):

    dat_len=len(data.values())
    

    c_1 = {}
    c_2 = {}
    c_3 = {}
    c_4 = {}
    c_5 = {}
    c_6 = {}
    c_7 = {}
    c_8 = {}
    c_9 = {}
    c_10 = {}
    c_11 = {}
    c_12 = {}
    c_13 = {}
    c_14 = {}
    c_15 = {}
    c_16 = {}
    c_17 = {}
    c_18 = {}
    if dat_len == 6 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5

        return c_1, c_2, c_3, c_4, c_5
    if dat_len == 7 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        return c_1, c_2, c_3, c_4, c_5, c_6
    if dat_len == 8 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5

        return c_1, c_2, c_3, c_4, c_5, c_6, c_7

    if dat_len == 9 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5

        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8

    if dat_len == 10 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5
        
        op_speed_sum5 = sum(map(float, data[list(data.keys())[9]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[9]]):
            c_9[car] = float(top_spd) / (top_speed_sum5 * 2) * 0.5

        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9

    if dat_len == 11 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5
        
        top_speed_sum5 = sum(map(float, data[list(data.keys())[9]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[9]]):
            c_9[car] = float(top_spd) / (top_speed_sum5 * 2) * 0.5
        
        top_speed_sum6 = sum(map(float, data[list(data.keys())[10]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[10]]):
            c_10[car] = float(top_spd) / (top_speed_sum6 * 2) * 0.5

        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10

    if dat_len == 12 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5
        
        top_speed_sum5 = sum(map(float, data[list(data.keys())[9]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[9]]):
            c_9[car] = float(top_spd) / (top_speed_sum5 * 2) * 0.5
        
        top_speed_sum6 = sum(map(float, data[list(data.keys())[10]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[10]]):
            c_10[car] = float(top_spd) / (top_speed_sum6 * 2) * 0.5

        top_speed_sum7 = sum(map(float, data[list(data.keys())[11]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[11]]):
            c_10[car] = float(top_spd) / (top_speed_sum7 * 2) * 0.5
            
        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11
    
    if dat_len == 13 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5
        
        top_speed_sum5 = sum(map(float, data[list(data.keys())[9]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[9]]):
            c_9[car] = float(top_spd) / (top_speed_sum5 * 2) * 0.5
        
        top_speed_sum6 = sum(map(float, data[list(data.keys())[10]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[10]]):
            c_10[car] = float(top_spd) / (top_speed_sum6 * 2) * 0.5

        top_speed_sum7 = sum(map(float, data[list(data.keys())[11]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[11]]):
            c_11[car] = float(top_spd) / (top_speed_sum7 * 2) * 0.5

        top_speed_sum8 = sum(map(float, data[list(data.keys())[12]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[12]]):
            c_12[car] = float(top_spd) / (top_speed_sum8 * 2) * 0.5    
        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12
    
    if dat_len == 14 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5
        
        top_speed_sum5 = sum(map(float, data[list(data.keys())[9]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[9]]):
            c_9[car] = float(top_spd) / (top_speed_sum5 * 2) * 0.5
        
        top_speed_sum6 = sum(map(float, data[list(data.keys())[10]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[10]]):
            c_10[car] = float(top_spd) / (top_speed_sum6 * 2) * 0.5

        top_speed_sum7 = sum(map(float, data[list(data.keys())[11]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[11]]):
            c_11[car] = float(top_spd) / (top_speed_sum7 * 2) * 0.5

        top_speed_sum8 = sum(map(float, data[list(data.keys())[12]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[12]]):
            c_12[car] = float(top_spd) / (top_speed_sum8 * 2) * 0.5  

        top_speed_sum9 = sum(map(float, data[list(data.keys())[13]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[13]]):
            c_13[car] = float(top_spd) / (top_speed_sum9 * 2) * 0.5    
        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, c_13
    
    if dat_len == 15 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5
        
        top_speed_sum5 = sum(map(float, data[list(data.keys())[9]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[9]]):
            c_9[car] = float(top_spd) / (top_speed_sum5 * 2) * 0.5
        
        top_speed_sum6 = sum(map(float, data[list(data.keys())[10]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[10]]):
            c_10[car] = float(top_spd) / (top_speed_sum6 * 2) * 0.5

        top_speed_sum7 = sum(map(float, data[list(data.keys())[11]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[11]]):
            c_11[car] = float(top_spd) / (top_speed_sum7 * 2) * 0.5

        top_speed_sum8 = sum(map(float, data[list(data.keys())[12]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[12]]):
            c_12[car] = float(top_spd) / (top_speed_sum8 * 2) * 0.5  

        top_speed_sum9 = sum(map(float, data[list(data.keys())[13]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[13]]):
            c_13[car] = float(top_spd) / (top_speed_sum9 * 2) * 0.5    
        
        top_speed_sum10 = sum(map(float, data[list(data.keys())[14]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[14]]):
            c_14[car] = float(top_spd) / (top_speed_sum10 * 2) * 0.5    
        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, c_13, c_14
    
    if dat_len == 16 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5
        
        top_speed_sum5 = sum(map(float, data[list(data.keys())[9]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[9]]):
            c_9[car] = float(top_spd) / (top_speed_sum5 * 2) * 0.5
        
        top_speed_sum6 = sum(map(float, data[list(data.keys())[10]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[10]]):
            c_10[car] = float(top_spd) / (top_speed_sum6 * 2) * 0.5

        top_speed_sum7 = sum(map(float, data[list(data.keys())[11]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[11]]):
            c_11[car] = float(top_spd) / (top_speed_sum7 * 2) * 0.5

        top_speed_sum8 = sum(map(float, data[list(data.keys())[12]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[12]]):
            c_12[car] = float(top_spd) / (top_speed_sum8 * 2) * 0.5  

        top_speed_sum9 = sum(map(float, data[list(data.keys())[13]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[13]]):
            c_13[car] = float(top_spd) / (top_speed_sum9 * 2) * 0.5    
        
        top_speed_sum10 = sum(map(float, data[list(data.keys())[14]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[14]]):
            c_14[car] = float(top_spd) / (top_speed_sum10 * 2) * 0.5  

        top_speed_sum11 = sum(map(float, data[list(data.keys())[15]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[15]]):
            c_15[car] = float(top_spd) / (top_speed_sum11 * 2) * 0.5  

        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, c_13, c_14, c_15

    if dat_len == 17 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5
        
        top_speed_sum5 = sum(map(float, data[list(data.keys())[9]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[9]]):
            c_9[car] = float(top_spd) / (top_speed_sum5 * 2) * 0.5
        
        top_speed_sum6 = sum(map(float, data[list(data.keys())[10]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[10]]):
            c_10[car] = float(top_spd) / (top_speed_sum6 * 2) * 0.5

        top_speed_sum7 = sum(map(float, data[list(data.keys())[11]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[11]]):
            c_11[car] = float(top_spd) / (top_speed_sum7 * 2) * 0.5

        top_speed_sum8 = sum(map(float, data[list(data.keys())[12]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[12]]):
            c_12[car] = float(top_spd) / (top_speed_sum8 * 2) * 0.5  

        top_speed_sum9 = sum(map(float, data[list(data.keys())[13]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[13]]):
            c_13[car] = float(top_spd) / (top_speed_sum9 * 2) * 0.5    
        
        top_speed_sum10 = sum(map(float, data[list(data.keys())[14]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[14]]):
            c_14[car] = float(top_spd) / (top_speed_sum10 * 2) * 0.5  

        top_speed_sum11 = sum(map(float, data[list(data.keys())[15]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[15]]):
            c_15[car] = float(top_spd) / (top_speed_sum11 * 2) * 0.5

        top_speed_sum12 = sum(map(float, data[list(data.keys())[16]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[16]]):
            c_16[car] = float(top_spd) / (top_speed_sum12 * 2) * 0.5  

        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, c_13, c_14, c_15, c_16
    
    if dat_len == 18 :
        prc_sum = sum(map(float, data[list(data.keys())[1]]))
        for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
            c_1[car] = float(coast) / (prc_sum * 2) * 0.5

        range_sum = sum(map(float, data[list(data.keys())[2]]))
        for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
            c_2[car] = float(range) / (range_sum * 2) * 0.5

        power_sum = sum(map(float, data[list(data.keys())[3]]))
        for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
            c_3[car] = float(power) / (power_sum * 2) * 0.5

        to_100_sum = sum(map(float, data[list(data.keys())[4]]))
        for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
            c_4[car] = float(c100) / (to_100_sum * 2) * 0.5

        top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
            c_5[car] = float(top_spd) / (top_speed_sum * 2) * 0.5
        
        top_speed_sum2 = sum(map(float, data[list(data.keys())[6]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[6]]):
            c_6[car] = float(top_spd) / (top_speed_sum2 * 2) * 0.5

        top_speed_sum3 = sum(map(float, data[list(data.keys())[7]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[7]]):
            c_7[car] = float(top_spd) / (top_speed_sum3 * 2) * 0.5
        
        top_speed_sum4 = sum(map(float, data[list(data.keys())[8]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[8]]):
            c_8[car] = float(top_spd) / (top_speed_sum4 * 2) * 0.5
        
        top_speed_sum5 = sum(map(float, data[list(data.keys())[9]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[9]]):
            c_9[car] = float(top_spd) / (top_speed_sum5 * 2) * 0.5
        
        top_speed_sum6 = sum(map(float, data[list(data.keys())[10]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[10]]):
            c_10[car] = float(top_spd) / (top_speed_sum6 * 2) * 0.5

        top_speed_sum7 = sum(map(float, data[list(data.keys())[11]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[11]]):
            c_11[car] = float(top_spd) / (top_speed_sum7 * 2) * 0.5

        top_speed_sum8 = sum(map(float, data[list(data.keys())[12]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[12]]):
            c_12[car] = float(top_spd) / (top_speed_sum8 * 2) * 0.5  

        top_speed_sum9 = sum(map(float, data[list(data.keys())[13]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[13]]):
            c_13[car] = float(top_spd) / (top_speed_sum9 * 2) * 0.5    
        
        top_speed_sum10 = sum(map(float, data[list(data.keys())[14]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[14]]):
            c_14[car] = float(top_spd) / (top_speed_sum10 * 2) * 0.5  

        top_speed_sum11 = sum(map(float, data[list(data.keys())[15]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[15]]):
            c_15[car] = float(top_spd) / (top_speed_sum11 * 2) * 0.5

        top_speed_sum12 = sum(map(float, data[list(data.keys())[16]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[16]]):
            c_16[car] = float(top_spd) / (top_speed_sum12 * 2) * 0.5
        
        top_speed_sum13 = sum(map(float, data[list(data.keys())[17]]))
        for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[17]]):
            c_17[car] = float(top_spd) / (top_speed_sum13 * 2) * 0.5
    else:
        print("Out Of Range")
          

        return c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, c_13, c_14, c_15, c_16, c_17


data = {'mod': ['mod1', 'mod2'], 'prc': ['111', '222'], 'rng': ['111', '222'], 'pow': ['111', '222'], 'acss': ['111', '222'], 'top': ['111', '222']}
data2 = {'mod': ['mod1', 'mod2'], 'prc': ['11', '21'], 'rng': ['12', '22'], 'pow': ['13', '23'], 'accs': ['14', '24'], 'top': ['15', '25'], 'typ': ['16', '26'], 'ada': ['17', '27']}

print(main(data))