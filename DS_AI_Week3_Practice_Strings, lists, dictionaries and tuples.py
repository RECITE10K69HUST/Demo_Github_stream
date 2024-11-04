def exercise1():
    s = str(input("Enter your string: "))
    reversed_s = s[::-1]
    result = ''
    for i in range (len(reversed_s)):
        if i%2 != 0:
            pass
        else:
            result =  result + reversed_s[i]
    s = result.capitalize()
    print(s)
    
def exercise2():
    s = str(input("Enter your Snake case string: "))
    cutting = s.split('_')
    print(cutting)
    capitalized_words = [word.capitalize() for word in cutting]
    s = ''.join(capitalized_words)
    print(s)
    
def exercise3():
    s = str(input("Enter your string: "))
    list_of_s = s.split()
    s = ' '.join(list_of_s)
    print(s)
    
def exercise4():
    s = str(input("Enter your string: "))
    real = ['b','d','i','o','p','q','v','w','x'] 
    unreal = ['d','b','i','o','q','p','v','w','x']
    def reverse(n):
        for i in range (len(real)):
            if n == real[i]:
                return unreal[i]
    def mirror(s):
        result = ''
        for i in range (len(s)):
            if s[i] not in real:
                return 'NOT POSSIBLE'
            else:
                result = reverse(s[i]) + result
        return result
    print(mirror(s))    
    
def exercise5():
    your_list = list(map(int, input("Enter your list: ").split()))
    def remove_duplicates(l):
        l_clone = l[:]
        count = 0
        for i in range (1,len(l)):
            if l[i] == l[i-1]:
                del l_clone[i-count]
                count += 1
        return l_clone
    print(remove_duplicates(your_list))
                
def exercise6():
    temp = input("Enter your 2 dimensions: ").split(' ')
    m, n = int(temp[0]), int(temp[1])

    a = []
    b = []
    c = []

    for i in range(m):
        a.append(input(f"Enter your {n} entries in row {i+1} of matrix a: ").split(' '))
    for i in range(m):
        b.append(input(f"Enter your {n} entries in row {i+1} of matrix b: ").split(' '))  
    for i in range(m):
        c.append(list())
    for i in range (m):
        for k in range (n):
            c[i].append(int(a[i][k])+int(b[i][k]))
    print(c)
    for i in range(m):
        for k in range(n-1):
            print(c[i][k], end = ' ')
        print(c[i][n-1])
        
    def list_comprehension_solution():
        temp = input().split(' ')
        m, n = int(temp[0]), int(temp[1])

        a = []
        b = []

        for i in range(m):
            a.append(input().split(' '))
        for i in range(m):
            b.append(input().split(' '))

        c = [[int(a[i][k])+int(b[i][k]) for k in range(n)] for i in range(m)]

        for i in range(m):
            for k in range(n-1):
                print(c[i][k], end = ' ')
            print(c[i][n-1])
    
def exercise7():
    n = int(input("Enter number of students: "))
    l_input = list()
    for i in range(n):
        name, score = input(f"Enter student number {i+1} name and score: ").split()
        l_input.append((name, float(score)))
    def sort_students(data): #https://docs.python.org/3/howto/sorting.html#sortinghowto
        sorted_data = sorted(data, key=lambda x:(x[1],x[0]), reverse=False) #reverse = True: sort from higher to lower
        return sorted_data 
        
    print(sort_students(l_input))    
        
def exercise8():
    string = str(input("Enter your string: "))
    def dictionary_convert(s):
        frequency = dict()
        for i in s:
            frequency[i] = frequency.get(i, 0) + 1
        return frequency
    print(dictionary_convert(string))    
    
def exercise9():
    n = str(input("Enter your list: "))
    yourlist = n.split(',')
    yourlist = list(map(int, yourlist))
    
    def transform(l):
        trans_list = []
        for num in l:
            if num % 2 == 0:
                trans_list.append(num*2)
            else:
                trans_list.append(-num)
        return trans_list
    def transform2(l):
        return [num*2 if num%2==0 else -num for num in l]
    print(transform(yourlist))
    
def exercise10():
    tmp = input().split(' ')
    m, n = int(tmp[0]), int(tmp[1])
    a = [[k for k in range(i*n+1,i*n+n+1)] for i in range(m)]
    print(a)
    for i in range(m):
        for k in range(n-1):
            print(a[i][k],end = ' ')
        print(a[i][n-1])
        
def exercise11():
    def first_method():
        shift = int(input("Enter your distance: "))
        s = str(input("Enter your string line: "))
        alphabelt = 'abcdefghijklmnopqrstuvwxyz'
        lower_s = s.lower()
        list_s = lower_s.split(' ')
        result = []
        for word in list_s:
            replace_word = ''
            for i in range(len(word)):
                replace_word += alphabelt[(alphabelt.find(word[i])+shift)%26]
            result.append(replace_word) 
        str_result = ' '.join(result)
        print(str_result) 
    def second_method():
        shift = int(input("Enter your distance: "))
        s = str(input("Enter your string line: "))
        alphabelt = 'abcdefghijklmnopqrstuvwxyz'
        list_s = s.lower().split(' ')
        def Caesar_encryption(word):
            C_word = [alphabelt[(alphabelt.find(word[i])+shift)%26] for i in range(len(word))]
            return ''.join(C_word)
        print(' '.join(list(map(Caesar_encryption,list_s))))
    def third_method():
        shift = int(input("Enter your distance: "))
        s = str(input("Enter your string line: "))
        alphabelt = 'abcdefghijklmnopqrstuvwxyz'
        print(' '.join([''.join([alphabelt[(alphabelt.find(word[i])+shift)%26] for i in range(len(word))]) for word in s.lower().split(' ')]))
    third_method()
    
def exercise12():
    n = int(input("Enter your dict lenght: "))
    first_dict = dict()
    second_dict = dict()
    for i in range(n):
        name1, value1 = input(f"Enter your first dictionary's name and value number {i+1}: ").split()
        first_dict[name1] = int(value1)
    for i in range(n):
        name2, value2 = input(f"Enter your second dictionary's name and value number {i+1}: ").split()
        second_dict[name2] = int(value2)
    
    def merge_dict(d1,d2):
        result = d1.copy()
        for key, value in d2.items():
            result[key] = result.get(key,0) + value
        return result
    print(merge_dict(first_dict, second_dict))
    
def exercise13():
    '''
    *args và **kwargs là hai cách mà Python cho phép bạn truyền một số lượng tham số không xác định cho một hàm. Chúng giúp bạn viết những hàm linh hoạt hơn.
    *args: Cho phép bạn truyền một số lượng không xác định các tham số không có tên. Các tham số này sẽ được lưu trữ trong một tuple.
    **kwargs: Cho phép bạn truyền một số lượng không xác định các tham số có tên (key-value pairs). Các tham số này sẽ được lưu trữ trong một dictionary.
    '''
    import math
    vector1_input = str(input("Enter your n-dimension of first vector: "))
    vector1 = list(map(int, vector1_input.split()))
    print(f'Enter your {len(vector1)}-dimension of second vector: ', end = '')
    vector2=list(map(int,input().split()))
    if len(vector2) != len(vector1):
        print('Your dimension of two vectors must be the same !!!')
        return 0
    def vector_distance(vector1, vector2, **kwargs):
        result = {}
        result['manhattan'] = str(sum([abs(vector1[j]-vector2[j]) for j in range(len(vector1))]))
         
        numerator = sum([(vector1[j]*vector2[j]) for j in range(len(vector1))])
        denominator = math.sqrt(sum([vector1[o]**2 for o in range(len(vector1))])) * math.sqrt(sum([vector2[o]**2 for o in range(len(vector1))]))
        cosine = numerator/denominator
        result['cosine'] = (f'{cosine:.9f}') 
        
        euclidian = math.sqrt(sum([abs(vector1[j]-vector2[j])**2 for j in range(len(vector1))]))
        result['euclidian'] = (f'{euclidian:.9f}') 
        
        if not kwargs.values():
            return result['euclidian']
        else:
            l = []
            for key in kwargs.values():
                l.append(result[key])
            return '\n'.join(l)
                
            
    print(vector_distance(vector1, vector2))
    print(vector_distance(vector1, vector2, norm='manhattan', norm2='euclidian'))
    print(vector_distance(vector1, vector2, norm='cosine'))

exercise13()