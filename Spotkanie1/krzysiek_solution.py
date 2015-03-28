def solution(A):
    value = A[0]
    number = 0
    try:
        while number < len(A):
            value += A[value]
            number += 1
        else:
            return -1
    except IndexError:
            return(number + 1)

if __name__ == '__main__':
    test_1 = [2,3,-1,1,3]
    print(solution(test_1))
    test_2 = [1,1,-1,1,2,3,5,6]
    print(solution(test_2))
    test_3 = [2,4,-1,8,-3,4,6,9,1,3,4]
    print(solution(test_3))
    test_4 = [i for i in range(1,100000)]
    print(solution(test_4))
    
