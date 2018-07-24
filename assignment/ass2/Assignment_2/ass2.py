import os
import re
from collections import defaultdict
from copy import deepcopy
class FriezeError(Exception):
    def __init__(self,message):
        self.message=message

class Frieze:
    def __init__(self,name):
        self.name = name
        self.new_list=[]
        self.num_1={1,3,5,9,7,11,13,15}
        self.num_2={2,3,6,10,7,11,14,15}
        self.num_4={4,5,6,12,7,12,13,14,15}
        self.num_8={8,9,10,11,12,13,14,15}
       
        with open(self.name) as frieze:
            pattern = re.compile(r'\d+')
            pattern2 = re.compile(r'\D')
            pattern3 = re.compile(r'\S')
            for each in frieze:
                str2num=[]
                result2 = pattern2.findall(each)
                result22 = ''.join(result2)
                result3 = pattern3.findall(result22)
                if len(result3) > 0:
                    raise FriezeError('Incorrect input.')
                else:
                    result=pattern.findall(each)
                    str2num=[int(e) for e in result]
                    if len(str2num) >0:
                        self.new_list.append(str2num)
        self.length=len(self.new_list[0])
        self.height=len(self.new_list)
        # for every in self.new_list:
        #     print(every)
        # first estimate 符合长方形规则
        each_row_len={len(k) for k in self.new_list}  
        if len(each_row_len) != 1:
            raise FriezeError('Incorrect input.')
        else:
            # second estimate 长度5到51
            if self.length<5 and self.length>51:
                raise FriezeError('Incorrect input.')
        # third estimate 高度3到17
        if self.height < 3 and self.height>17:
            raise FriezeError('Incorrect input.')
        # fourth estimate 每个数字在0-15
        if not all(j in range(0,16) for i in self.new_list for j in i ):
            raise FriezeError('Incorrect input.')
        # print(all(j in range(0,16) for i in self.new_list for j in i ))

        #first not frieze 每行末column 只有0和1 且 第一行末为0
        zero_one = all(i[-1] in {0,1} for i in self.new_list)
        if self.new_list[0][-1] != 0:
            raise FriezeError('Input does not represent a frieze.')
        else:
            if not zero_one:
                raise FriezeError('Input does not represent a frieze.')
        
        # second not frieze 第一排和最后一排必须是4 或者 4的不超边界的数字
        first_row=self.new_list[0][0::-1]
        top_row_estmate = all(i in {4,12} for i in first_row)
        # print(top_row_estmate)
        if not top_row_estmate:
            raise FriezeError('Input does not represent a frieze.')
        last_row=self.new_list[-1][0::-1]
        last_row_estmate = all(i in {4,5,6,7} for i in last_row)
        # print(last_row_estmate)
        if not last_row_estmate:
            raise FriezeError('Input does not represent a frieze.')
        # third not frieze period 最少为2
        self.period_num = self._period(1)
        if self.period_num == 0:
            raise FriezeError('Input does not represent a frieze.')
        # cross 交叉
        cross = self._cross()
        if not cross:
            raise FriezeError('Input does not represent a frieze.')

    def _period_judge(self,period_list,no_last_list,h,row_len):
        length = len(no_last_list[0])
        period_judge =set()
        period_list_len = len(period_list)
        period_judge.add(tuple(period_list))
        if row_len > length//2+1:
            return (0,row_len)
        for l in range(period_list_len,length-period_list_len+1,period_list_len):
            single_tuple = tuple(no_last_list[h][l:l+period_list_len])
            if single_tuple not in period_judge:
                period_judge.add(1)
                break
            period_judge.add(tuple(no_last_list[h][l:l+period_list_len]))
        if len(period_judge) != 1:
            row_len += 1
            period_list.append(no_last_list[h][row_len-1])
            return self._period_judge(period_list,no_last_list,h,row_len)
        else:
            return (1,row_len)         
    def _period(self,row_len1):
        self.no_last_list = [i[0:-1] for i in self.new_list]
        height = len(self.no_last_list)
        period_list = []
        obtained_set=set()
        for h in range(height):
            if obtained_set == set(): 
                row_len = row_len1
                period_list = self.no_last_list[h][:row_len]
                single_data = self._period_judge(period_list,self.no_last_list,h,row_len) 
            else:
                row_len = single_data[1]
                period_list = self.no_last_list[h][:single_data[1]]
                single_data = self._period_judge(period_list,self.no_last_list,h,row_len)
            if single_data[1] != row_len:
                return self._period(max(row_len,single_data[1]))
            if single_data[0] == 0:
                return 0
            if single_data[0] == 1:
                continue
        return row_len
    def _cross(self):
        length = self.length
        height = self.height
        test_above = self.num_8
        test_below = self.num_2
        for h in range(height-1):
            top_one = 0
            top_two = 0
            for l in range(length):
                if self.new_list[h][l] in test_above:
                    top_one += 1
                if self.new_list[h+1][l] in test_below:
                    top_two += 1
                if top_one != 0 and top_two != 0 and top_one == top_two:
                    return False
                else:
                    top_one = 0
                    top_two = 0
        return True
    # -
    def _heng(self):
        heng_list=list()
        for h in range(self.height):
            count = 0
            first_ele = 0
            for l in range(self.length):
                if self.new_list[h][l] in self.num_4:
                    count += 1
                else:
                    end_ele = (l,h)
                    if count > 0:
                        heng_list.append((first_ele,end_ele))
                    count = 0
                if count == 1:
                    first_ele = (l,h)
        return heng_list
    # |
    def _shu(self):
        shu_list=list()
        for l in range(self.length):
            count = 0
            first_ele = 0 
            for h in range(self.height)[::-1]:
                if self.new_list[h][l] in self.num_1:
                    count += 1
                else:
                    end_ele =(l,h)
                    if count>0:
                        shu_list.append((end_ele,first_ele))
                    count=0
                if count == 1:
                    first_ele = (l,h)
        return shu_list
    # \
    def _NW_to_SE(self):
        N_to_W_list = []
        for h in range(self.height)[::-1]:
            l=0
            count = 0
            for k in range(self.height-h):
                l += k
                h += k
                if self.new_list[h][l] in self.num_8:
                    count += 1
                    if count == 1:
                        first_ele = (l,h)
                else:
                    end_ele = (l,h)
                    if count > 0:
                        N_to_W_list.append((first_ele,end_ele))
                    count = 0
                l -= k
                h -= k
        for l in range(1,self.length-self.height+1):
            h=0
            count = 0
            for k in range(self.height):
                h += k 
                l += k
                if self.new_list[h][l] in self.num_8:
                    count += 1
                    if count == 1:
                        first_ele = (l,h)
                else:
                    end_ele = (l,h)
                    if count > 0:
                        N_to_W_list.append((first_ele,end_ele))
                    count = 0
                l -= k
                h -= k
        for l in range((self.length-self.height)+1,self.length):
            h=0
            count = 0 
            for k in range(self.length-l):
                l += k
                h += k
                if self.new_list[h][l] in self.num_8:
                    count += 1
                    if count == 1:
                        first_ele = (l,h)
                else:
                    end_ele =(l,h)
                    if count > 0:
                        N_to_W_list.append((first_ele,end_ele))
                    count = 0
                l -= k
                h -= k
        return N_to_W_list
    #/
    def _SW_to_NE(self):
        S_to_W_list = []
        for l in range(self.length-self.height,self.length)[::-1]:
            h=self.height - 1
            count = 0
            for k in range(self.length - l):
                l += k
                h -= k
                if self.new_list[h][l] in self.num_2:
                    count += 1
                    if count == 1:
                        first_ele = (l,h)
                else:
                    end_ele = (l,h)
                    if count > 0:
                        S_to_W_list.append((first_ele,end_ele))
                    count = 0
                l -= k
                h += k
        for l in range(0,self.length-self.height)[::-1]:
            h = self.height-1
            count = 0
            for k in range(self.height):
                h -= k 
                l += k
                if self.new_list[h][l] in self.num_2:
                    count += 1
                    if count == 1:
                        first_ele = (l,h)
                else:
                    end_ele = (l,h)
                    if count > 0:
                        S_to_W_list.append((first_ele,end_ele))
                    count = 0
                l -= k
                h += k
        for h in range(self.height-1)[::-1]:
            l = 0
            count = 0 
            for k in range(h+1):
                l += k
                h -= k
                if self.new_list[h][l] in self.num_2:
                    count += 1
                    if count == 1:
                        first_ele = (l,h)
                else:
                    end_ele =(l,h)
                    if count > 0:
                        S_to_W_list.append((first_ele,end_ele))
                    count = 0
                l -= k
                h += k
        return S_to_W_list

    #横竖分离
    def _grid(self):
        self.heng_grid = deepcopy(self.no_last_list)
        for h in range(self.height):
            for l in range(self.length-1):
                if self.heng_grid[h][l] in self.num_4:
                    self.heng_grid[h][l] = 1
                else:
                    self.heng_grid[h][l] = 0
        self.shu_grid = deepcopy(self.no_last_list)
        for h in range(self.height):
            for l in range(self.length-1):
                if self.shu_grid[h][l] in self.num_1:
                    self.shu_grid[h][l] = 1
                else:
                    self.shu_grid[h][l] = 0
        self.SE_grid = deepcopy(self.no_last_list)
        for h in range(self.height):
            for l in range(self.length-1):
                if self.SE_grid[h][l] in self.num_8:
                    self.SE_grid[h][l]=1
                else:
                    self.SE_grid[h][l]=0
        self.NE_grid =  deepcopy(self.no_last_list)
        for h in range(self.height):
            for l in range(self.length-1):
                if self.NE_grid[h][l] in self.num_2:
                    self.NE_grid[h][l]=1
                else:
                    self.NE_grid[h][l]=0 
    def _heng_sym(self):
        self.h_heng_sym = list(reversed(self.heng_grid))
        self.h_shu_sym = list(reversed(self.shu_grid))
        self.h_SE_sym = list(reversed(self.SE_grid))
        self.h_NE_sym = list(reversed(self.NE_grid))
        if self.h_heng_sym != self.heng_grid:
            return False
            
        for k in range(self.height-1):
            if self.shu_grid[k+1] != self.h_shu_sym[k]:
                return False   
        if self.h_SE_sym != self.NE_grid:
            return False
        if self.h_NE_sym != self.SE_grid:
            return False
        return True
    def _shu_sym(self,he,shu,NE,SE):
        esti_num = True
        self.s_heng_1 = he
        self.s_heng_sym = deepcopy(he)
        for i in self.s_heng_sym:
            i.reverse()
        for h in range(self.height):
            if self.s_heng_sym[h] != he[h]:
                esti_num = False
        self.s_shu_1 = shu
        self.s_shu_sym = deepcopy(shu)
        for i in self.s_shu_sym:
            i.reverse()
        for h in range(self.height):
            for l in range(self.length-2):
                if self.s_shu_sym[h][l] != shu[h][l+1]:
                    esti_num = False
        self.s_SE_1 = SE
        self.s_SE_sym = deepcopy(SE)
        for i in self.s_SE_sym:
            i.reverse() 
        self.s_NE_1 = NE
        self.s_NE_sym = deepcopy(NE)
        for i in self.s_NE_sym:
            i.reverse() 
        for k in range(self.height-1):
            if self.s_SE_sym[k] != NE[k+1]:
                esti_num = False
        for k in range(self.height-1):
            if self.s_NE_sym[k+1] != SE[k]:
                esti_num = False
        
        if esti_num :
            return True
        else:
            self.single_period_shu=[i[:self.period_num] for i in self.shu_grid]
            self.single_period_heng=[i[:self.period_num] for i in self.heng_grid]
            self.single_period_SE = [i[:self.period_num] for i in self.SE_grid]
            self.single_period_NE = [i[:self.period_num] for i in self.NE_grid]
            final_result = self._shu_period()
            return final_result
       
    def _shu_period(self):
        estimate = False
        self.single_period_heng_r = deepcopy(self.single_period_heng)
        self.single_period_shu_r = deepcopy(self.single_period_shu)
        self.single_period_NE_r = deepcopy(self.single_period_NE)
        self.single_period_SE_r = deepcopy(self.single_period_SE)
        for g in range(self.period_num//2+1):
            if not estimate:
                for h in range(self.height):
                    period_heng1 = self.single_period_heng_r[h].pop()
                    self.single_period_heng_r[h].insert(0,period_heng1)
                self.single_period_heng_rr = deepcopy(self.single_period_heng_r)
                for k in self.single_period_heng_rr:
                    k.reverse()
                for h in range(self.height):
                    period_shu1 = self.single_period_shu_r[h].pop()
                    self.single_period_shu_r[h].insert(0,period_shu1)
                self.single_period_shu_rr = deepcopy(self.single_period_shu_r)
                for k in self.single_period_shu_rr:
                    k.reverse()
                for h in range(self.height):
                    period_NE1 = self.single_period_NE_r[h].pop()
                    self.single_period_NE_r[h].insert(0,period_NE1)
                self.single_period_NE_rr = deepcopy(self.single_period_NE_r)
                for k in self.single_period_NE_rr:
                    k.reverse()
                for h in range(self.height):
                    period_SE =self.single_period_SE_r[h].pop()
                    self.single_period_SE_r[h].insert(0,period_SE)
                self.single_period_SE_rr = deepcopy(self.single_period_SE_r)
                for k in self.single_period_SE_rr:
                    k.reverse()
                heng_count= 0
                heng_count1 = 0
                for h in range(self.height):
                    if heng_count == 0:
                        for l in range(self.period_num-1):
                            if self.single_period_heng_r[h][l] != self.single_period_heng_rr[h][l+1]:
                                estimate = False
                                heng_count += 1
                                break
                    else:
                        heng_count1 += 1
                        break
                if heng_count1 != 0:
                    continue
  
                if self.single_period_shu_r != self.single_period_shu_rr:
                    estimate = False
                    continue
                SE_count = 0
                SE_count1 = 0
                for h in range(self.height-1):
                    if SE_count == 0:
                        for l in range(self.period_num-1):
                            if self.single_period_SE_r[h][l] != self.single_period_NE_rr[h+1][l+1]:
                                estimate = False
                                SE_count += 1
                                break
                    else:
                        SE_count1 += 1
                        break
                if SE_count1 != 0:
                    continue
                NE_count = 0
                NE_count1 = 0 
                for h in range(self.height-1):
                    if NE_count == 0:
                        for l in range(self.period_num-1):
                            if self.single_period_NE_r[h+1][l] != self.single_period_SE_rr[h][l+1]:
                                estimate = False
                                NE_count += 1
                                break
                    else:
                        NE_count1 += 1
                        break
                if NE_count1 != 0:
                    continue

                return True
                
        return estimate
            


    def _glided(self):
        period = self.period_num
        length = self.length-1
        height = self.height
        if period % 2 != 0:
            return False
        for h in range(height):
            for i in range(length-period//2):
                if self.h_heng_sym[h][i] != self.heng_grid[h][i+period//2]:
                    return False
        for h in range(height-1):
            for i in range(length-period//2):
                if self.shu_grid[h+1][i+period//2] != self.h_shu_sym[h][i]:
                    return False
        for h in range(height):
            for i in range(length-period//2):
                if self.h_SE_sym[h][i] != self.NE_grid[h][i+period//2]:
                    return False
        for h in range(height):
            for i in range(length-period//2):
                if self.h_NE_sym[h][i] != self.SE_grid[h][i+period//2]:
                    return False
        return True
    def _rotation(self):
        self.r_shu = deepcopy(self.h_shu_sym)
        head = self.r_shu.pop()
        self.r_shu.insert(0,head)
        for h in range(self.height):
            for l in range(self.length-1):
                if self.shu_grid[h][l] != self.r_shu[h][l]:
                    self.r_shu[h][l] = max(self.shu_grid[h][l],self.r_shu[h][l]) 
        self.r_heng = deepcopy(self.h_heng_sym)
        for h in range(self.height):
            for l in range(self.length-1):
                if self.heng_grid[h][l] != self.r_heng[h][l]:
                    self.r_heng[h][l] = max(self.heng_grid[h][l],self.r_heng[h][l])
        self.r_SE = deepcopy(self.h_NE_sym)
        self.r_NE = deepcopy(self.h_SE_sym)
        for h in range(self.height):
            for l in range(self.length-1):
                if self.SE_grid[h][l] != self.r_SE[h][l]:
                    self.r_SE[h][l] = max(self.SE_grid[h][l],self.r_SE[h][l])
        for h in range(self.height):
            for l in range(self.length-1):
                if self.NE_grid[h][l] != self.r_NE[h][l]:
                    self.r_NE[h][l] = max(self.NE_grid[h][l],self.r_NE[h][l])
        result = self._shu_sym(self.r_heng,self.r_shu,self.r_NE,self.r_SE)
        return result

    def analyse(self):
        self.heng = self._heng()
        self.heng.sort(key=lambda x:x[0][1])
        self.shu = self._shu()
        self.shu.sort(key=lambda x:x[0][0])
        self.SE = self._NW_to_SE()
        self.SE.sort(key=lambda x:x[0][1])
        self.NE = self._SW_to_NE()
        self.NE.sort(key=lambda x:x[0][1])
        self._grid()
        self.heng_judge = self._heng_sym()
        self.shu_judge = self._shu_sym(self.heng_grid,self.shu_grid,self.NE_grid,self.SE_grid)
        self.glided_judge = self._glided()
        self.rotation_judge = self._rotation()
    def display(self):
        new_name = self.name
        
        with open()




frieze = Frieze('frieze_1.txt')
frieze.analyse()
heng = frieze.heng_judge
shu = frieze.shu_judge
glid = frieze.glided_judge
rotation = frieze.rotation_judge










            
            
            



            




                














