import os
import re
import numpy as np
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
            if self.length<5 or self.length>51:
                raise FriezeError('Incorrect input.')
        # third estimate 高度3到17
        if self.height < 3 or self.height>17:
            raise FriezeError('Incorrect input.')
        # fourth estimate 每个数字在0-15
        if not all(j in range(0,16) for i in self.new_list for j in i ):
            raise FriezeError('Incorrect input.')
        # print(all(j in range(0,16) for i in self.new_list for j in i ))

        #first not frieze 每行末column 只有0和1 且 第一行末为0
        first_col = [i[0] for i in self.new_list]
        final_col = [i[-1] for i in self.new_list]
        for k in range(len(first_col)):
            if final_col[k] not in {0,1}:
                raise FriezeError('Input does not represent a frieze.')
            if first_col[k] in self.num_1:
                if final_col[k] not in self.num_1:
                    raise FriezeError('Input does not represent a frieze.')
            else:
                if final_col[k] in self.num_1:
                    raise FriezeError('Input does not represent a frieze.')

        # second not frieze 第一排和最后一排必须是4 或者 4的不超边界的数字
        first_row=self.new_list[0][:-1]
        top_row_estmate = all(i in {4,12} for i in first_row)
        # print(top_row_estmate)
        if not top_row_estmate:
            raise FriezeError('Input does not represent a frieze.')
        last_row=self.new_list[-1][:-1]
        last_row_estmate = all(i in {4,5,6,7} for i in last_row)
        # print(last_row_estmate)
        if not last_row_estmate:
            raise FriezeError('Input does not represent a frieze.')
        # third not frieze period 最少为2
        self.period_num = self._period(2)
        if self.period_num < 2:
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
        for l in range(period_list_len,length,period_list_len):
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
    def _separate(self):
        self.new_array = np.array(self.new_list)
        self.array_4 = self.new_array&4
        self.array_1 = self.new_array&1
        self.array_2 = self.new_array&2
        self.array_8 = self.new_array&8
    def _horizontal_reverse(self):
        self.array_4_h = np.flipud(self.array_4)
        self.array_1_h = np.flipud(self.array_1)
        self.array_1_h = np.roll(self.array_1_h,1,axis=0)
        self.array_2_h = np.where(np.flipud(self.array_8)==8,2,0)
        self.array_8_h = np.where(np.flipud(self.array_2)==2,8,0)
        self.horizontal_h = self.array_4_h + self.array_1_h + self.array_2_h +self.array_8_h
        return self.horizontal_h
    
    def _horizontal_judge(self):
        self._horizontal_reverse()
        horizontal_reverse = self._horizontal_reverse()
        result = (self.new_array == horizontal_reverse).all()
        if result:
            return True
        else:
            return False
    def _vertical_reverse(self):
        self.array_4_v = np.roll(np.fliplr(self.array_4),-1,axis=1)
        self.array_1_v = np.fliplr(self.array_1)
        self.array_2_v = np.fliplr(self.array_2)
        self.array_2_v = np.where(np.roll(np.roll(self.array_2_v,-1,axis=0),-1,axis=1)==2,8,0)
        self.array_8_v = np.fliplr(self.array_8)
        self.array_8_v = np.where(np.roll(np.roll(self.array_8_v,1,axis=0),-1,axis=1)==8,2,0)
        self.vertical_v = self.array_4_v + self.array_1_v + self.array_2_v + self.array_8_v
        return self.vertical_v
    
    def _vertical_judge(self):
        vertical_reverse = self._vertical_reverse()
        self.vertical_period = vertical_reverse[:,:self.period_num]
        for i in range(self.period_num):
            new_period = self.new_array[:,i:i+self.period_num]
            result = (new_period == self.vertical_period).all()
            if result:
                return True
            else:
                continue
        return False
    def _horizontal_rotation(self):
        h_4 = np.flipud(self.array_4)
        h_1 = np.roll(np.flipud(self.array_1),1,axis=0)
        h_2 = np.where(np.flipud(self.array_8)==8,2,0)
        h_8 = np.where(np.flipud(self.array_2)==2,8,0)

        h_4 = np.roll(np.fliplr(h_4),-1,axis=1)
        h_1 = np.fliplr(h_1)
        h_2 = np.fliplr(h_2)
        h_2 = np.where(np.roll(np.roll(h_2,-1,axis=0),-1,axis=1)==2,8,0)
        h_8 = np.fliplr(h_8)
        h_8 = np.where(np.roll(np.roll(h_8,1,axis=0),-1,axis=1)==8,2,0)
        self.rotation_reverse = h_4 + h_1 + h_2 + h_8
        return self.rotation_reverse
    def _rotation(self):
        self.rotation_reverse = self._horizontal_rotation()
        self.rotation_period = self.rotation_reverse[:,:self.period_num]
        for i in range(self.period_num):
            new_period = self.new_array[:,i:i+self.period_num]
            result = (new_period == self.rotation_period).all()
            if result:
                return True
            else:
                continue
        return False

    
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
 
    def _glided(self):
        self.h_heng_sym = list(reversed(self.heng_grid))
        self.h_shu_sym = list(reversed(self.shu_grid))
        self.h_SE_sym = list(reversed(self.SE_grid))
        self.h_NE_sym = list(reversed(self.NE_grid))
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
    
        
    def analyse(self):
        self._separate()
        horizontal_judge = self._horizontal_judge()
        vertical_judge = self._vertical_judge()
        rotation_judge =self._rotation()
        
        self._grid()
        self.glided_judge = self._glided()
        heng = horizontal_judge
        shu = vertical_judge
        glid = self.glided_judge
        rotation = rotation_judge

        if heng == False and shu == False and glid == False and rotation == False:
            print(f'Pattern is a frieze of period {self.period_num} that is invariant under translation only.')
        if heng == False and shu == True and glid == False and rotation == False:
            print(f'Pattern is a frieze of period {self.period_num} that is invariant under translation')
            print (' '*8+'and vertical reflection only.')  
        if heng == True and shu == False and glid == False and rotation == False:
            print(f'Pattern is a frieze of period {self.period_num} that is invariant under translation')
            print (' '*8+'and horizontal reflection only.')
        if heng == False and shu == False and glid == True and rotation == False:
            print(f'Pattern is a frieze of period {self.period_num} that is invariant under translation')
            print (' '*8+'and glided horizontal reflection only.')
        if heng == False and shu == False and glid == False and rotation == True:
            print(f'Pattern is a frieze of period {self.period_num} that is invariant under translation')
            print (' '*8+'and rotation only.')
        if heng == False and shu == True and glid == True and rotation == True:
            print(f'Pattern is a frieze of period {self.period_num} that is invariant under translation,')
            print (' '*8+'glided horizontal and vertical reflections, and rotation only.')
        if heng == True and shu == True and glid == False and rotation == True:
            print(f'Pattern is a frieze of period {self.period_num} that is invariant under translation,')
            print (' '*8+'horizontal and vertical reflections, and rotation only.')


    def display(self):
        self.heng = self._heng()
        self.heng.sort(key=lambda x:x[0][1])
        self.shu = self._shu()
        self.shu.sort(key=lambda x:(x[0][0],x[0][1]))
        self.SE = self._NW_to_SE()
        self.SE.sort(key=lambda x:x[0][1])
        self.NE = self._SW_to_NE()
        self.NE.sort(key=lambda x:(x[0][1],x[0][0]))
        new_name = self.name
        new_name_list=new_name.split('.')
        new_name = new_name_list[0]+'.tex'
        with open(new_name,'w') as file1:
            file1.write('\\documentclass[10pt]{article}\n') 
            file1.write('\\usepackage{tikz}\n')
            file1.write('\\usepackage[margin=0cm]{geometry}\n')
            file1.write('\\pagestyle{empty}\n')
            file1.write('\n')
            file1.write('\\begin{document}\n')
            file1.write('\n')
            file1.write('\\vspace*{\\fill}\n')
            file1.write('\\begin{center}\n')
            file1.write('\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]\n')
            file1.write('% North to South lines\n')
            for each in self.shu:
                file1.write(' '*4+'\\draw'+' '+str(each[0]).replace(' ','')+' '+'--'+' ')
                file1.write(str(each[1]).replace(' ','')+';'+'\n')
            file1.write('% North-West to South-East lines\n')
            for each in self.SE:
                file1.write(' '*4+'\\draw'+' '+str(each[0]).replace(' ','')+' '+'--'+' ')
                file1.write(str(each[1]).replace(' ','')+';'+'\n')
            file1.write('% West to East lines\n')
            for each in self.heng:
                file1.write(' '*4+'\\draw'+' '+str(each[0]).replace(' ','')+' '+'--'+' ')
                file1.write(str(each[1]).replace(' ','')+';'+'\n')
            file1.write('% South-West to North-East lines\n')
            for each in self.NE:
                file1.write(' '*4+'\\draw'+' '+str(each[0]).replace(' ','')+' '+'--'+' ')
                file1.write(str(each[1]).replace(' ','')+';'+'\n')
            file1.write('\\end{tikzpicture}\n')
            file1.write('\\end{center}\n')
            file1.write('\\vspace*{\\fill}\n')
            file1.write('\n')
            file1.write('\\end{document}\n')



# frieze = Frieze('linan.txt')
# frieze.analyse()
# frieze.display()






