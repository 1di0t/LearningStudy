import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = [[l,w] for l,w in zip(fish_length,fish_weight)]
fish_target = [1]*35 + [0]*14
#훈련과 평가의 데이터가 같으면 당연하게도 모두 예측한다. 이를 방지하기 위해 데이터를 나눈다.
# print(input_arr.shape)#input_arr(fish_data)의 크기 출력 (샘플수, 특성수)


input_arr = np.array(fish_data)#물고기 데이터를 넘파이 형식의 배열에 대입
target_arr = np.array(fish_target)#물고기 타겟을 넘파이 형식의 배열에 대입


#위에서 데이터를 나누기만 하면 샘플링 편향이 일어남 아래는 이를 방지하기 위한 코드
np.random.seed(42)#랜덤시드를 지정
index = np.arange(49)#0부터 48까지의 정수를 생성
np.random.shuffle(index)#index를 무작위로 섞음

train_input = input_arr[index[:35]]#input_arr의 값을 index의 0부터 34까지의 순서로 train_input에 대입
train_target = target_arr[index[:35]]#target_arr의 값을 index의 0부터 34까지의 순서로 train_input에 대입
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

plt.scatter(train_input[:,0], train_input[:,1])#train_input의 0번째 열과 1번째 열을 산점도로 그림 무게와 길이를 의미
plt.scatter(test_input[:,0], test_input[:,1])#test_input의 0번째 열과 1번째 열을 산점도로 그림 무게와 길이를 의미
plt.xlabel('length')#x축을 지정
plt.ylabel('weight')#y축을 지정
# plt.show()#그래프 출력
#####################################################
kn = KNeighborsClassifier()#KNeighborsClassifier 클래스의 객체를 생성하여 메서드 실행시의 데이터 초기화를 방지

kn = kn.fit(train_input, train_target)#학습
print(kn.score(test_input, test_target))#정확도를 평가하는 코드
print(kn.predict(test_input))#테스트값을 학습 데이터와 비교하여 예측하는 코드
print(test_target)#실제값 출력