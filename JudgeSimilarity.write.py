# coding=gbk
from Dict import TrAngle as dict1  # �����ֵ�
import Character  # �������к��ֵ��б�
from tqdm import tqdm  # ������
from writenumDict import write_num_dict as dict2  # �ʻ����ֵ�
from Dict import structure_dict as dict3  # �ṹ�ֵ�
from Pronunciation import pronunciation_index

lst = Character.Symbol_lst()

file1 = open('Shape.txt', 'w')


def get_similar(char1,char2):  # char1,char2Ϊ����
    # ��ȡ����ͺ��ֱʻ���
    code1 = dict1[char1]
    code2 = dict1[char2]
    write_num1 = int(dict2[char1])
    write_num2 = int(dict2[char2])
    structure1 = dict3.setdefault(char1, None)
    structure2 = dict3.setdefault(char2, None)

    # ����ṹ���ƶ�
    if structure1 and structure2 and structure1 == structure2:
        structure_index = 1
    else:
        structure_index = 0

    # �����������ƶ�
    code_index = 0
    # �����Ϊ��λ���㣬����ͬ��ָ��+1����ͬΪ0,��Ȩ������4�ټ�Ȩ
    for _i in range(4):
        if code1[_i] == code2[_i]:
            code_index += 1
    code_index /= 4

    # ��ӷ������ƶ�
    voice_index = pronunciation_index(char1,char2)

    # �ʻ����������ƫ��ķ�ʽ���м���
    write_num_index = 1- abs((write_num1 - write_num2)/max(write_num1,write_num2))
    # ����Ȩ�ء��ʻ�Ȩ�غͽṹȨ�طֱ�ΪΪ 0.4 0.3 0.3
    write_index = code_index * 0.4 + write_num_index * 0.3 + structure_index * 0.3
    similarity_index_ = write_index * 0.5 + voice_index * 0.5

    return write_index,voice_index,similarity_index_


def main():
    print('�ν����ж�д����...')
    for i in tqdm(lst):
        file1.write(i+' ')
        for j in lst:
            if i == j:
                pass
            else:
                # ���һ����Ȩ���������ƶ��㷨�����ݱʻ�������������̶����жϣ�������ĳһ����ֵ����д��������ļ�
                write_index, voice_index, similarity_index = get_similar(i,j)
                if similarity_index >= 0.95:
                    file1.write(j)
                else:
                    pass
        file1.write('\n')
    file1.close()

if __name__ == '__main__':
    main()

